from ecart.gestorAplicacion import errors


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

   def update_settings(self, arr, name, price, quantity, description) -> str:

      for product in arr:
         if product.get_name() == name and product != self:
            raise errors.ErrorSystemOperation(
                f"Ese nombre ya esta en uso por otro producto"
            )

      self.set_name(name)
      self.set_price(price)
      self.set_quantity(quantity)
      self.set_description(description)

      return "Se actualizó la configuración del producto correctamente"

   def get_name(self):
      return self._name

   def set_name(self, name):
      self._name = name

   def get_price(self):
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
