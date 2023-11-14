from tkinter import messagebox
from typing import Any


# clase abstract para la utilizacion de messagebox de una manera no trivial
class MsgboxWrapper():
   @classmethod
   def show(cls, message_type, message, parent = None) -> Any:
      if message_type == "w":
         return messagebox.showwarning("Warning", message, parent=parent)
      elif message_type == "i":
         return messagebox.showinfo("Info", message, parent=parent)
      elif message_type == "aq":
         return messagebox.askquestion("Ask Question", message, parent=parent)
