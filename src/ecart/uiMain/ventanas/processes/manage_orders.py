import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base


class ManageOrders(Base):

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master, "Administrar Ordenes",
                       "Aqui pueda crear, borrar y actualizar sus ordenes")

   def setup_ui(self):
      pass
