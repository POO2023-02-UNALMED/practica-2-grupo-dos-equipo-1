from ecart.gestorAplicacion.merchandise.product import Product


class Order:
   instances = []

   def __init__(self, products: dict[str, int], destinationAddress,
                origin_address):
      self._products = products
      self._destinationAddress = destinationAddress
      self._origin_address = origin_address

      self._totalPrice = 0
      self._delivered = False
      self._deliveryPrice = 0
      self._id = len(Order.instances)

      Order.instances.append(self)

   def update_settings(self, products: dict[str, int], destinationAddress):
      self.setProducts(products)
      self.setDestinationAddress(destinationAddress)

   def get_origin_address(self):
      return self._origin_address

   def is_delivered(self):
      return self._delivered

   def set_delivered(self, delivered):
      self._delivered = delivered

   def getProducts(self) -> dict[str, int]:
      return self._products

   def setProducts(self, products):
      self._products = products

   # def addProduct(self, product):
   #    self._products.append(product)

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
