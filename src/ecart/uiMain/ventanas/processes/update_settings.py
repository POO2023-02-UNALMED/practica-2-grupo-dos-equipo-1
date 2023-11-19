import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base


class UpdateSettings(Base):

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master, "Actualizar Configuraciones",
                       "Aqui puede actualizar sus configuraciones")

   def setup_ui(self):
      pass
