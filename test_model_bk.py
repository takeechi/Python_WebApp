from sqlalchemy import Column, Float, Integer, Table, Text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column
from sqlalchemy.orm.base import Mapped

Base = declarative_base()
metadata = Base.metadata


class Human(Base):
    __tablename__ = 'human'

    name = mapped_column(Text, nullable=False)
    id = mapped_column(Integer, primary_key=True)
    height = mapped_column(Float)
    weight = mapped_column(Float)


class Person(Base):
    __tablename__ = 'person'

    name = mapped_column(Text, nullable=False)
    id = mapped_column(Integer, primary_key=True)
    size = mapped_column(Float)


class Dummy():
    pass
