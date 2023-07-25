from vector_search.models.domain.custom_base import CustomBase


class Movie(CustomBase):
    movie_id: int
    movie_title: str
    release_date: str
    video_release_date: str
    IMDb_URL: str
    unknown: bool
    Action: bool
    Adventure: bool
    Animation: bool
    Childrens: bool
    Comedy: bool
    Crime: bool
    Documentary: bool
    Drama: bool
    Fantasy: bool
    FilmNoir: bool
    Horror: bool
    Musical: bool
    Mystery: bool
    Romance: bool
    SciFi: bool
    Thriller: bool
    War: bool
    Western: bool
