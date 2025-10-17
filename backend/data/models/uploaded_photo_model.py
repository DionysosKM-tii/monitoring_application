from sqlalchemy import Column, Integer, String, ForeignKey, Date

from backend.data.models import Base

class UploadedPhotoModel(Base):
    __tablename__ = "uploaded_photos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    area_id = Column(Integer, ForeignKey("areas_of_interest.id", ondelete="CASCADE"), nullable=False)
    photo_full_path = Column(String, nullable=False)
    photo_date = Column(Date, nullable=False)

