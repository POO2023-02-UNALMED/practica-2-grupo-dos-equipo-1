from tkinter import messagebox
from typing import Any


# clase abstract para la utilizacion de messagebox de una manera no trivial
class MsgboxWrapper():

   @classmethod
   def show(cls, message_type, message, parent=None) -> Any:

      if message_type == "i":
         return messagebox.showinfo("Información", message, parent=parent)
      elif message_type == "w":
         return messagebox.showwarning("Advertencia", message, parent=parent)
      elif message_type == "e":
         return messagebox.showerror("Advertencia", message, parent=parent)
      elif message_type == "aq":
         return messagebox.askquestion("Pregunta", message, parent=parent)
      elif message_type == "ay":
         return messagebox.askyesno("Confirmación", message, parent=parent)
