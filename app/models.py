from pydantic import BaseModel
from typing import Optional, Dict
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import Integer
from sqlalchemy import JSON

from app.database import Base


class EventTable(Base):
    __tablename__ = "events"

    event_id = Column(String, primary_key=True)

    store_id = Column(String)

    camera_id = Column(String)

    visitor_id = Column(String)

    event_type = Column(String)

    timestamp = Column(String)

    zone_id = Column(String, nullable=True)

    dwell_ms = Column(Integer)

    is_staff = Column(Boolean)

    confidence = Column(Float)

    metadata_json = Column(JSON)


class EventSchema(BaseModel):
    event_id: str

    store_id: str

    camera_id: str

    visitor_id: str

    event_type: str

    timestamp: str

    zone_id: Optional[str] = None

    dwell_ms: int = 0

    is_staff: bool = False

    confidence: float

    metadata: Dict = {}