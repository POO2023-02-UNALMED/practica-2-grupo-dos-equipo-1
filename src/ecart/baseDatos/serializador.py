import pickle
from ecart.gestorAplicacion.merchandise.store import Store

file = "store.pkl"
class StoreSerializer:
    @staticmethod
    def serialize(store):
        picklefile = open(file, "wb")
        pickle.dump(store, picklefile)
        picklefile.close()


    @staticmethod
    def deserialize():
        picklefile = open("store.pkl", "rb")

        Store.instances = pickle.load(picklefile)

        picklefile.close()

        print(type(Store.instances))