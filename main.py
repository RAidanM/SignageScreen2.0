from fastapi import FastAPI
from pydantic import BaseModel
from api import test,slides


app = FastAPI()

app.include_router(test.router)
app.include_router(slides.router)