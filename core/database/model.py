from sqlalchemy import String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ApiKey(Base):
    __tablename__ = "apiKeys"
    uuid = Column(String, primary_key=True, index=True)
    apiKey = Column(String, index=True)
    level = Column(Integer)
    created_at = Column(Integer)

    
