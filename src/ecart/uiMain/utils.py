import tkinter as tk

from typing import Any, Iterator
import os

from ecart.uiMain.commons import Commons
"""
Este archivo contiene clases abstractas con metodos usados en varias partes de la interfaz
el cual  proporciona una serie de métodos estáticos útiles para la construcción y 
manipulación de elementos de la interfaz de usuario 


_build_frame (Método Estático Privado):
Construye y devuelve un nuevo marco (frame) con características comunes, como un borde resaltado en gris.


_build_label (Método Estático Privado):
Construye y devuelve una nueva etiqueta (label) que se autoajusta según su contenido.
Se usa para crear etiquetas que se ajustan automáticamente a su contenido y ajustan su longitud de línea (wraplength) dinámicamente.


iterate_inf (Método Estático):
Se usa principalmente para que en la interfaz siempre se repita infitamente y mostrar siempre su contenido
Crea un iterador infinito sobre una lista dada.
Se puede utilizar para iterar infinitamente sobre los elementos de una lista que en esta caso son lo autores


left_align (Método Estático):
Recibe un texto como entrada y devuelve el mismo texto con alineación a la izquierda.


get_images_iterator (Método Estático):
Obtiene y devuelve un iterador infinito sobre la lista de archivos en un directorio específico. 
Se usa para iterar infinitamente sobre los archivos de imágenes.
"""


class Utils:
   """builds a frame with common characteristics"""

   @staticmethod
   def _build_frame(holder_widget: tk.Frame) -> tk.Frame:
      return tk.Frame(holder_widget,
                      highlightbackground="gray",
                      highlightthickness=2)

   """builds a label that auroresizes itself"""

   @staticmethod
   def _build_label(*args: Any, **kwargs: Any) -> tk.Label:

      label = tk.Label(*args, **kwargs)
      label.bind("<Configure>",
                 lambda _: label.configure(wraplength=label.winfo_width()))

      return label

   """Iterates infinately over a given list"""

   @staticmethod
   def iterate_inf(l: Any) -> Iterator:
      while True:
         for item in l:
            yield item

   @staticmethod
   def left_align(text: str):
      return '\n'.join(line.lstrip() for line in text.split('\n'))

   """gets the root directory of the current module"""
   @staticmethod
   def get_module_rootdir() -> str:

      return os.path.join(
          os.path.abspath(__file__).split("ecart", 1)[0], "ecart")

   @staticmethod
   def get_file(*path: str) -> str:
      return os.path.join(Utils.get_module_rootdir(), *path)

   @staticmethod
   def get_image_file(*path: str) -> str:
      return os.path.join(Utils.get_module_rootdir(), "images", *path)

   @staticmethod
   def get_images(*source_path: str) -> list:

      source_dir = Utils.get_image_file(*source_path)
      files = []

      for f in os.listdir(source_dir):
         f_path = os.path.join(source_dir, f)

         if os.path.isfile(f_path):
            files.append(f_path)

      return files

   @staticmethod
   def get_images_iterator(*source_path: str) -> Iterator:
      return Utils.iterate_inf(Utils.get_images(*source_path))
