from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.transactions.order import Order
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.entites.entity import Entity
from .entity import Entity
from typing import Tuple


class Delivery(Entity):

   def __init__(self, name: str, address: Tuple[int, int], workplace: Store):

      super().__init__(name, address)
      self._workspace = workplace
      self._orders: list[Order] = []

      workplace.add_delivery(self)

   @classmethod
   def find(cls, name: str, arr):
      for delivery in arr:
         if delivery.get_name() == name:
            return delivery

      return None

   @classmethod
   def create(cls, name: str, address: Tuple[int, int], workplace: Store, arr: list):

      if cls.find(name, arr) is not None:
         return None

      return cls(name, address, workplace)

   def plan_route(self):
      pass
