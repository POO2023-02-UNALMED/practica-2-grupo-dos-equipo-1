

class Product:

    instances = []

    def __init__(self, name, price, description, quantity, tag, productHolder):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity
        self.tag = tag
        self.listed = True
        self.productHolder = productHolder
        self.productTags = []
        Product.instances.append(self)

    @staticmethod
    def create(name, price, description, quantity, tag, productHolder):
        return Product(name, price, description, quantity, tag, productHolder)
