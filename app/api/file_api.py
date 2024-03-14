from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from crud.file_crud import get_files, get_file, upload_file, delete_file
from schemas.file_schema import FileSchema, FileResponseSchema, FileDeleteSchema
from core.database import get_db

router = APIRouter()

# @router.get("/", response_model=List[FileResponseSchema])
# def read_files(filetype: str=None, db: Session = Depends(get_db)):
#     files = get_files(db, filetype)
#     if files == None:
#         raise HTTPException(status_code=404, detail="Files not found")
#     return files

@router.get("/{filename}", response_model=FileResponseSchema)
def read_file(filename, db: Session = Depends(get_db)):
    requested_file = get_file(filename, db)
    if requested_file == None:
        raise HTTPException(status_code=404, detail="File not found")
    return requested_file

@router.post("/upload", response_model=FileResponseSchema, status_code=status.HTTP_201_CREATED)
def create_file(new_file: FileSchema, db: Session = Depends(get_db)):
    new_file = upload_file(new_file, db)
    if new_file == None:
        raise HTTPException(status_code=400, detail="Invalid Base64String")
    return new_file

@router.delete("/delete", status_code=status.HTTP_200_OK)
def remove_file_endpoint(file_to_delete: FileDeleteSchema, db: Session = Depends(get_db)):
    file_to_delete = delete_file(file_to_delete, db)
    if file_to_delete is None:
        raise HTTPException(status_code=404, detail="File not found")
    return {"message": "File deleted successfully"}