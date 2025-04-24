from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/test/{test_id}")
def read_test(test_id: int, q: str | None):
    return {"test_id":test_id, "q":q}
