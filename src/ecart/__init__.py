from tkinter import Tk
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags

from ecart.uiMain.ventanas.inicio import VentanaInicio
from ecart.gestorAplicacion.entites.admin import Admin

def main() -> None:
   ROOT = Tk()
   ROOT.geometry("1200x720")

   a = Admin("defualt", (0,0))
   # NO BORRAR, ES PARA TESTEAR MAS RAPIDAMENTE
   a.create_store("Hello World", (100, 100), Tags.ALIMENTOS, "super cool store")
   s = Store.find("Hello World")
   if s:
      a.set_current_store(s)
   a.create_delivery("Pedro", (99, 99))
   

   VentanaInicio.start(ROOT)

   ROOT.mainloop()
