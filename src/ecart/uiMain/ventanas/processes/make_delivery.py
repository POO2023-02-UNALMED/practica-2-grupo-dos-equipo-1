import tkinter as tk

class MakeDelivery(tk.Frame):
   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self.title = "Hacer Delivery"
      self.description = "Aqui puede asignar deliveries a sus empleados"

      self.setup_ui()

   def setup_ui(self):
      pass

