from typing import Tuple
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.entites.entity import Entity


class Store(Entity):

   instances = []

   def __init__(self, name: str, address: Tuple[int, int], tag: Tags,
                description: str):

      super().__init__(name, address)

      self._description = description
      self._tag = tag
      self._balance = 0
      # self._products: list[Product] = []

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

      return Store(name, address, tag, description)

   def get_description(self):
      return self._description

   def set_description(self, description):
      self._description = description

   def get_balance(self) -> int:
      return self._balance

   def set_balance(self, balance: int) -> None:
      self._balance = balance

   # def get_products(self):
   #    return self._products
   #
   # def add_product(self, product) -> None:
   #    self._products.append(product)

   # def createProduct(self, name, price, description, quantity, tag):
   #    newProduct = Product.create(name, price, description, quantity, tag)
   #    if newProduct is None:
   #       return Retval(
   #           "Failed to create product. The product already exists inside the store",
   #           False)
   #
   #    self.add_product(newProduct)
   #
   #    return Retval("Created product successfully!")
