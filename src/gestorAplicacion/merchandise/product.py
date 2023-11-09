class Product:

    instances = []

    def __init__(self, name=None, price=None, description=None, quantity=None, tags=None):
        self._name = name
        self._price = price
        self._description = description
        self._quantity = quantity
        if tags is None:
            tags = []
        self._tags = tags
        self._listed = True
        Product.instances.append(self)

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getPrice(self):
        return self._price

    def setPrice(self, price):
        self._price = price

    def getDescription(self):
        return self._description

    def setDescription(self, description):
        self._description = description

    def getQuantity(self):
        return self._quantity

    def setQuantity(self, quantity):
        self._quantity = quantity

    def getTags(self):
        return self._tags

    def setTags(self, tags):
        self._tags = tags

    @staticmethod
    def create(name, price, description, quantity, tag, productHolder):
        return Product(name, price, description, quantity, tag, productHolder)
