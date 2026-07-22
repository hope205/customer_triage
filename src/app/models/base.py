from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# # Base class for models
Base = declarative_base()