from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_root():
    return {"hello": "world"}
