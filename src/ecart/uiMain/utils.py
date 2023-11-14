import tkinter as tk
from typing import Any
import os, sys


# este archivo contiene clases abstractas con
# metodos usados en varias partes de la interfaz

class Utils:
   """builds a frame with common characteristics"""
   @staticmethod
   def _build_frame(holder_widget: tk.Frame) -> tk.Frame:
      return tk.Frame(holder_widget, highlightbackground="gray", highlightthickness=2)

   """builds a label that auroresizes itself"""
   @staticmethod
   def _build_label(*args: Any, **kwargs: Any) -> tk.Label:
      label = tk.Label(*args, **kwargs, font=("Broadway",12))
      label.bind("<Configure>", lambda _: label.configure(wraplength=label.winfo_width()))
      return label

   """Iterates infinately over a given list"""
   @staticmethod
   def iterate_inf(l) -> Any:
      while True:
         for item in l: yield item

   """gets the root directory of the current module"""
   @staticmethod
   def get_module_rootdir() -> str:
      module_path = os.path.abspath(sys.path[0])

      if os.path.isfile(module_path):
         return os.path.dirname(module_path)

      return module_path

   """gets the root directory of the current module"""
   @staticmethod
   def get_image_path(*path_to_image) -> str:
      return os.path.join(Utils.get_module_rootdir(), "ecart", "images", *path_to_image)
