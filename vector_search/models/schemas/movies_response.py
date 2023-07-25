from vector_search.models.domain.custom_base import CustomBase


class MovieResponse(CustomBase):
    movie_id: int
    movie_title: str
