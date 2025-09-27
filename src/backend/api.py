from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd
from io import BytesIO

# Import your Pydantic model
from src.commons import FinancialBusinessMetrics  # adjust to actual package/module name

app = FastAPI(title="Investor Reporting API", version="0.1")


def parse_excel_to_metrics(file_bytes: bytes) -> FinancialBusinessMetrics:
    """Parse uploaded Excel bytes and map values into the metrics model."""
    df = pd.read_excel(BytesIO(file_bytes))

    # Expect Excel columns to match model field names (MVP assumption)
    data = {}
    for field in FinancialBusinessMetrics.model_fields.keys():
        if field in df.columns:
            value = df[field].dropna().iloc[0]  # first non-empty value
            data[field] = value

    return FinancialBusinessMetrics(**data)


@app.post("/file")
async def upload_excel(file: UploadFile = File(...)):
    try:
        file_bytes = await file.read()
        metrics = parse_excel_to_metrics(file_bytes)
        return JSONResponse(content=metrics.model_dump())
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to parse Excel: {str(e)}")
