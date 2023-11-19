import tkinter as tk

class ManageOrders(tk.Frame):
   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self.title = "Administrar Ordenes"
      self.description = "Aqui pueda crear, borrar y actualizar sus ordenes"

      self.setup_ui()

   def setup_ui(self):
      pass

