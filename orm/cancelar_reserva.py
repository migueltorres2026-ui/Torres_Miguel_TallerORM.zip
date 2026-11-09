from conexion import Session
from modelo import Reserva


def cancelar_reserva(id_reserva):
    if type(id_reserva) is not int or id_reserva <= 0:
        raise ValueError("El ID debe ser un entero positivo")

    with Session.begin() as session:
        reserva = session.get(Reserva, id_reserva)
        if reserva is None:
            return False

        reserva.sala.disponible = True
        session.delete(reserva)

    return True