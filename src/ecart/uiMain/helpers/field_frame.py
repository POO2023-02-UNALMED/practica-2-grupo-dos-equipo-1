import tkinter as tk
from typing import Any, Union
from tkinter import ttk

from ecart.uiMain.commons import Commons


class FieldFrame(tk.Frame):
   """ Example call:
      
      ff = FieldFrame(
         some_window,
         "Fields",
         "Entries"
         [
            "Name",
            ("Opinion", "no opinion"),
            ("ID", existing_id, True), # disable the field
            ("Colors", ["red", "green", "blue"])
         ]
      )

      (<field name>, <value(s)>, disable?)
      (mandatory, defaults: None, default: false)
   """

   def __init__(self, master: tk.Misc, title: str, fieldsTitle: str,
                entriesTitle: str, fields: list, *args, **kwargs):
      super().__init__(master, *args, **kwargs)

      if title:
         tk.Label(self, text=title, font=Commons.TEXT_FONT_BOLD).pack(pady=10)

      self.form = tk.Frame(self, bg="lightblue")
      self.form.pack(expand=True, side="top", anchor="center")
      self.form.grid_columnconfigure(0, pad=20)

      clear_button = tk.Button(self.form, text="   Borrar   ", command=self.clear)
      save_button = tk.Button(self.form, text="   Guardar   ", command=self.save)

      if fieldsTitle:
         tk.Label(self.form, text=fieldsTitle,
                  font=Commons.TEXT_FONT_BOLD).grid(row=0, column=0)

      if entriesTitle:
         tk.Label(self.form, text=entriesTitle,
                  font=Commons.TEXT_FONT_BOLD).grid(row=0, column=1)

      self._entries: dict[str, Union[tk.Entry, ttk.Combobox]] = {}

      for i, field in enumerate(fields, start=2):
         _field = list(field)

         if isinstance(field, str): _field[0:] = [field]
         else: _field = field

         if len(_field) < 2: _field.append(None)
         if len(_field) < 3: _field.append(False)

         tk.Label(self.form, text=_field[0], justify="left",
                  anchor="w").grid(row=i + 1, column=0, sticky="w")

         entry: Union[tk.Entry, ttk.Combobox] = tk.Entry(self.form)

         if isinstance(_field[1], list):
            entry = ttk.Combobox(self.form, values=_field[1])

            entry.set("Escoge uno")
            entry.grid(row=i + 1, column=1, sticky="e")
            entry.bind("<<ComboboxSelected>>",
                       lambda _: entry.selection_clear())
         else:
            entry.grid(row=i + 1, column=1, sticky="e")

            if _field[1]:
               entry.insert(0, _field[1])

         if _field[2]:
            entry.config(state="readonly")

         self._entries[_field[0]] = entry

      clear_button.grid(pady=(20, 0), row=len(fields) + 3, column=0)
      save_button.grid(pady=(20, 0), row=len(fields) + 3, column=1)

   def save(self) -> None:
      pass

   def clear(self) -> None:
      for entry in self._entries.values():
         if isinstance(entry, tk.Entry):
            entry.delete(0, tk.END)
         else:
            entry.set("")
