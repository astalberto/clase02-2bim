import csv

from sqlalchemy.orm import sessionmaker

from modelo import engine, Premio, Serie
Session = sessionmaker(bind=engine)
session = Session()

serie_map = {p.titulo: p for p in session.query(Serie).all()}

with open("../data/premios.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        premio =Premio(
            id=int(row["id"]), 
            nombre_premio=row["nombre_premio"],
            categoria=row["categoria"],
            anio=row["anio"],
            serie=serie_map.get(row["serie"]),
        )
        session.add(premio)
session.commit()
