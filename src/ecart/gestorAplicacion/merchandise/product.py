from ecart.gestorAplicacion import errors

"""
En product es donde se genera la gestion e interaccion de productos

Método __init__:

Es el método del constructor que se llama cuando se crea una instancia de la clase Product.
Recibe cinco parámetros: 
name (nombre del producto), 
price (precio del producto), 
quantity (cantidad actual del producto), 
description (descripción del producto).

Método de Clase find:
Recibe un nombre (name) y una lista de productos (arr).
Busca un producto por su nombre en la lista de productos


Método de Clase create:
Crea y retorna una nueva instancia de Product


Método increase_quantity:
Recibe una cantidad (quantity) y aumenta la cantidad del producto 
ademas de actualizar el atributo de _historic_quantity


Método update_settings:
Recibe una lista de productos (arr) y nuevos valores para el nombre, precio, cantidad y descripción del producto.

"""


class Product:

    def __init__(self, name: str, price: float, quantity: int, description: str):

        self._name = name
        self._price = price
        self._quantity = quantity
        self._historic_quantity = quantity
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

    def increase_quantity(self, quantity):
        if abs(quantity) == quantity:
            self._historic_quantity += quantity

        if self._quantity + quantity < 0:
            self._quantity = 0
        else:
            self._quantity += quantity

    def set_historic_quantity(self, quantity):
        self._historic_quantity = quantity

    def get_historic_quantity(self):
        return self._historic_quantity

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
