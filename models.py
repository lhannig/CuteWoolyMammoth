from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship


Base = declarative_base()

yarn_materials_table = Table('association', Base.metadata,
                            Column('yarn_id', Integer, ForeignKey('yarns.id')),
                            Column('material_id', Integer, ForeignKey('materials.id'))
                            )

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
    manufacturer = relationship('Manufacturer', back_populates='yarns_manufacturers')
    wash_id = Column(Integer, ForeignKey('washs'))
    wash = relationship('Wash', back_populates='yarns_wash')
    weight_id = Column(Integer, ForeignKey('weight.id'))
    weight = relationship('Weight', back_populates='yarns_weight')
    materials = relationship('Material', secondary=yarn_materials_table, back_populates='yarn_materials')
    colorways = relationship('Colorway', backref='yarns')




class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    yarns_manufacturers = relationship('Yarn', back_populates='manufacturer')


    def __repr__(self):
        return "<Yarn (name='%s' )> % (self.name)"

class Wash(Base):
    __tablename__= 'washs'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    yarns_wash = relationship('Yarn', back_populates='wash')


class Weight(Base):
    __tablename__= 'weights'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True, nullable=False)
    yarns_weight = relationship('Yarn', back_populates='weight')


class Material(Base):
    __tablename__='materials'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    notes = Column(String(100))
    yarn_materials = relationship('Yarn', secondary=yarn_materials_table, back_populates='materials')


class Colorway(Base):
    __tablename__='colorways'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    nr = Column(Integer, unique=True)
    in_stash = Column(Boolean, default=False)
    quantity = Column(Integer, default=0)
    notes = Column(String(100))
    yarn_id = Column(Integer, ForeignKey('yarn.id', ondelete='CASCADE', onupdate='CASCADE'))
