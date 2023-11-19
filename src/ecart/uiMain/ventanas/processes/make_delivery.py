import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base


class MakeDelivery(Base):

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master, "Hacer Delivery",
                       "Aqui puede asignar deliveries a sus empleados")

   def setup_ui(self):
      pass
