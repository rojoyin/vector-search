from pydantic import BaseModel


class CustomBase(BaseModel):
    @classmethod
    def get_table_name(cls) -> str:
        return cls.__name__.lower()

    @classmethod
    def get_annoy_index_name(cls) -> str:
        return cls.__name__.lower()

    class Config:
        use_enum_values = True
