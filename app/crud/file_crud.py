from sqlalchemy.orm import Session
import models.file_model as file_model, schemas.file_schema as file_schema
from core.utils import save_file_to_storage, delete_file_from_storage

def get_files(db: Session, filetype: str = None):
    if filetype:
        return db.query(file_model.Files).filter(file_model.Files.filetype == filetype).all()
    return db.query(file_model.Files).all()

def get_file(filename, db: Session):
    return db.query(file_model.Files).filter(file_model.Files.filename == filename).first()

def upload_file(new_file: file_schema.FileSchema, db: Session):
    result = save_file_to_storage(new_file.base64str)
    if "error" in result:
        return None
    new_file = file_model.Files(**result)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)
    return new_file

def delete_file(file_to_delete: file_schema.FileDeleteSchema, db: Session):
    file_to_delete = db.query(file_model.Files).filter(file_model.Files.filename == file_to_delete.filename).first()
    if file_to_delete is None:
        return None
    delete_file_from_storage(file_to_delete.filename)
    db.delete(file_to_delete)
    db.commit()
    return file_to_delete