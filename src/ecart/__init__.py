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
   a.create_store("Other Store", (90, 90), Tags.ALIMENTOS, "super cool store")

   s = Store.find("Hello World")
   o = Store.find("Other Store")
   if s:
      a.set_current_store(s)

   a.create_delivery("Pedro", (99, 99))

   a.create_product("Manzana", 10.0, 100, "super cool fruit")
   a.create_product("Pera", 5.0, 100, "super cool fruit")
   a.create_product("Mango", 8.0, 100, "super cool fruit")

   if o:
      a.set_current_store(o)

   a.create_product("Banano", 10.0, 20, "super cool fruit")
   a.create_product("Sandia", 5.0, 10, "super cool fruit")
   a.create_product("Melones", 8.0, 10, "super cool fruit")

   if s:
      a.set_current_store(s)
   

   VentanaInicio.start(ROOT)

   ROOT.mainloop()
