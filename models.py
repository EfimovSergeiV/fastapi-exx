from sqlalchemy import Column, Integer, String, UUID
from database import Base
import uuid


class Item(Base):
    __tablename__ = "items"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)