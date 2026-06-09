import csv

from sqlalchemy.orm import sessionmaker

from modelo import engine, Plataforma, Pais
Session = sessionmaker(bind=engine)
session = Session()

pais_map = {p.nombre: p for p in session.query(Pais).all()}

with open("../data/plataformas.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        plataforma =Plataforma(
            id=int(row["id"]), 
            nombre=row["nombre"],
            pais = pais_map.get(row["pais"]), ## Metodo para que si no retorna un pais registrado devuelva none
            suscriptores_millones=row["suscriptores_millones"])
        session.add(plataforma)
session.commit()
