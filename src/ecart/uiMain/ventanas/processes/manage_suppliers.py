import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base


class ManageSuppliers(Base):

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master, "Administrar Proveedores",
                       "Aqui puede distribuir recursos entre sus tiendas")

   def setup_ui(self):
      pass
