import tkinter as tk
from ecart.uiMain.parts.msgbox_wrapper import MsgboxWrapper as MB


class VentanaInicio(tk.Frame):
   def __init__(self, master: tk.Tk, *args, **kwargs) -> None:
      super().__init__(master, *args, **kwargs)
      self.master: tk.Tk = master
      
      master.wm_title("Inicio")
      MB.show("i", "hello world!", self)

   def configurar_p1():
      pass

   def configurar_p2():
      pass

   def configurar_p3():
      pass

   def configurar_p4():
      pass

   def configurar_p5():
      pass

   def configurar_p6():
      pass
