from pydantic import BaseModel
from datetime import datetime

class FileSchema(BaseModel):
    base64str: str

class FileResponseSchema(BaseModel):
    filename: str
    filetype: str
    size: int
    url: str
    created_at: datetime
    
    class Config:
        from_attributes = True

class FileDeleteSchema(BaseModel):
    filename: str