class User(Person, Serializable):
    instances = []

    def __init__(self, username=None, password=None, address=None):
        super().__init__(username, password, address)
        self.shoppingCart = ShoppingCart()
        self.stores = []
        self.orders = []
        User.instances.append(self)