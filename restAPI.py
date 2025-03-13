from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class slide(BaseModel):
    slide_id: int
    slide_name: int
    file_location: str
    must_follow: int | None
    must_precede: int | None
    must_avoid: str | None






@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/slides/{slide_id}")
def update_slide(slide_id: in):
