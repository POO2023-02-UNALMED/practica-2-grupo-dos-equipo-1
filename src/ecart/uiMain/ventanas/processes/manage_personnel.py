import tkinter as tk

class ManagePersonnel(tk.Frame):
   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self.title = "Administrar Personal"
      self.description = "Aqui pueda crear, borrar y actualizar a sus empleados"

      self.setup_ui()

   def setup_ui(self):
      pass
