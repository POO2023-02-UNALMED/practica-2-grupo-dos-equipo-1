import tkinter as tk
from abc import ABC, abstractmethod

class Base(ABC, tk.Frame):
   def __init__(self, master: tk.Misc, title: str, description: str) -> None:
      super().__init__(master)

      self.master = master

      self.title = title 
      self.description = description

   @abstractmethod
   def setup_ui(self):
      pass

