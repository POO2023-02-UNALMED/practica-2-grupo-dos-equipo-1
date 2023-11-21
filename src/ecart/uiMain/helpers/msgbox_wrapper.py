from tkinter import messagebox
from typing import Any

"""
clase abstract para la utilizacion de messagebox de una manera no trivial

show (Método Estático):
Este método estático permite mostrar diferentes tipos de cuadros de mensaje según el tipo de mensaje proporcionado.
El cual tiene los siguientes parametros
Los parámetros son:

message_type: Tipo de mensaje (
"i" para información, 
"w" para advertencia, 
"e" para error, "aq" para pregunta, 
"ay" para confirmación).

message: El mensaje que se mostrará en el cuadro de mensaje.

Utiliza el módulo messagebox de Tkinter para mostrar el cuadro de mensaje correspondiente según el tipo proporcionado.
"""

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
