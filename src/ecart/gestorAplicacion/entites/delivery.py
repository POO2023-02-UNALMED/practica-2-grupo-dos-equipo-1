from ecart.gestorAplicacion.transactions.order import Order
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.entites.entity import Entity
from .entity import Entity
from typing import Tuple


class Delivery(Entity):
   instances = []

   def __init__(self, name: str, address: Tuple[int, int], workplace: Store):

      super().__init__(name, address)
      self._workspace = workplace
      self._orders: list[Order] = []

      Delivery.instances.append(self)

   @classmethod
   def get(cls):
      return cls.instances

   @classmethod
   def find(cls, name: str):
      for delivery in cls.instances:
         if delivery.get_name() == name:
            return delivery

      return None

   @classmethod
   def create(cls, name: str, address: Tuple[int, int], workplace: Store):

      if cls.find(name) is not None:
         return None

      return cls(name, address, workplace)
