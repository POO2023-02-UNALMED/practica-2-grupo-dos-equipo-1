from ecart.gestorAplicacion.entites.entity import Entity
from os import error
from typing import Optional, Tuple

from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.merchandise.store import deserializar
from .entity import Entity
import ecart.gestorAplicacion.errors as errors


class Delivery(Entity):
    deliveries = []

    def __init__(self, product_name, store_name, quantity, delivery_address, notes, name: str,
                 address: Tuple[int, int]):
        super().__init__(name, address)
        self.product_name = product_name
        self.store_name = store_name
        self.quantity = quantity
        self.delivery_address = delivery_address
        self.notes = notes

    @classmethod
    def create_delivery(cls, product_name, store_name, quantity, delivery_address, notes):
        delivery = cls(product_name, store_name, quantity, delivery_address, notes)
        cls.deliveries.append(delivery)
        return True, delivery

    @classmethod
    def get_all_deliveries(cls):
        return cls.deliveries

    def get_product_name(self):
        return self.product_name


"""
    instances = []

    def __init__(self, name, username=None):
        super().__init__(name)
        super(username)
        self._orders = []  # Las ordenes que tiene que entregar
        Delivery.instances.append(self)

    def getOrders(self):
        return self._orders

    def addOrder(self, order):
        self._orders.append(order)

    @classmethod
    def getInstances(cls):
        return Delivery.instances

    def planRoute(self):  # Aquí va la lógica de cuál lleva primero y tales
        sequence = []  # Las ordenes en el órden optimo o luego miramos
        return sequence
"""
