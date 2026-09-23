
from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas.resume import ResumeRequest
from app.services.resume_service import generate_resume

router = APIRouter(prefix="/resume",tags=["Resume"])

@router.post("/generate")
def generate_resume(data:ResumeRequest) :
  pdf_path = generate_resume(data)
  return FileResponse(
    path=pdf_path,
    media_type="application/pdf",
    filename="resume.pdf"
  )
