import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operation(Base):
    __tablename__ = 'operations'

    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Date)
    name = sa.Column(sa.String)
