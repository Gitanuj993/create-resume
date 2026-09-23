"""
API Gateway
"""

from fastapi import FastAPI
from pydantic import BaseModel

# create app
app = FastAPI()

# Health
@app.get("/health")
async def health() :
  return { "message" : "Healthy" }

# data recieve from json
@app.post("/create_resume")
async def create_resume():
  pass




