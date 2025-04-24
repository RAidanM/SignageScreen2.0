from pydantic import BaseModel

class Slide(BaseModel):
    slide_id: int
    slide_name: str
    file_location: str
    must_follow: int | None = None
    must_precede: int | None = None
    must_avoid: int | None = None

class Schedule(BaseModel):
    schedule_id: int
    slide_id: int
    start_date: str
    end_date: str | None
    day: int | None