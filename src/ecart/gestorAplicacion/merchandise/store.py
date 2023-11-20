from typing import Tuple
import pickle
from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.merchandise.product import Product
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.entites.entity import Entity


def deserializar():
   # Deserializar la lista de instancias desde el archivo
   with open('archivo_serializado.pkl', 'rb') as archivo:
      lista_deserializada = pickle.load(archivo)
   return lista_deserializada


class Store(Entity):
   instances = []

   def __init__(self, name: str, address: Tuple[int, int], tag: Tags,
                description: str):

      super().__init__(name, address)

      self._description = description
      self._tag = tag
      self._balance = 0

      from ecart.gestorAplicacion.entites.delivery import Delivery
      self._deliveries: list[Delivery] = []
      self._products: list[Product] = []

      Store.instances.append(self)

   @classmethod
   def get(cls) -> list:
      return cls.instances

   @classmethod
   def find(cls, name: str):
      for store in cls.instances:
         if store.get_name() == name:
            return store

      return None

   @classmethod
   def create(cls, name: str, address: Tuple[int, int], tag: Tags,
              description: str):

      if cls.find(name) is not None:
         return None

      return cls(name, address, tag, description)

   def get_products(self) -> list[Product]:
      return self._products

   def create_product(self, name: str, price: float, quantity: int, description: str):
      p = Product(name, price, quantity, description)
      self._products.append(p)

   def get_deliveries(self) -> list:
      return self._deliveries

   def set_deliveries(self, deliveries) -> None:
      self._deliveries = deliveries

   def update_settings(self, name, address, tag, description) -> str:

      if not self.is_address_available(address):
         raise errors.ErrorSystemOperation(
             f"La direccion {address} ya está en uso. Recuerda que ninguno puede pasarse de 100"
         )

      self.set_name(name)
      self.set_address(address)
      self.set_tag(tag)
      self.set_description(description)

      return "Se actualizó la configuración de la tienda correctamente"

   def add_delivery(self, delivery):
      self._deliveries.append(delivery)

   def serializar(self):
      # Serializar la lista de instancias
      with open('archivo_serializado.pkl', 'wb') as archivo:
         pickle.dump(self, archivo)

   def set_tag(self, tag: Tags) -> None:
      self._tag = tag

   def get_description(self):
      return self._description

   def set_description(self, description):
      self._description = description

   def get_balance(self) -> int:
      return self._balance

   def set_balance(self, balance: int) -> None:
      self._balance = balance
