import tkinter as tk


class VentanaPrincipal(tk.Frame):
   def __init__(self, master: tk.Tk, *args, **kwargs) -> None:

      super().__init__(master, *args, **kwargs)
      self.master: tk.Tk = master
      master.wm_title("Ecart - Usuario")
