import pickle
from ecart.gestorAplicacion.merchandise.store import Store
import os


class StoreSerializer:
    file = "Store"

    @staticmethod
    def serialize(store):
        if os.path.exists(StoreSerializer.file):
            # El archivo ya existe, cargar datos actuales
            with open(StoreSerializer.file, "rb") as existing_file:
                existing_data = pickle.load(existing_file)
            store.update(existing_data)

        # Guardar datos actualizados
        with open(StoreSerializer.file, "wb") as picklefile:
            pickle.dump(store, picklefile)

    @staticmethod
    def deserialize():
        if os.path.exists(StoreSerializer.file):
            with open(StoreSerializer.file, "rb") as picklefile:
                Store.instances = pickle.load(picklefile)
                print(type(Store.instances))
        else:
            print("El archivo no existe.")


"""
 file = "src/store.pkl"


class StoreSerializer:
    @staticmethod
    def serialize(store):
        picklefile = open(file, "wb")
        pickle.dump(store, picklefile)
        picklefile.close()

    @staticmethod
    def deserialize():
        picklefile = open(file, "rb")

        Store.instances = pickle.load(picklefile)

        picklefile.close()

        print(type(Store.instances))
"""
