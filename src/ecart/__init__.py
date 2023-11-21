from tkinter import Tk
import pickle
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.uiMain.ventanas.inicio import VentanaInicio
from ecart.gestorAplicacion.entites.admin import Admin


def cerrar_aplicacion(root):
    # Serializar todas las instancias de la clase Store
    fichero = open("Store", 'wb')
    pickle.dump(Store.instances, fichero)
    fichero.close()

    root.destroy()


def main() -> None:

    ROOT = Tk()
    ROOT.geometry("1200x720")
    a = Admin("defualt", (0, 0))

    # ROOT.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
    ROOT.protocol("WM_DELETE_WINDOW", lambda: cerrar_aplicacion(ROOT))

    VentanaInicio.start(ROOT)

    ROOT.mainloop()
