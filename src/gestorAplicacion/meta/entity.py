class Entity:
    def __init__(self, username, password=""):
        self.name = username
        self.password = password

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password
