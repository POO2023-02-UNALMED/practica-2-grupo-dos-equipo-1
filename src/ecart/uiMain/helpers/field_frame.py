from collections.abc import Callable
import tkinter as tk
from typing import Any, Tuple, Union
from tkinter import ttk
import string
from ecart.gestorAplicacion import errors

from ecart.uiMain.commons import Commons

"""
Se deberá implementar un componente FieldFrame que herede de Frame para visualizar y gestionar listas de
atributo-valor. La interface pública deberá ser como mínimo:
class FieldFrame(Frame):

    crea un nuevo objeto de tipo FieldFrame
    @arg tituloCriterios titulo para la columna "Criterio"
    @arg criterios array con los nombres de los criterios
    @arg tituloValores titulo para la columna "valor"
    @arg valores array con los valores iniciales; Si ‘None’, no hay valores iniciales
    @arg habilitado array con los campos no-editables por el usuario; Si ‘None’, todos son editables

def init (tituloCriterios, criterios, tituloValores, valores, habilitado):
...
/**
@arg criterio el criterio cuyo valor se quiere obtener
@return el valor del criterio cuyo nombre es 'criterio'
*/
Def getValue(self, criterio):



"""
class FieldFrame(tk.Frame):
   """ Example call:
      
      ff = FieldFrame(
         some_window,
         "Fields",
         "Entries"
         [
            "Name",
            ("Description\n"), # text box
            ("Opinion", "no opinion"), # normal Entry with default value
            ("ID", existing_id, True), # disable the field
            ("Colors", ["red", "green", "blue"]) # combobox
         ]
      )

      (<field name>, <value(s)>, disable?)
      (mandatory, defaults: None, default: false)
   """

   def __init__(self, master: tk.Misc, title: str, fields_title: str,
                entries_title: str, fields: list, save_callback: Callable,
                *args, **kwargs):
      super().__init__(master, *args, **kwargs)

      if title:
         tk.Label(self, text=title, font=Commons.TEXT_FONT_B).pack(pady=(10, 7))

      self.form = tk.Frame(self,
                           highlightthickness=2,
                           highlightbackground="gray", padx=45, pady=10)
      self.form.pack(expand=True, side="top", anchor="center")
      self.form.grid_columnconfigure(0, pad=20)

      clear_button = tk.Button(self.form,
                               text="   Borrar   ",
                               command=self.clear_values)
      save_button = tk.Button(self.form,
                              text="   Guardar   ",
                              command=lambda: self.get_values(save_callback))

      if fields_title:
         tk.Label(self.form, text=fields_title,
                  font=Commons.TEXT_FONT_B).grid(row=0, column=0)

      if entries_title:
         tk.Label(self.form, text=entries_title,
                  font=Commons.TEXT_FONT_B).grid(row=0, column=1, columnspan=3)

      self._entries: dict[str, Union[tk.Entry, ttk.Combobox, tk.Text]] = {}

      for i, field in enumerate(fields, start=2):
         _field = list(field)

         if isinstance(field, str): _field[0:] = [field]
         else: _field = field

         if len(_field) < 2: _field.append(None)
         if len(_field) < 3: _field.append(False)

         tk.Label(self.form,
                  text=_field[0],
                  justify="left",
                  font=Commons.TEXT_FONT_I,
                  anchor="w").grid(row=i + 1, column=0, sticky="w")

         entry: Union[tk.Entry, ttk.Combobox,
                      tk.Text] = tk.Entry(self.form, font=("Broadway", 12))

         if isinstance(_field[1], list):  # combobox

            entry = ttk.Combobox(self.form,
                                 values=_field[1],
                                 font=("Broadway", 12))

            entry.set("Escoge uno")
            entry.bind("<<ComboboxSelected>>",
                       lambda _: entry.selection_clear())

            if _field[2]: entry.config(state="readonly")

         elif _field[0].count("\n") > 0:  # text box

            _field[0] = _field[0][:-1]

            entry = tk.Text(self.form,
                            height=10,
                            width=20,
                            wrap=tk.WORD,
                            font=("Broadway", 12))

            if _field[1]:
               entry.insert(tk.END, _field[1])

            if _field[2]: entry.config(state="disabled")

         else:  # simple entry
            if _field[1]:
               entry.insert(0, _field[1])

            if _field[2]: entry.config(state="readonly")

         entry.grid(row=i + 1,
                    column=1,
                    columnspan=3,
                    pady=(10, 0),
                    sticky="e")

         self._entries[_field[0]] = entry

      clear_button.grid(pady=(20, 0), row=len(fields) + 3, column=0)
      save_button.grid(pady=(20, 0), row=len(fields) + 3, column=2)

   def get_typed_values(self) -> dict:
      values = {}
      for name, entry in self._entries.items():
         value = ""
         if isinstance(entry, tk.Entry):
            value = entry.get()

         if isinstance(entry, ttk.Combobox):
            value = entry.get()
            if value == "Escoge uno": value = ""

         if isinstance(entry, tk.Text):
            value = entry.get(1.0, tk.END)
            if value == "\n": value = ""
            else: value = value[:-1]

         values[name] = value

      return values

   def get_values(self, callback) -> None:
      values = self.get_typed_values()
      callback(values)

   def check_empty_values(self) -> None:
      missing_values = ""
      for name, value in self.get_typed_values().items():
         if value == "":
            missing_values += f"'{name}', "

      if missing_values != "":
         raise errors.ErrorInputEmpty(
             f"the following values are missing: {missing_values}")

   def clear_values(self) -> None:
      for entry in self._entries.values():
         if isinstance(entry, ttk.Combobox):
            entry.set("Escoge uno")
         elif isinstance(entry, tk.Text):
            entry.delete("1.0", tk.END)
         else:
            entry.delete(0, tk.END)
