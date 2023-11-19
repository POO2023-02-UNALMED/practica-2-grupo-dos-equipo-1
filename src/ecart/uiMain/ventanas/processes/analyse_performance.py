import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base


class AnalysePerformance(Base):

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(
          master, "Analizar Rendimiento",
          "Aqui puede ver como ha sido en rendimiento de su negocio")

   def setup_ui(self):
      pass
