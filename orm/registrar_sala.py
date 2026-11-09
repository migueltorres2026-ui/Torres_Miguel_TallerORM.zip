from conexion import Session
from modelo import Sala


def insertar_salas(nombre, capacidad):
    nombre = nombre.strip()

    if not nombre or len(nombre) > 100:
        raise ValueError("maximo 100 caracteres")

    if type(capacidad) is not int or capacidad <= 0:
        raise ValueError("capacidad menor o igual a cero")

    with Session.begin() as session:
        sala = Sala(
            nombre=nombre,
            capacidad=capacidad,
            disponible=True,
        )

        session.add(sala)

    return sala