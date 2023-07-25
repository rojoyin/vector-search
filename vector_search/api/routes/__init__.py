from fastapi import APIRouter

from vector_search.api.routes.root import router as root_router


router = APIRouter()
router.include_router(root.router, tags=["root"], prefix="")
