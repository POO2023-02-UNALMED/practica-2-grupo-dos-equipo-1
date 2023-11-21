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
    apertura = open('Store', 'rb')
    pruebaa = pickle.load(apertura)
    apertura.close()

    ROOT = Tk()
    ROOT.geometry("1200x720")
    a = Admin("defualt", (0, 0))

    for c in pruebaa:
        a.create_store(c.get_name(), c.get_address(), c.get_tag(), c.get_description())
        a.create_delivery("angel", (12, 12))

    # ROOT.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
    ROOT.protocol("WM_DELETE_WINDOW", lambda: cerrar_aplicacion(ROOT))

    VentanaInicio.start(ROOT)

    ROOT.mainloop()


"""
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
"""
