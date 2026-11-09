from sqlalchemy import select
from conexion import Session
from modelo import Sala

def consultar_sala():
    with Session() as session:
        consulta = select(Sala).order_by(Sala.id)
        sala = session.scalars(consulta).all()

    return sala