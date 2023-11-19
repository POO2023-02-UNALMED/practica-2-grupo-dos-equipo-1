import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base


class ManagePersonnel(Base):

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(
          master, "Administrar Personal",
          "Aqui pueda crear, borrar y actualizar a sus empleados")

   def setup_ui(self):
      pass
