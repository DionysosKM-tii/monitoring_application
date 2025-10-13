from dataclasses import dataclass

from pydantic import BaseModel

dataclass(frozen=True)


class GetAreaView(BaseModel):
    geometry: dict
    id: int