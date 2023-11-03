class Store(Entity, Serializable):
    storeAddress = None
    instances = []

    def __init__(self, name, password, description, tag):
        super().__init__(name, password)
        self.description = description
        self.tag = tag
        self.members = []
        self.products = []
        Store.instances.append(self)