from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class Yarn(Base):
    __tablename__ = 'yarns'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    superwash = Column(Boolean)
    yardage = Column(Integer)
    notes = Column(String(200))
    length = Column(Integer)
    skeinweight = Column(Integer)

    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    id = Column(Integer,primary_key=True)
    name = Column(String(50), unique=True)

    yarns = relationship('Yarn')


    def __repr__(self):
        return "<Yarn (name='%s' )> % (self.name)"

