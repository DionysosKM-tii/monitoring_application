from fastapi import FastAPI

from backend.interfaces.controllers.areas_controller import router as areas

app = FastAPI()

app.include_router(areas, prefix="/areas", tags=["areas"])
