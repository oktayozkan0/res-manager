from pydantic import BaseModel


class TestCreateSchema(BaseModel):
    test_col: str

class TestUpdateSchema(BaseModel):
    id: int
    new_col: str
