import tkinter as tk

class ManageInventory(tk.Frame):
   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self.title = "Administrar Inventario"
      self.description = "Aqui pueda crear, borrar y actualizar productos"

      self.setup_ui()

   def setup_ui(self):
      pass
