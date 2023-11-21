import pickle
from ecart.gestorAplicacion.merchandise.store import Store

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
