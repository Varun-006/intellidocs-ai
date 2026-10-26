
from fastapi import FastAPI, UploadFile, File, HTTPException
from pypdf import PdfReader
from io import BytesIO

app = FastAPI(title="IntelliDocs AI")


@app.get("/")
def home():
    return {
        "message": "Welcome to IntelliDocs AI!",
        "status": "Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a PDF file."
        )

    try:
        content = await file.read()

        if not content:
            raise HTTPException(
                status_code=400,
                detail="The uploaded file is empty."
            )

        reader = PdfReader(BytesIO(content))
        extracted_text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"

        return {
                "filename": file.filename,
                "pages": len(reader.pages),
                "characters_extracted": len(extracted_text),
                "preview": extracted_text[:2000].strip().splitlines()
              }
        

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Could not read this PDF. Please check that it is a valid PDF."
        )
