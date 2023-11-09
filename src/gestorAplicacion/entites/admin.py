from entity import Entity
from order import Order
from delivery import Delivery


class Admin(Entity):

    def __init__(self, username=None, store=None):
        super(username)
        self._store = store

    def getStore(self):
        return self._store

    def setStore(self, store):
        self._store = store

    # Las funciones que siguen son como para tener una idea de lo que podrá hacer el admin
    def makeOrder():  # Crea un objeto Order
        order = Order()
        return order

    def newDelivery(name):  # Crea un nuevo Delivery
        return Delivery(name)

    def assignOrder(order, delivery):  # Le asigna a un delivery una orden creada
        delivery.addOrder(order)
