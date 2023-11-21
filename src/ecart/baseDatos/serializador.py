import pickle
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.uiMain.utils import Utils
import os


class StoreSerializer:
   file = Utils.get_file("stores.pkl")

   @staticmethod
   def _assert_existance():
      if not os.path.exists(StoreSerializer.file):
         with open(StoreSerializer.file, 'w'):
            pass

   @staticmethod
   def serialize():

      StoreSerializer._assert_existance()

      with open(StoreSerializer.file, "wb") as picklefile:
         pickle.dump(Store.instances, picklefile)

   @staticmethod
   def deserialize():

      StoreSerializer._assert_existance()

      try:
         with open(StoreSerializer.file, "rb") as picklefile:
            Store.instances = pickle.load(picklefile)
      except EOFError:
         pass
