from entity import Entity


class Delivery(Entity):
    instances = []

    def __init__(self, username=None):
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

    def planRoute():  # Aquí va la lógica de cuál lleva primero y tales
        sequence = []  # Las ordenes en el órden optimo o luego miramos
        return sequence
