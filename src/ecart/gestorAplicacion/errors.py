from collections.abc import Callable
from typing import Any, Optional, Tuple, Type, Union
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW

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
