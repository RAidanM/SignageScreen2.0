from pydantic import BaseModel

class Schedule(BaseModel):
    schedule_id: int
    slide_id: int
    start_date: str
    end_date: str | None
    day: int | None