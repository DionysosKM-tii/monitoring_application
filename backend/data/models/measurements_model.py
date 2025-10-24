from sqlalchemy import Column, Integer, ForeignKey, Date, Float, String

from backend.data.models import Base


class MeasurementsModel(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    area_id = Column(Integer, ForeignKey("areas_of_interest.id", ondelete="CASCADE"), nullable=False)
    timestamp = Column(Date, nullable=False)
    type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
