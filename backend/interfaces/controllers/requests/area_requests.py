from pydantic import BaseModel


class CreateAreaRequest(BaseModel):
    geometry: dict
    name: str
