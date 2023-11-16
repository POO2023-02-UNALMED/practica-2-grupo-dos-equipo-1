from entity import Entity
from transactions.order import Order
from delivery import Delivery
from merchandise.store import Store
from transactions.retval import Retval
from merchandise.product import Product


class Admin(Entity):

    def __init__(self, name, address, store):
        super().__init__(name, address)
        self._store = store

    def getStore(self):
        return self._store

    def setStore(self, store):
        self._store = store

    # Las funciones que siguen son como para tener una idea de lo que podrá hacer el admin
    def makeOrder(self):  # Crea un objeto Order
        order = Order()
        return order

    def newDelivery(name):  # Crea un nuevo Delivery
        return Delivery(name)

    def assignOrder(order, delivery):  # Le asigna a un delivery una orden creada
        delivery.addOrder(order)

    # Metodos definidos para la clase user (Ahora admin)
    # Sin password

    def createProduct(self, store, name, price, description, quantity, tag):
        return store.createProduct(name, price, description, quantity, tag, self)

    def createStore(self, name, description, tag):
        newStore = Store.create(name, description, tag)
        if newStore is None:
            return Retval("Failed to create store, name already in use", False)

        return self.addStore(newStore)

    def addStore(self, store):
        return self.addStoreByName(store.getName())

    def addStoreByName(self, name):
        existingStore = Store.validate(name)
        if existingStore is None:
            return Retval("Error: the store does not exist", False)

        retval = existingStore.addUser(self.getName())
        if retval.isOk():
            self.stores.append(existingStore)

        return retval

    def addToShoppingCart(self, productName, quantity):
        existingProduct = Product.validate(productName)

        retval = self.shoppingCart.addProduct(existingProduct, quantity)

        return retval

    @staticmethod
    def listProduct(productName, store, doList):
        existingProduct = Product.validate(productName, store.getProducts())
        if existingProduct is None:
            return Retval("Error: there is no such product inside the store", False)

        existingProduct.setListed(doList)

        return Retval("Unlisted product successfully")
