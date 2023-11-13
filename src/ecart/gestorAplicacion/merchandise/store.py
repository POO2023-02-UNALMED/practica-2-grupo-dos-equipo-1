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

    def addUser(self, user):
        return self.addUserByName(user.getName())

    def addUserByName(self, name):
        newUser = User.validate(name, self.members)
        if newUser is not None:
            return Retval("Failed to join store. User is already a member of the store", False)

        self.members.append(newUser)

        return Retval("Joined store successfully")

    def createProduct(self, name, price, description, quantity, tag, productHolder):
        newProduct = Product.create(name, price, description, quantity, tag, productHolder, self.getProducts())
        if newProduct is None:
            return Retval("Failed to create product. The product already exists inside the store", False)

        self.products.append(newProduct)

        return Retval("Created product successfully!")
