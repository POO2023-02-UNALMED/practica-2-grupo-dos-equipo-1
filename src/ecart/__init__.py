from tkinter import Tk

from ecart.uiMain.ventanas.inicio import VentanaInicio

def main() -> None:
   ROOT = Tk()
   ROOT.geometry("1200x720")

   VentanaInicio.start(ROOT)

   ROOT.mainloop()
