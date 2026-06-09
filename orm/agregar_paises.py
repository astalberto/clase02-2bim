import csv

from sqlalchemy.orm import sessionmaker

from modelo import engine, Pais
Session = sessionmaker(bind=engine)
session = Session()

with open("../data/paises.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pais =Pais(
            id=int(row["id"]), 
            nombre=row["nombre"],
            continente=row["continente"])
        session.add(pais)
session.commit()