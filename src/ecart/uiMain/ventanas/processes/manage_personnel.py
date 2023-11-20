import tkinter as tk
from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.entites.admin import Admin
from ecart.gestorAplicacion.entites.delivery import Delivery
from ecart.uiMain.commons import Commons
from ecart.uiMain.helpers.field_frame import FieldFrame
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW
from ecart.uiMain.helpers.scrollable_text import ScrollableText
from ecart.uiMain.utils import Utils
import random

from ecart.uiMain.ventanas.processes.base import Base


class ManagePersonnel(Base):

   PROFILE_ICON = Utils.get_file("assets", "profile.png")

   def __init__(self, master: tk.Misc) -> None:

      self._icon = tk.PhotoImage(file=ManagePersonnel.PROFILE_ICON)
      self.current_delivery: Delivery | None = None

      super().__init__(
          master, "Administrar Personal",
          "Aqui pueda crear, borrar y actualizar a sus empleados")

   def save_callback(self, form: FieldFrame, update: bool, entries: dict):
      form.check_empty_values()

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

      ok = True

      if update:
         ok, _ = errors.pcall(lambda: self.current_delivery.update_settings(
             *entries.values()) if self.current_delivery else None)
      else:
         ok, _ = errors.pcall(
             lambda: Admin.current.create_delivery(*entries.values()))

      if not ok: return

      self.current_delivery = None

      form.destroy()
      self.setup_ui()

   def is_current_delivery(self):
      if not self.current_delivery:
         MW.show("e", "Por favor haga click en alguno de los deliveries", self)
         return False

      return True

   def create_or_update_delivery(self, use_current: bool = False):
      if use_current:
         if not self.is_current_delivery(): return

      self.personnel_pseudoframe.destroy()
      self.header_frame.destroy()

      FORM = ["Nombre", "Calle", "Carrera"]

      if use_current:
         if self.current_delivery:
            FORM = [["Nombre", self.current_delivery.get_name()],
                    ["Calle",
                     str(self.current_delivery.get_address()[0])],
                    ["Carrera",
                     str(self.current_delivery.get_address()[1])]]

      form = FieldFrame(master=self,
                        title="Delery",
                        fields_title="Propiedades",
                        entries_title="Valores",
                        fields=FORM,
                        save_callback=lambda input: errors.pcall(
                            self.save_callback, form, use_current, input))
      form.pack(expand=True, fill="both")

   def delete_delivery(self):
      if not self.is_current_delivery(): return

      perform = MW.show("ay", "Estas seguro que deseas borrar este delivery?",
                        self)

      if perform:
         ok, _ = errors.pcall(lambda: Admin.current.delete_delivery(
             self.current_delivery) if self.current_delivery else None)
         if not ok: return

         self.current_delivery = None
         self.personnel_pseudoframe.destroy()
         self.header_frame.destroy()

         self.setup_ui()

   def add_to_grid(self, delivery: Delivery) -> None:
      item = tk.Label(bd=5,
                      padx=5,
                      image=self._icon,
                      text=delivery.get_name(),
                      compound=tk.TOP,
                      font=Commons.HEADER_FONT,
                      relief="solid",
                      bg=random.choice(
                          ("lightpink", "lightyellow", "lightgreen",
                           "lightblue", "lightsalmon")))

      def set_current_delivery():
         self.selected_delivery.config(
             text=f"Delivery seleccionado: {delivery.get_name()}")
         self.current_delivery = delivery
         MW.show(
             "i",
             f"Bien! la tienda el delivery seleccionado ahora es: {delivery.get_name()}"
         )

      item.bind("<Button-1>", lambda _: set_current_delivery())

      # put it inside the pseudo frame
      self.personnel_pseudoframe.window_create("end", window=item)

   def setup_ui(self):
      self.header_frame = tk.Frame(self, bg="lightblue")
      self.header_frame.pack(fill="x", padx=10, side="top", anchor="center")

      self.personnel_pseudoframe = ScrollableText(self,
                                                  wrap="char",
                                                  borderwidth=0,
                                                  highlightthickness=0,
                                                  state="disabled",
                                                  cursor="arrow")

      admin: Admin = Admin.current

      deliveries = admin.get_current_store_deliveries()
      if deliveries is not None:
         for delivery in deliveries:
            self.add_to_grid(delivery)

      self.selected_delivery = tk.Label(self.header_frame,
                                        text="Delivery seleccionado: ninguno",
                                        font=Commons.TEXT_FONT_BI,
                                        bg="lightblue")
      add_button = tk.Button(self.header_frame,
                             text="   Crear   ",
                             command=self.create_or_update_delivery)
      delete_button = tk.Button(
          self.header_frame,
          text="   Editar Propiedades   ",
          command=lambda: self.create_or_update_delivery(True))
      edit_button = tk.Button(self.header_frame,
                              text="   Borrar   ",
                              command=self.delete_delivery)

      self.selected_delivery.grid(row=0, column=1, pady=(10, 0))
      add_button.grid(row=1, column=0, padx=(30, 0), pady=10)
      delete_button.grid(row=1, column=1, pady=10)
      edit_button.grid(row=1, column=3, padx=(0, 30), pady=10)

      self.header_frame.columnconfigure(1, weight=1)
      self.personnel_pseudoframe.pack(fill="both", expand=True, padx=10)
