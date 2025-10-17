from datetime import date

from fastapi import UploadFile, Form, File


class AddPhotoRequest:
    area_id: int
    photo_date: date
    photo: UploadFile

    def __init__(
            self,
            area_id: int = Form(...),
            photo_date: date = Form(...),
            photo: UploadFile = File(...)
    ):
        self.area_id = area_id
        self.photo_date = photo_date
        self.photo = photo
