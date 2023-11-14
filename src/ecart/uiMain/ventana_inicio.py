import tkinter as tk
from ecart.uiMain.parts.msgbox_wrapper import MsgboxWrapper as MB


class VentanaInicio(tk.Frame):
   def __init__(self, master: tk.Tk, *args, **kwargs) -> None:
      super().__init__(master, *args, **kwargs)
      self.master: tk.Tk = master
      
      master.wm_title("Ecart - Inicio")

      self.configure_menubar()

   def exit_program(self) -> None:

      should_exit = MB.show("ay", "Estas seguro que deseas salir de la aplicación?")
      if should_exit:
         self.master.destroy()

   def toggle_description(self) -> None:
      pass

   def configure_menubar(self) -> None:

      menubar = tk.Menu(self.master)

      inicio_menu = tk.Menu(menubar, tearoff=False)
      menubar.add_cascade(label="Inicio", menu=inicio_menu)

      inicio_menu.add_command(label="Salir", command=self.exit_program)
      inicio_menu.add_separator()
      inicio_menu.add_command(label="Descripción", command=self.toggle_description)

      self.master.config(menu=menubar)

   def configure_p1(self) -> None:
      pass

   def configure_p2(self) -> None:
      pass

   def configure_p3(self) -> None:
      pass

   def configure_p4(self) -> None:
      pass

   def configure_p5(self) -> None:
      pass

   def configure_p6(self) -> None:
      pass
