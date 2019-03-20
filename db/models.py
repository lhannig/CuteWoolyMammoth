from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship


Base = declarative_base()

yarn_materials_table = Table('association', Base.metadata,
                            Column('yarn_id', Integer, ForeignKey('yarns.id')),
                            Column('material_id', Integer, ForeignKey('materials.id'))
                            )

yarn_shops_table = Table('yarn_shop_association', Base.metadata,
                         Column('yarn_id', Integer, ForeignKey('yarns.id')),
                         Column('yarnshop_id', Integer, ForeignKey('yarnshops.id')))

yarn_swatch_table = Table('yarn_swatch_association', Base.metadata,
                          Column('yarn_id', Integer, ForeignKey('yarns.id')),
                          Column('swatch_id', Integer, ForeignKey('swatches.id')))

yarns_projectideas_table = Table('yarns_projectideas_association', Base.metadata,
                                Column('yarn.id', Integer, ForeignKey('yarns.id')),
                                Column('projectideas.id', Integer, ForeignKey('projectideas.id'))
                                )

colors_projectideas_table = Table('colorways_projectideas_association', Base.metadata,
                                 Column('colorway_id', Integer, ForeignKey('colorways.id')),
                                 Column('projectidea_id', Integer, ForeignKey('projectideas.id')))

colorway_work_table = Table('colorway_work_association', Base.metadata,
                            Column('colorway_id', Integer, ForeignKey('colorways.id')),
                            Column('work_in_progress_id', Integer, ForeignKey('work_in_progress.id')))


work_needlesize_table = Table('work_needlesize_association', Base.metadata,
                              Column('work_in_progress_id', Integer, ForeignKey('work_in_progress.id')),
                              Column('needlesize_id', Integer, ForeignKey('needlesizes.id'))
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

    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'))
    manufacturer = relationship('Manufacturer', back_populates='yarns_manufacturers')
    wash_id = Column(Integer, ForeignKey('washs.id'))
    wash = relationship('Wash', back_populates='yarns_wash')
    weight_id = Column(Integer, ForeignKey('weights.id'))
    weight = relationship('Weight', back_populates='yarns_weight')
    colorways = relationship('Colorway', backref='yarns')

    materials = relationship('Material', secondary=yarn_materials_table, back_populates='yarn_materials')
    yarnshops = relationship('Yarnshop', secondary=yarn_shops_table, back_populates='yarn_yarnshops')
    yarn_swatches = relationship('Swatch', secondary=yarn_swatch_table, back_populates='yarns_swatch')
    yarn_projectideas = relationship('Projectidea', secondary=yarns_projectideas_table, back_populates='yarns_projectidea')


class Manufacturer(Base):
    __tablename__ = 'manufacturers'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    yarns_manufacturers = relationship('Yarn', back_populates='manufacturer')


    def __repr__(self):
        return "<Yarn (name='%s' )> % (self.name)"

class Wash(Base):
    __tablename__ = 'washs'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    yarns_wash = relationship('Yarn', back_populates='wash')


class Weight(Base):
    __tablename__ = 'weights'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True, nullable=False)
    yarns_weight = relationship('Yarn', back_populates='weight')
    weight_projectideas = relationship('Projectidea', back_populates='weights_projectideas')


class Material(Base):
    __tablename__ = 'materials'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    notes = Column(String(100))
    yarn_materials = relationship('Yarn', secondary=yarn_materials_table, back_populates='materials')


class Colorway(Base):
    __tablename__ = 'colorways'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    nr = Column(Integer, unique=True)
    in_stash = Column(Boolean, default=False)
    quantity = Column(Integer, default=0)
    notes = Column(String(100))
    yarn_id = Column(Integer, ForeignKey('yarns.id', ondelete='CASCADE', onupdate='CASCADE'))

    color_projectideas = relationship('Projectidea', secondary=colors_projectideas_table, back_populates='colors_projectidea')
    work_colors = relationship('WorkInProgress', secondary=colorway_work_table, back_populates='colors_work')


class Yarnshop(Base):
    __tablename__ = 'yarnshops'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    purchased_at = Column(Boolean, default=False)
    notes = Column(String(100))

    yarn_yarnshops = relationship('Yarn', secondary=yarn_shops_table, back_populates='yarnshops')


class Needlesize(Base):
    __tablename__ = 'needlesizes'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True, nullable=False)

    swatches = relationship('Swatch', back_populates='needlesizes')
    needlesize_works = relationship('WorkInProgress', back_populates='work_needlesizes')

class Swatch(Base):
    __tablename__ = 'swatches'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    n_rows = Column(Integer)
    n_stitches = Column(Integer)
    n_rows_washed = Column(Integer)
    n_stiches_washed = Column(Integer)
    notes = Column(String(100))

    needlesize_id = Column(Integer, ForeignKey('needlesizes.id'))
    needlesizes = relationship('Needlesize', back_populates='swatches')
    yarns_swatch = relationship('Yarn', secondary='yarn_swatch_table', back_populates='yarn_swatches')



class Projectidea(Base):
    __tablename__ = 'projectideas'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    link = Column(String)
    notes = Column(String(200))
    yardage_needed = Column(Integer, nullable=True)
    skeins_needed = Column(Integer, nullable=True)

    weight_id = Column(Integer, ForeignKey('weights.id'))
    weights_projectdeas = relationship('Weight', back_populates='weight_projectideas')
    works_in_progress = relationship('WorkInProgress', back_populates='projectidea_work')

    yarns_objectidea = relationship('Yarn', secondary=yarns_projectideas_table, back_populates='yarn_projectideas')
    colors_objectidea = relationship('Colorway', secondary=colors_projectideas_table, back_populates='color_oprojectideas')


class WorkInProgress(Base):
    __tablename__ = 'work_in_progress'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    stichnr = Column(Integer)
    notes = Column(String(200))

    projectidea_id = Column(Integer, ForeignKey('projectideas.id'))
    projectidea_work = relationship('Projectidea', back_populates='works_in_progress')

    colors_work = relationship('Colorway', secondary=colorway_work_table, back_populates='work_colors')
    work_needlesizes = relationship('Needlesize', secondary=work_needlesize_table, back_populates='needlesize_works')

    work_finished_objects = relationship('FinishedObject', back_populates='finished_objects_works')

class FinishedObject(Base):
    __tablename__ = 'finished_object'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    recipient = Column(String(50))
    work_in_progress_id = Column(Integer, ForeignKey('work_in_progress.id'))
    finished_objects_works = relationship('WorkInProgress', back_populates='work_finished_objects')

