from conexion import engine
from modelo import Base

def crear_tabla():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    crear_tabla()