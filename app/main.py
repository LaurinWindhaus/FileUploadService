from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from core.database import engine, Base
from api.file_api import router
import os

Base.metadata.create_all(bind=engine)

# uvicorn main:app --reload
app = FastAPI()

allowed_origins = [
    "http://127.0.0.1:5000",
    "http://localhost:5000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/fileservice/file", tags=["file"])

os.makedirs("uploaded_files", exist_ok=True)
app.mount("/fileservice/uploaded_files", StaticFiles(directory="uploaded_files"), name="uploaded_files")