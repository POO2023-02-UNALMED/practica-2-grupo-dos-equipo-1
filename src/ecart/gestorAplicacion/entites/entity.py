from typing import Tuple

from ecart.gestorAplicacion import errors


class Entity:
   addresses = []

   def __init__(self, name: str, address: Tuple[int, int]) -> None:
      self._name = name
      self._address = address

      if not self.is_address_available():
         raise errors.ErrorSystemOperation(f"La direccion {address} ya está en uso. Recuerda que ninguno puede pasarse de 100")

      self.addresses.append(address)

   def is_address_available(self) -> bool:
      if not (0 <= self._address[0] <= 100) or not (0 <= self._address[1] <= 100):
         return False

      for address in Entity.addresses:
         if address[0] == self._address[0] and address[1] == self._address[1]:
            return False

      return True

   def get_name(self) -> str:
      return self._name

   def set_name(self, name: str) -> None:
      self._name = name

   def get_address(self) -> Tuple[int, int]:
      return self._address

   def set_address(self, address) -> None:
      self._address = address
