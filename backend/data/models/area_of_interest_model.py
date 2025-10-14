from geoalchemy2 import Geometry
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AreaOfInterestModel(Base):
    __tablename__ = "areas_of_interest"

    id = Column(Integer, primary_key=True, autoincrement=True)
    geometry = Column(Geometry(geometry_type="POLYGON", srid=4326))
    name = Column(String, nullable=False)