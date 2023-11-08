class Order(Serializable):
    instances = []

    def __init__(self, selectedProducts, destinationUser, totalPrice):
        self.selectedProducts = {}
        self.selectedProducts.update(selectedProducts)
        self.delivered = False
        self.totalPrice = totalPrice
        self.payedSoFar = 0
        self.deliveryPrice = 0
        self.destinationUser = destinationUser
        self.id = len(Order.instances)

        Order.instances.append(self)
