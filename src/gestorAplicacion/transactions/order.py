class Order:
    instances = []

    def __init__(self, products, destinationAddress, totalPrice):
        self._products = []
        self._destinationAddress = destinationAddress
        self._totalPrice = totalPrice
        self._delivered = False
        self._deliveryPrice = 0
        self._id = len(Order.instances)

        Order.instances.append(self)

    def getProducts(self):
        return self._products

    def addProduct(self, product):
        self._products.append(product) 

    def getDestinationAddress(self):
        return self._destinationAddress

    def setDestinationAddress(self, address):
        self._destinationAddress = address

    def getTotalPrice(self):
        return self._totalPrice

    def setTotalPrice(self, price):
        self._totalPrice = price

    def isDelivered(self):
        return self._delivered

    def setDelivered(self, status):
        self._delivered = status

    def getDeliveryPrice(self):
        return self._deliveryPrice

    def setDeliveryPrice(self, price):
        self._deliveryPrice = price

    def getId(self):
        return self._id

    def setId(self, num):
        self._id = num

    # Bocetos de posibles funciones
    def CalcularPrecioTotal(self):
        total = float
        self.setTotalPrice(total)

    def CalcularPrecioDelivery(self):
        pago = float
        self.setDeliveryPrice(pago)
