import csv

from sqlalchemy.orm import sessionmaker

from modelo import engine, Actor, Pais, Serie
Session = sessionmaker(bind=engine)
session = Session()

pais_map = {p.nombre: p for p in session.query(Pais).all()}
serie_map = {p.titulo: p for p in session.query(Serie).all()}

with open("../data/actores.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        actor =Actor(
            id=int(row["id"]),
            nombre=row["nombre"],
            edad=row["edad"],
            pais = pais_map.get(row["pais"]), ## Metodo para que si no retorna un pais registrado devuelva non
            serie=serie_map.get(row["serie"]),
        )
        session.add(actor)
session.commit()