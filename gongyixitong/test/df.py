from sqlalchemy import *
from sqlalchemy.orm import *
from astropy.utils import metadata

db = "sqlite:///./sqlite.db"

engine = create_engine(db, echo=True)
metadata = MetaData(engine)

users = Table('t-users', metadata,
              Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
              Column('name', String(50)),
              Column('password', String(12))
              )

metadata.drop_all(engine)
metadata.create_all(engine)
