class Product:

   def __init__(self, name: str, price: float, quantity: int, description: str):

      self._name = name
      self._price = price
      self._quantity = quantity
      self._description = description

   @classmethod
   def find(cls, name: str, arr):
      for product in arr:
         if product.get_name() == name:
            return product

      return None

   @classmethod
   def create(cls, name: str, price: float, quantity: int, description: str):
      return cls(name, price, quantity, description)

   def get_name(self):
      return self._name

   def set_name(self, name):
      self._name = name

   def get_nrice(self):
      return self._price

   def set_price(self, price):
      self._price = price

   def get_description(self):
      return self._description

   def set_description(self, description):
      self._description = description

   def get_quantity(self):
      return self._quantity

   def set_quantity(self, quantity):
      self._quantity = quantity
