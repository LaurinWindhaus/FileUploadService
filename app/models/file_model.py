from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from core.database import Base

class Files(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, nullable=False)
    filename = Column(String, unique=True, nullable=False)
    filetype = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())

    # __repr__ = {"id": id, "filename": filename, "filetype": filetype, "size": size, "url": url, "created_at": created_at}