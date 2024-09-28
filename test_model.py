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


t_person = Table(
    'person', metadata,
    Column('id', Integer),
    Column('name', Text, nullable=False),
    Column('size', Float)
)
