from tkinter import Tk

from ecart.uiMain.ventanas.inicio import VentanaInicio
from ecart.gestorAplicacion.entites.admin import Admin

def main() -> None:
   ROOT = Tk()
   ROOT.geometry("1200x720")

   Admin("defualt", (0,0))

   VentanaInicio.start(ROOT)

   ROOT.mainloop()
