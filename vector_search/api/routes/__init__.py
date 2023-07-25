from fastapi import APIRouter

from vector_search.api.routes.root import root_router
from vector_search.api.routes.movies import movies_router


router = APIRouter()
router.include_router(root_router, tags=["root"], prefix="")
router.include_router(movies_router, tags=["movies"], prefix="/movie")
