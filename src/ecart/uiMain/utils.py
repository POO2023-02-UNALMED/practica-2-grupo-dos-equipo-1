import tkinter as tk
from typing import Any, Iterator
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
   def iterate_inf(l) -> Iterator:
      while True:
         for item in l: yield item

   @staticmethod
   def left_align(text):
      return '\n'.join(line.lstrip() for line in text.split('\n'))

   """gets the root directory of the current module"""
   @staticmethod
   def get_module_rootdir() -> str:

      module_path = os.path.abspath(sys.path[0])

      if os.path.isfile(module_path):
         return os.path.dirname(module_path)

      return module_path

   @staticmethod
   def get_images(*source_path) -> list:

      source_dir = os.path.join(Utils.get_module_rootdir(), "ecart", "images", *source_path)

      files = []

      for f in os.listdir(source_dir):
         f_path = os.path.join(source_dir, f)

         if os.path.isfile(f_path):
            files.append(f_path)

      return files

   @staticmethod
   def get_images_iterator(*source_path) -> Iterator:
      return Utils.iterate_inf(Utils.get_images(*source_path))
