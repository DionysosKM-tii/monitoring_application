from sqlalchemy.orm import declarative_base

Base = declarative_base()

from backend.data.models.area_of_interest_model import AreaOfInterestModel
from backend.data.models.uploaded_photo_model import UploadedPhotoModel
from backend.data.models.measurements_model import MeasurementsModel