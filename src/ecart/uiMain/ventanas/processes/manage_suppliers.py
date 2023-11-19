import tkinter as tk

class ManageSuppliers(tk.Frame):
   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self.title = "Administrar Proveedores"
      self.description = "Aqui puede distribuir recursos entre sus tiendas"

      self.setup_ui()

   def setup_ui(self):
      pass

