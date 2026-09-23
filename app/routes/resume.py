
from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas.resume import ResumeRequest

router = APIRouter(prefix="/resume",tags=["Resume"])

@router.post("/generate")
async def generate_resume(data:ResumeRequest) :
  return { "msg" : " request recieved successfully" }
