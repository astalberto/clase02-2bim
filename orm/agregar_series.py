import csv

from sqlalchemy.orm import sessionmaker

from modelo import engine, Plataforma, Pais, Serie
Session = sessionmaker(bind=engine)
session = Session()

pais_map = {p.nombre: p for p in session.query(Pais).all()}
plataforma_map = {p.nombre: p for p in session.query(Plataforma).all()}

with open("../data/series.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        serie =Serie(
            id=int(row["id"]), 
            titulo=row["titulo"],
            genero=row["genero"],
            anio_estreno=row["anio_estreno"],
            temporadas=row["temporadas"],
            plataforma=plataforma_map.get(row["plataforma"]),
            pais = pais_map.get(row["pais"]), ## Metodo para que si no retorna un pais registrado devuelva none
        )
        session.add(serie)
session.commit()
