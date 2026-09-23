from pydantic import BaseModel


class ResumeRequest(BaseModel):
    name: str
    email: str
    phone: str
    summary: str
