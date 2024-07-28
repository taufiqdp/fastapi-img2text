from pydantic import BaseModel
from fastapi import APIRouter, UploadFile, File
from pathlib import Path

from models.ml import extract_text

router = APIRouter(
    prefix="/extract",
    tags=["extract"]
)


@router.post("/")
async def extract(file: UploadFile = File(...)):
    contents = await file.read()
    
    return extract_text(contents=contents)

