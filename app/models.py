from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    short_id = Column(String(10), unique=True, index=True, nullable=False)
    original_url = Column(String(2048), nullable=False)
    clicks = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
