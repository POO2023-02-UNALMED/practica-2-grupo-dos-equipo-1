from typing import Tuple
import pickle
from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.gestorAplicacion.entites.entity import Entity


def deserializar():
    # Deserializar la lista de instancias desde el archivo
    with open('archivo_serializado.pkl', 'rb') as archivo:
        lista_deserializada = pickle.load(archivo)
    return lista_deserializada


class Store(Entity):
    instances = []

    def __init__(self, name: str, address: Tuple[int, int], tag: Tags,
                 description: str):

        super().__init__(name, address)

        self._description = description
        self._tag = tag
        self._balance = 0
        # self._products: list[Product] = []

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

        return Store(name, address, tag, description)

    def update_settings(self, name, address, tag, description) -> str:

        if not self.is_address_available(address):
            raise errors.ErrorSystemOperation(
                f"La direccion {address} ya está en uso. Recuerda que ninguno puede pasarse de 100")

        self.set_name(name)
        self.set_address(address)
        self.set_tag(tag)
        self.set_description(description)

        return "Se actualizó la configuración de la tienda correctamente"

    def serializar(self):
        # Serializar la lista de instancias
        with open('archivo_serializado.pkl', 'wb') as archivo:
            pickle.dump(self, archivo)


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

    # def get_products(self):
    #    return self._products
    #
    # def add_product(self, product) -> None:
    #    self._products.append(product)

    # def createProduct(self, name, price, description, quantity, tag):
    #    newProduct = Product.create(name, price, description, quantity, tag)
    #    if newProduct is None:
    #       return Retval(
    #           "Failed to create product. The product already exists inside the store",
    #           False)
    #
    #    self.add_product(newProduct)
    #
    #    return Retval("Created product successfully!")

    """
        class StoreSerializer:
            @staticmethod
            def serialize(stores):
                serialized_stores = []
                for store in stores:
                    serialized_store = {
                        'name': store.get_name(),
                        'address': store.get_address(),
                        'tag': store._tag,  # Assuming Tags is serializable
                        'description': store.get_description(),
                        'balance': store.get_balance()
                    }
                    serialized_stores.append(serialized_store)
                return pickle.dumps(serialized_stores)

            @staticmethod
            def deserialize(serialized_data):
                deserialized_stores = pickle.loads(serialized_data)
                stores = []
                for data in deserialized_stores:
                    name = data['name']
                    address = data['address']
                    tag = data['tag']
                    description = data['description']
                    balance = data['balance']

                    # Assuming Tags has a method to deserialize itself
                    deserialized_tag = Tags.deserialize(tag)

                    # Create a new Store instance
                    store = Store.create(name, address, deserialized_tag, description)
                    store.set_balance(balance)

                    stores.append(store)

                return stores
    """
