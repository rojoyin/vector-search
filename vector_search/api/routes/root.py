from fastapi import APIRouter

root_router = APIRouter()


@root_router.get("/")
def get_root():
    return {"hello": "world"}
