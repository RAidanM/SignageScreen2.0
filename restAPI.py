from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Slide(BaseModel):
    slide_id: int
    slide_name: str
    file_location: str
    must_follow: int | None
    must_precede: int | None
    must_avoid: int | None

class Schedule(BaseModel):
    schedule_id: int
    slide_id: int
    start_date: str
    end_date: str | None
    day: int | None

#slides
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/slides/{slide_id}")
def read_slide(slide_id: int, q: str | None = None):
    return {"slide_id": slide_id, "q": q}

@app.post("/slides/{slide_id}")
def create_slide(slide_id: int, slide: Slide):
    return {"slide_name": slide.slide_name, "slide_id": slide_id}

@app.put("/slides/{slide_id}")
def update_slide():
    return {"slide_name": slide.slide_name, "slide_id": slide_id}
#schedule

