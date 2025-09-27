from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from src.backend.file_to_metrics import parse_excel_to_metrics

app = FastAPI(title="Investor Reporting API", version="0.1")


@app.post("/file")
async def upload_excel(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        metrics = parse_excel_to_metrics(file_bytes)
        return JSONResponse(content=metrics.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse Excel: {str(e)}")
