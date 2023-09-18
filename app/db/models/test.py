from sqlalchemy import Column, String
from app.db.models.base import Base


class Test(Base):
    test_col = Column(String)
