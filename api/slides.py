from fastapi import APIRouter
from models import Slide
from db import crud

router = APIRouter()

@router.get("/slides/{slide_id}")
def read_slide(slide_id: int):
    return crud.get_slide(slide_id)

@router.post("/slides/{slide_id}")
def create_slide(slide_id: int, slide: Slide):

    return {"slide_name": slide.slide_name, "slide_id": slide_id}

@router.put("/slides/{slide_id}")
def update_slide(slide_id: int, slide: Slide):

    return {"slide_name": slide.slide_name, "slide_id": slide_id}