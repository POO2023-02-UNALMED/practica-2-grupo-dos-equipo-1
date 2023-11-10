import pickle
from gestorAplicacion.entites.person import person


class Serializer:
    @staticmethod
    def serialize(obj, filename):
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)


if __name__ == "__main__":
    superUsuario = Admin("Jaime", [10, 20], )

    # creacion del archivo pickle
    # Serializacion de los objetos creatos
    Serializer.serialize(superUsuario, "wb")
