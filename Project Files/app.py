from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from model.granite_model import generate_code, fix_code, document_code
from utils.pdf_utils import extract_text_from_pdf

app = FastAPI(title="SmartSDLC AI")

class Prompt(BaseModel):
    text: str

@app.post("/generate-code")
def generate_code_api(prompt: Prompt):
    result = generate_code(prompt.text)
    return {"result": result}

@app.post("/fix-code")
def fix_code_api(prompt: Prompt):
    result = fix_code(prompt.text)
    return {"result": result}

@app.post("/document-code")
def document_code_api(prompt: Prompt):
    result = document_code(prompt.text)
    return {"result": result}

@app.post("/pdf-to-code/")
async def pdf_to_code(file: UploadFile = File(...)):
    contents = await file.read()
    extracted_text = extract_text_from_pdf(contents)
    result = generate_code(extracted_text)
    return {"result": result}
