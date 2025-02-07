import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ApiKey(Base):
    __tablename__ = "apiKeys"
    uuid = Column(UUID, primary_key=True, default=uuid.uuid4, index=True)
    apiKey = Column(String, unique=True, nullable=False, index=True)
    level = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)