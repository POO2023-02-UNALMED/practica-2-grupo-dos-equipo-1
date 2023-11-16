from gestorAplicacion.entites.entity import Entity
from transactions.retval import Retval
from product import Product


class Store(Entity):
    
    instances = []

    def __init__(self, name, description, address):
        super(name)
        self._description = description
        self._address = address
        self._products = []
        self._balance = 0
        Store.instances.append(self)

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

    def createProduct(self, name, price, description, quantity, tag):
        newProduct = Product.create(name, price, description, quantity, tag)
        if newProduct is None:
            return Retval("Failed to create product. The product already exists inside the store", False)

        self.addProduct(newProduct)

        return Retval("Created product successfully!")
