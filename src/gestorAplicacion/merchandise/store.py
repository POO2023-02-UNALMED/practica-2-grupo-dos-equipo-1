from entity import Entity


class Store(Entity):

    def __init__(self, name, description, address):
        super(name)
        self._description = description
        self._address = address
        self._products = []
        self._balance = 0

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def getProducts(self):
        return self._products

    def addProduct(self, product):
        self._products.append(product)

    def getBalance(self):
        return self._balance

    def setBalance(self, balance):
        self._balance = balance
