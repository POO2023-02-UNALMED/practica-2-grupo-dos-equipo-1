import pickle
from gestorAplicacion.entites.admin import Admin
from ecart.gestorAplicacion.merchandise.store import *


class StoreSerializer:
    @staticmethod
    def serialize(store):
        serialized_store = {
            'name': store.get_name(),
            'address': store.get_address(),
            'tag': store._tag,  # Assuming Tags is serializable
            'description': store.get_description(),
            'balance': store.get_balance()
        }
        return pickle.dumps(serialized_store)

    @staticmethod
    def deserialize(serialized_data):
        deserialized_data = pickle.loads(serialized_data)
        name = deserialized_data['name']
        address = deserialized_data['address']
        tag = deserialized_data['tag']
        description = deserialized_data['description']
        balance = deserialized_data['balance']

        # Assuming Tags has a method to deserialize itself
        deserialized_tag = Tags.deserialize(tag)

        # Create a new Store instance
        store = Store.create(name, address, deserialized_tag, description)
        store.set_balance(balance)

        return store

    def save_stores_to_file(file_path, stores):
        serialized_stores = [StoreSerializer.serialize(store) for store in stores]
        with open(file_path, 'wb') as file:
            pickle.dump(serialized_stores, file)

    def load_stores_from_file(file_path):
        try:
            with open(file_path, 'rb') as file:
                serialized_stores = pickle.load(file)
                stores = [StoreSerializer.deserialize(data) for data in serialized_stores]
                return stores
        except FileNotFoundError:
            return []

    # Guardar las tiendas en un archivo al cerrar el programa
    save_stores_to_file('stores_data.pkl', Store.get())

    # Cargar las tiendas desde un archivo al abrir el programa
    loaded_stores = load_stores_from_file('stores_data.pkl')