class Entity:
    addresses = []

    #    def __init__(self, name):
    #       self._name = name

    def __init__(self, name, address):
        self.name = name
        self.address = address

        if not self.isAddressAvailable(address):
            raise ValueError("Address is not available")

        self.addresses.append(address)

    # En este caso solo se verifica que la direccion esté entre un valor de 0 - 100

    def isAddressAvailable(self):
        if not (0 <= self[0] <= 100):
            return False

        if not (0 <= self[1] <= 100):
            return False

        return True

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name
