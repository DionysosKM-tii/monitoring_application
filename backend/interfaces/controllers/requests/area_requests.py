from dataclasses import dataclass

from pydantic import BaseModel

dataclass(frozen=True)


class CreateAreaRequest(BaseModel):
    geometry: dict
