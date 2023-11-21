from typing import Tuple
import pickle
from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.merchandise.product import Product
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.entites.entity import Entity
from ecart.gestorAplicacion.transactions.order import Order


class Store(Entity):
    instances = []

    def __init__(self, name: str, address: Tuple[int, int], tag: Tags,
                 description: str):

        super().__init__(name, address)

        self._description = description
        self._tag = tag
        self._balance = 0
        self._orders: list[Order] = []

        from ecart.gestorAplicacion.entites.delivery import Delivery
        self._deliveries: list[Delivery] = []
        self._products: list[Product] = []

        Store.instances.append(self)

    @classmethod
    def get(cls) -> list:
        return cls.instances

    @classmethod
    def find(cls, name: str):
        for store in cls.instances:
            if store.get_name() == name:
                return store

        return None

    @classmethod
    def create(cls, name: str, address: Tuple[int, int], tag: Tags,
               description: str):

        if cls.find(name) is not None:
            return None

        return cls(name, address, tag, description)

    def get_order_by_id(self, id: int):
        for order in self._orders:
            if order.getId() == id:
                return order

        raise errors.ErrorSystemActivity("No se pudo encontrar una orden con ese ID")

    def get_orders(self) -> list[Order]:
        return self._orders

    def create_order(self, products: dict[str, int], destination_address: Tuple[int, int]):
        o = Order(products, destination_address, self.get_address())
        self._orders.append(o)

    def get_products(self) -> list[Product]:
        return self._products

    def get_product_by_name(self, name):
        for product in self._products:
            if product.get_name() == name:
                return product

        return None

    def create_product(self, name: str, price: float, quantity: int, description: str):
        p = Product(name, price, quantity, description)
        self._products.append(p)

    def get_deliveries(self) -> list:
        return self._deliveries

    def set_deliveries(self, deliveries) -> None:
        self._deliveries = deliveries

    def update_settings(self, name, address, tag, description) -> str:

        if not self.is_address_available(address):
            raise errors.ErrorSystemOperation(
                f"La direccion {address} ya está en uso. Recuerda que ninguno puede pasarse de 100"
            )

        self.set_name(name)
        self.set_address(address)
        self.set_tag(tag)
        self.set_description(description)

        return "Se actualizó la configuración de la tienda correctamente"

    @classmethod
    def get_instances(cls):
        return cls.instances

    def add_delivery(self, delivery):
        self._deliveries.append(delivery)

    def serializar(self):
        # Serializar la lista de instancias
        with open('archivo_serializado.pkl', 'wb') as archivo:
            pickle.dump(self, archivo)

    def get_tag(self):
        return self._tag

    def set_tag(self, tag: Tags) -> None:
        self._tag = tag

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_balance(self) -> int:
        return self._balance

    def set_balance(self, balance: int) -> None:
        self._balance = balance


"""
    @classmethod
    def deserializar(cls):
        try:
            with open('archivo_serializado.pkl', 'rb') as archivo:
                cls.instances = pickle.load(archivo)
        except FileNotFoundError:
            # Si el archivo no existe, simplemente crea una instancia vacía
            cls.instances = []

    def serializar(self):
        # Serializar la lista de instancias
        with open('archivo_serializado.pkl', 'wb') as archivo:
            pickle.dump(Store.instances, archivo)

    @staticmethod
    def get_instances():
        return Store.instances
"""
