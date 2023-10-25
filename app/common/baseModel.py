import uuid

from sqlalchemy import Column, DateTime, String, func

from config import db


def default_uuid():
    return uuid.uuid4().hex

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(String(40), primary_key=True, default=lambda: default_uuid())
    createdOn = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    updatedOn = Column(DateTime(timezone=True), onupdate=func.now())
    deletedOn = Column(DateTime(timezone=True), default=None)
