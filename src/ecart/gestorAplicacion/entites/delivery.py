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

      workplace.add_delivery(self)

   @classmethod
   def find(cls, name: str, arr):
      for delivery in arr:
         if delivery.get_name() == name:
            return delivery

      return None

   @classmethod
   def create(cls, name: str, address: Tuple[int, int], workplace: Store,
              arr: list):

      if cls.find(name, arr) is not None:
         return None

      return cls(name, address, workplace)

   def update_settings(self, name: str, address: Tuple[int, int]) -> str:

      for delivery in self._workspace.get_deliveries():
         if delivery.get_name() == name and delivery != self:
            raise errors.ErrorSystemOperation(
                f"Ese nombre ya esta en uso por otro delivery")

      self.set_name(name)
      self.set_address(address)

      return "Se actualizó la configuración del delivery correctamente"

   def deliver(self, order: Order):

      nodes = [
          self.get_address(),
          order.get_origin_address(),
          order.getDestinationAddress()
      ]

      total_distance = 0
      for i in range(len(nodes) - 1):
         x1, y1 = nodes[i]
         x2, y2 = nodes[i + 1]
         distance = abs(x2 - x1) + abs(y2 - y1)
         total_distance += distance

      standard_rate = 7  # $7/8 Km
      travel_cost = (total_distance // 8) * standard_rate

      total_cost = travel_cost

      origin_store: Store | None = None
      for store in Store.get_instances():
         if store.get_address() == order.get_origin_address():
            origin_store = store
            break

      destination_place: Store | None = None
      for store in Store.get_instances():
         if store.get_address() == order.getDestinationAddress():
            destination_place = store
            break

      if origin_store:
         for product_name, quantity in order.getProducts().items():
            product = origin_store.get_product_by_name(product_name)
            if product:
               total_cost += product.get_price() * quantity
               product.increase_quantity(-quantity)

               if destination_place:
                  arrival_product = destination_place.get_product_by_name(
                      product_name)
                  if arrival_product:
                     arrival_product.increase_quantity(quantity)
                  else:
                     destination_place.create_product(
                         product_name, product.get_price(),
                         quantity, product.get_description())

      order.setDelivered(True)

      return f"Se ejecuto con exito la entrega.\n\nRecorrido: {total_distance} Km\nCosto del Trayecto: ${travel_cost} USD\nCosto total: ${total_cost} USD"
