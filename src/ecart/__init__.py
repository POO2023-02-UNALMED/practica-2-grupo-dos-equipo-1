from tkinter import Tk
from ecart.uiMain.ventanas.inicio import VentanaInicio

def main() -> None:
   ROOT = Tk()
   ROOT.geometry("1024x576")

   VentanaInicio(ROOT, bg="lightblue").pack(fill="both", side="top", expand = True)

   ROOT.mainloop()
