import tkinter as tk
from ecart.gestorAplicacion.entites.admin import Admin
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.uiMain.commons import Commons
from ecart.uiMain.helpers.field_frame import FieldFrame
from ecart.uiMain.helpers.scrollable_text import ScrollableText
from ecart.uiMain.utils import Utils
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW
import ecart.gestorAplicacion.errors as errors
import random


class ChooseStore(tk.Frame):

   STORE_ICON = Utils.get_file("assets", "store.png")
   FORM = [
       "Nombre de la tienda", "Calle", "Carrera",
       ["Tag", Tags.get_list(), True], "Descripcion\n"
   ]

   def __init__(self, master: tk.Misc) -> None:
      super().__init__(master)

      self.master = master

      self._icon = tk.PhotoImage(file=ChooseStore.STORE_ICON)
      self.title = "Escoger Tienda"
      self.description = "Aqui pueda cambiar de tiendas y escoger cual quiere administrar"

      self.setup_ui()

   def show_field_frame(self):

      self.stores_pseudoframe.destroy()
      self.add_button.destroy()

      def save_callback(entries: dict):
         missing_values = ""
         for name, value in entries.items():
            if value == "":
               missing_values += f"'{name}', "

         if missing_values != "":
            raise errors.ErrorInputEmpty(
                f"the following values are missing: {missing_values}")

         calle = entries["Calle"]
         carrera = entries["Carrera"]

         try:
            entries["Calle"] = (int(calle), int(carrera))
         except Exception:
            errors.display(
                errors.ErrorInputType(
                    "Calle y Carrera solo pueden recibir numeros"))
            return

         entries.pop("Carrera")

         entries["Tag"] = Tags.get_entry_for_tag(entries["Tag"])

         ok, _ = errors.pcall(
             lambda: Admin.current.create_store(*entries.values()))
         if not ok: return

         form.destroy()
         self.setup_ui()

      form = FieldFrame(
          master=self,
          title="Registro de Tienda",
          fields_title="Propiedades",
          entries_title="Valores",
          fields=ChooseStore.FORM,
          save_callback=lambda input: errors.pcall(save_callback, input))
      form.pack(expand=True, fill="both")

   def add_store_to_grid(self, store: Store) -> None:
      item = tk.Label(bd=5,
                      padx=5,
                      image=self._icon,
                      text=store.get_name(),
                      compound=tk.TOP,
                      font=Commons.HEADER_FONT,
                      relief="solid",
                      bg=random.choice(
                          ("lightpink", "lightyellow", "lightgreen",
                           "lightblue", "lightsalmon")))

      def set_current_store():
         Admin.current.set_current_store(store)
         MW.show(
             "i",
             f"Bien! la tienda actual ahora es: {store.get_name()}\nYa puedes acceder a los otros procesos"
         )

      item.bind("<Button-1>", lambda _: set_current_store())

      # put it inside the pseudo frame
      self.stores_pseudoframe.window_create("end", window=item)

   def setup_ui(self):

      self.stores_pseudoframe = ScrollableText(self,
                                               wrap="char",
                                               borderwidth=0,
                                               highlightthickness=0,
                                               state="disabled",
                                               cursor="arrow")

      for store in Store.get():
         self.add_store_to_grid(store)

      self.add_button = tk.Button(self,
                                  text="   Create Store   ",
                                  command=self.show_field_frame)

      self.add_button.pack(pady=(0, 10))
      self.stores_pseudoframe.pack(fill="both", expand=True, padx=10)
