class Person(Entity):
    addresses = []

    def __init__(self, name, password, address):
        super().__init__(name, password)
        self.address = address
        self.bankAccount = BankAccount(password)
        self.bankAccount.setBalance(100.0)

        if self.isAddressAvailable(address):
            Person.addresses.append(address)

    @staticmethod
    def isAddressAvailable(wantedAddress):
        if wantedAddress[0] < 0 or wantedAddress[0] > 100:
            return False

        if wantedAddress[1] < 0 or wantedAddress[1] > 100:
            return False

        for address in Person.addresses:
            if address[0] == wantedAddress[0] and address[1] == wantedAddress[1]:
                return False
        return True

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    @staticmethod
    def getAddresses():
        return Person.addresses

    @staticmethod
    def setAddresses(addresses):
        Person.addresses = addresses

    def getBankAccount(self):
        return self.bankAccount

    def setBankAccount(self, bankAccount):
        self.bankAccount = bankAccount
