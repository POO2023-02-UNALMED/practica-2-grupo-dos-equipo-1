import tkinter as tk
from abc import ABC, abstractmethod

"""
Esta clase contiene la plantilla basica para cada una de las ventanas que contienen las funcionalidades

Es una clase abstracta de la cual heredan todas las clases que estan en el package processes

Metodo (__init__) el cual recibe el elemento primario que en cualquier caso sera master titulo y la 
descripcion para luego llamar super() e inicializar la parte de la interfaz de usuario


Se declara un método abstracto llamado setup_ui utilizando el decorador @abstractmethod. 
Este método deberá ser implementado por las clases que heredan de Base.

"""

class Base(ABC, tk.Frame):
   def __init__(self, master: tk.Misc, title: str, description: str) -> None:
      super().__init__(master)

      self.master = master

      self.title = title
      self.description = description

   @abstractmethod
   def setup_ui(self):
      pass

