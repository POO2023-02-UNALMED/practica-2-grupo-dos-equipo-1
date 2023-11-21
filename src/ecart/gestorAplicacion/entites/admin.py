from os import error
from typing import Optional, Tuple
from ecart.gestorAplicacion.entites.delivery import Delivery
from ecart.gestorAplicacion.merchandise.product import Product

from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.transactions.order import Order
from .entity import Entity
import ecart.gestorAplicacion.errors as errors

"""
Admin hereda de la clase llamada Entity. 
La clase Admin representa un administrador en el sistema de esta aplicacion:

Metodo __init__ que recibe dos parámetros: name y address.

Métodos para Manipulación de Productos (create_product, delete_product)

Métodos para Manipulación de Deliveries (create_delivery, delete_delivery)

Aunque estos metodos sean parecidos sus funcionalidades son completamente diferentes

Método para Crear una Nueva Tienda (create_store)

Métodos para Configuración de Tienda Actual (set_current_store, get_current_store):
"""


class Admin(Entity):

    def __init__(self, name, address):

        super().__init__(name, address)
        self._current_store: Store | None = None

        Admin.current: Admin = self

    def create_order(self, products: dict[str, int], destination_address: Tuple[int, int]):
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
