from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy.sql import func

@as_declarative()
class Base:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    __name__: str
    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
