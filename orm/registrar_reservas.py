from datetime import date
from conexion import Session
from modelo import Sala, Reserva


def registrar_reserva(estudiante, sala_id, fecha):
    
    if not isinstance(estudiante, str) or not estudiante.strip():
        raise ValueError("Debes ingresar el nombre del estudiante")
    if type(sala_id) is not int or sala_id <= 0:
        raise ValueError("El ID de la sala debe ser un entero positivo")
    if type(fecha) is not date:
        raise ValueError("La fecha debe ser un objeto date")
    estudiante = estudiante.strip()

    with Session.begin() as session:
        sala = session.get(Sala, sala_id)
        if sala is None:
            raise ValueError("La sala no existe")
        if not sala.disponible:
            raise ValueError("La sala no está disponible")
        
        reserva = Reserva(
            estudiante=estudiante,
            sala_id=sala_id,
            fecha=fecha,
        )
        session.add(reserva)
        sala.disponible = False

    return reserva