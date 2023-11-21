from collections.abc import Callable
from typing import Any, Optional, Tuple, Type, Union
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW

"""

Manejo de Errores

Para el manejo de errores se deberá hacer una jerarquía de errores empezando por una clase de error
llamada ErrorAplicacion que es hija de la clase Exception.

Clase Base ErrorAplicacion (Application Error):

Hereda de la clase base Exception.
Representa un error general de la aplicación.
Tiene un constructor que toma un tipo (kind) y un mensaje (msg).
Almacena el mensaje en un formato específico que incluye el tipo del error.


Función display:
Toma un error (opcional) como argumento y muestra el error 
utilizando la clase MsgboxWrapper (abreviada como MW).


Función pcall:
Implementa un mecanismo de llamada a funciones con manejo de errores.
Toma una función (fn) y sus argumentos y keyword arguments.
Intenta ejecutar la función y captura cualquier excepción.
Si la ejecución tiene éxito, devuelve una tupla con un indicador booleano (ok) y los valores de retorno de la función.


Clases de Errores Específicos:
ErrorInput, 
ErrorInputEmpty, 
ErrorInputType, 
ErrorSystem, 
ErrorSystemOperation 
son clases que heredan de ErrorAplicacion


"""


class ErrorAplicacion(Exception):
    def __init__(self, kind: str, msg: str) -> None:
        super().__init__(f"Error ({kind}):\n\n\n{msg}")


def display(error: Optional[Union[Type[Exception], Exception]] = None) -> None:
    MW.show("e", str(error))


def pcall(fn: Callable, *args, **kwargs) -> Tuple[bool, *tuple[Any, ...]]:
    try:
        ok, *retval = True, fn(*args, **kwargs)

        if isinstance(retval[0], str):
            MW.show("i", retval[0])

        return ok, *retval

    except Exception as e:
        display(e)
        return False, str(e)


class ErrorInput(ErrorAplicacion):
    def __init__(self, kind: str, msg: str) -> None:
        super().__init__(f"input -> {kind}", msg)


class ErrorInputEmpty(ErrorInput):
    def __init__(self, msg: str) -> None:
        super().__init__("empty values", msg)


class ErrorInputType(ErrorInput):
    def __init__(self, msg: str) -> None:
        super().__init__("data type", msg)


class ErrorSystem(ErrorAplicacion):
    def __init__(self, kind: str, msg: str) -> None:
        super().__init__(f"system -> {kind}", msg)


class ErrorSystemOperation(ErrorSystem):
    def __init__(self, msg: str) -> None:
        super().__init__("invalid operation", msg)


class ErrorSystemActivity(ErrorSystem):
    def __init__(self, msg: str) -> None:
        super().__init__("background activity", msg)
