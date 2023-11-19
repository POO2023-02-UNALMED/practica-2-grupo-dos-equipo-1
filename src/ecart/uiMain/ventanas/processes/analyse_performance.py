import tkinter as tk

class AnalysePerformance(tk.Frame):
   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self.title = "Analizar Rendimiento"
      self.description = "Aqui puede ver como ha sido en rendimiento de su negocio"

      self.setup_ui()

   def setup_ui(self):
      pass

