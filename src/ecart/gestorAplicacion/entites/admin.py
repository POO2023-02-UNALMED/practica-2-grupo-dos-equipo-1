from os import error
from typing import Optional, Tuple

from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.merchandise.store import deserializar
from .entity import Entity
import ecart.gestorAplicacion.errors as errors


class Admin(Entity):

   def __init__(self, name, address):

      super().__init__(name, address)
      self._current_store: Store | None = None

      Admin.current: Admin = self

   def create_store(self, name: str, address: Tuple[int, int], tag: Tags,
                    description: str):

      new_store = Store.create(name, address, tag, description)
      if new_store is None:
         raise errors.ErrorSystemOperation(
             "Ya existe una tienda con ese nombre")

      return "Se ha creado la tienda correctamente"

   def update_settings(self, name, address) -> str:

      if not self.is_address_available(address):
         raise errors.ErrorSystemOperation(
             f"La direccion {address} ya está en uso. Recuerda que ninguno puede pasarse de 100"
         )

      self.set_name(name)
      self.set_address(address)

      return "Se actualizó la configuración del administrador correctamente"

   def set_current_store(self, current_store: Store) -> None:
      self._current_store = current_store

   def get_current_store(self) -> Optional[Store]:
      return self._current_store

   # # Las funciones que siguen son como para tener una idea de lo que podrá hacer el admin
   # def makeOrder(self):  # Crea un objeto Order
   #     order = Order()
   #     return order
   #
   # def newDelivery(name):  # Crea un nuevo Delivery
   #     return Delivery(name)
   #
   # def assignOrder(order, delivery):  # Le asigna a un delivery una orden creada
   #     delivery.addOrder(order)
   #
   # # Metodos definidos para la clase user (Ahora admin)
   # # Sin password
   #
   # def createProduct(self, store, name, price, description, quantity, tag):
   #     return store.createProduct(name, price, description, quantity, tag, self)
   #
   # def addStore(self, store):
   #     return self.addStoreByName(store.getName())
   #
   # def addStoreByName(self, name):
   #     existingStore = Store.validate(name)
   #     if existingStore is None:
   #         return Retval("Error: the store does not exist", False)
   #
   #     retval = existingStore.addUser(self.getName())
   #     if retval.isOk():
   #         self.stores.append(existingStore)
   #
   #     return retval
   #
   # def addToShoppingCart(self, productName, quantity):
   #     existingProduct = Product.validate(productName)
   #
   #     retval = self.shoppingCart.addProduct(existingProduct, quantity)
   #
   #     return retval
   #
   # @staticmethod
   # def listProduct(productName, store, doList):
   #     existingProduct = Product.validate(productName, store.getProducts())
   #     if existingProduct is None:
   #         return Retval("Error: there is no such product inside the store", False)
   #
   #     existingProduct.setListed(doList)
   #
   #     return Retval("Unlisted product successfully")
