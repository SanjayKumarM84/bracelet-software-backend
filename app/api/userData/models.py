from sqlalchemy import (ARRAY, JSON, BigInteger, Boolean, Column, DateTime,
                        Float, String, Text, func)

from app.common.baseModel import BaseModel
from config import app, db


class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String(50), nullable=True)
    phoneNo = Column(BigInteger, nullable=True)
    email = Column(Text)
    age = Column(BigInteger, nullable=True)
    deviceID = Column(Text)
    firebaseInstallationID = Column(Text)
    emergencyContact = Column(ARRAY(JSON))
    password = Column(Text)
    lastLogin = Column(DateTime(timezone=True), server_default=func.now(), index=True)
