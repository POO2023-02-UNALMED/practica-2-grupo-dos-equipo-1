from tkinter import Tk
import pickle
from ecart.baseDatos.serializador import StoreSerializer
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.uiMain.ventanas.inicio import VentanaInicio
from ecart.gestorAplicacion.entites.admin import Admin


def cerrar_aplicacion(root):
   StoreSerializer.serialize()
   root.destroy()


def main() -> None:

   StoreSerializer.deserialize()

   ROOT = Tk()
   ROOT.geometry("1200x720")
   a = Admin("defualt", (0, 0))

   # ROOT.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
   ROOT.protocol("WM_DELETE_WINDOW", lambda: cerrar_aplicacion(ROOT))

   VentanaInicio.start(ROOT)

   ROOT.mainloop()
