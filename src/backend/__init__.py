from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from ..commons import FormData
from .db import Report, SubmissionState, load_db, save_db
from .file_to_metrics import parse_excel_to_metrics, parse_text_to_metrics


db: list[Report] = []


@asynccontextmanager
async def lifespan(app: FastAPI):
    global db
    db = load_db()
    yield
    save_db(db)


app = FastAPI(title="Investor Reporting API", version="0.1", lifespan=lifespan)


@app.post("/startup-report/file")
async def parse_startup_report(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Couldn't read file: {str(e)}")
    try:
        file_content = file_bytes.decode("utf-8")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Couldn't decode file: {str(e)}")
    if file.filename is None:
        raise HTTPException(status_code=400, detail="File name is required")
    else:
        file_name = file.filename
    try:
        if file_name.endswith((".xlsx", ".xls")):
            metrics = parse_excel_to_metrics(file_content)
        else:
            # Assume text/CSV file parsing
            file_content = file_bytes.decode("utf-8")
            metrics = parse_text_to_metrics(file_content)
        db.append(Report(form_data=metrics, state=SubmissionState.DRAFT))
        return JSONResponse(content=metrics.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse Excel: {str(e)}")


@app.post("/startup-report/")
async def uplod_draft(report: Report):
    db.append(report)


@app.get("/startup-report")
async def get_current_draft() -> Optional[FormData]:
    try:
        report = db[-1]
        if report.state == SubmissionState.DRAFT:
            return report.form_data
        else:
            return None
    except IndexError:
        return None
