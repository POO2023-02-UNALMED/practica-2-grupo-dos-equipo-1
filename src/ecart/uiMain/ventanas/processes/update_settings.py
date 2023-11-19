import tkinter as tk

class UpdateSettings(tk.Frame):
   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self.title = "Actualizar Configuraciones"
      self.description = "Aqui puede actualizar sus configuraciones"

      self.setup_ui()

   def setup_ui(self):
      pass

