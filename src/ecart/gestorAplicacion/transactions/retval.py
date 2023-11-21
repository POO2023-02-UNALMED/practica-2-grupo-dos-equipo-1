
"""
Clase Retval:

Representa un objeto de retorno que contiene un mensaje y un indicador booleano (ok)
que indica si una operación fue exitosa.

Método __init__:

Constructor de la clase que inicializa el objeto Retval.
Toma dos parámetros opcionales:
message (mensaje) y ok (indicador booleano de éxito).
Por defecto, message está configurado en una cadena vacía ("") y ok está configurado en False.
"""

class Retval:
    def __init__(self, message="", ok=False):
        self.message = message
        self.ok = ok

    def getMessage(self):
        return self.message

    def isOk(self):
        return self.ok
