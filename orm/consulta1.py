"""
Titulo - Promedio de edad 
"""
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from modelo import Actor, Serie
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

series = session.query( Serie.titulo,func.avg(Actor.edad).label("promedio_edad")).join(Actor).group_by(Serie).order_by(Serie.titulo).all()

for s in series:
    print("Titulo : %s - Promedio Edad: %s" % (s.titulo, s.promedio_edad))
