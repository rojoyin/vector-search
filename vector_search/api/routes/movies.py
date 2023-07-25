from typing import List

from fastapi import APIRouter, Query

from vector_search.api.routes.commons import handle_similar_search
from vector_search.models.domain.movie import Movie
from vector_search.models.schemas.movies_response import MovieResponse

movies_router = APIRouter()


@movies_router.post('/find_similar')
def find_similar_users(data: Movie, num_neighbors: int = Query(default=10, gt=0)) -> List[MovieResponse]:
    return handle_similar_search(data.model_dump(), type(data).get_table_name(), num_neighbors)
