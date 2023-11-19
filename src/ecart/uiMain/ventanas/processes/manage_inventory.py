import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base


class ManageInventory(Base):

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master, "Administrar Inventario",
                       "Aqui pueda crear, borrar y actualizar productos")

   def setup_ui(self):
      pass
