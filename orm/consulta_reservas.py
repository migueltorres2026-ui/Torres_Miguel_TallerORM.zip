from sqlalchemy import select
from sqlalchemy.orm import joinedload
from conexion import Session
from modelo import Reserva

def consultar_reservas():
    with Session() as session:
        consulta = (select(Reserva).options(joinedload(Reserva.sala)).order_by(Reserva.id))
        reservas = session.scalars(consulta).all()

    return reservas