from os import error
from typing import Optional, Tuple
from ecart.gestorAplicacion.entites.delivery import Delivery
from ecart.gestorAplicacion.merchandise.product import Product

from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.merchandise.store import deserializar
from ecart.gestorAplicacion.transactions.order import Order
from .entity import Entity
import ecart.gestorAplicacion.errors as errors


class Admin(Entity):

   def __init__(self, name, address):

      super().__init__(name, address)
      self._current_store: Store | None = None

      Admin.current: Admin = self

   def create_order(self, products: dict[str, int], destination_address: Tuple[int ,int]):
      if self._current_store:
         self._current_store.create_order(products, destination_address)

      return "Se ha creado la orden de manera exitosa"

   def create_product(self, name: str, price: float, quantity: int, description: str):
      if self._current_store:
         self._current_store.create_product(name, price, quantity, description)

      return "Se ha creado el producto de manera exitosa"

   def delete_order(self, order: Order):
      if self._current_store:
         self._current_store.get_orders().remove(order)

         return "Se ha borrado la orden exitosamente"

      raise errors.ErrorSystemOperation("No una tienda actual")

   def delete_product(self, product: Product):
      if self._current_store:
         self._current_store.get_products().remove(product)

         return "Se ha borrado el producto exitosamente"

      raise errors.ErrorSystemOperation("No una tienda actual")

   def create_delivery(self, name: str, address: Tuple[int, int]):

      if self._current_store:
         new_delivery = Delivery.create(name, address, self._current_store, self._current_store.get_deliveries())
         if new_delivery is None:
            raise errors.ErrorSystemOperation(
                "Ya existe un delivery on ese nombre")

      return "Se ha creado el delivery correctamente"

   def delete_delivery(self, delivery: Delivery):
      if self._current_store:
         self._current_store.get_deliveries().remove(delivery)

         return "Se ha borrado el delivery con exito"

      raise errors.ErrorSystemOperation("No una tienda actual")

   def get_current_store_orders(self) -> list[Order]:
      if self._current_store:
         return self._current_store.get_orders()

      return []

   def get_current_store_deliveries(self) -> list[Delivery]:
      if self._current_store:
         return self._current_store.get_deliveries()

      return []

   def get_current_store_products(self) -> list[Product]:
      if self._current_store:
         return self._current_store.get_products()

      return []

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
