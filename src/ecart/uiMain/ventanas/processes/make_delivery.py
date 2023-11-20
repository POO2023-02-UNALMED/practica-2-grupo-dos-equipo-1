import tkinter as tk
from ecart.gestorAplicacion.transactions.order import Order

from ecart.uiMain.ventanas.processes.base import Base
from ecart.uiMain.helpers.field_frame import FieldFrame
from ecart.uiMain.helpers.scrollable_text import ScrollableText
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW
from ecart.uiMain.utils import Utils
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.entites.delivery import Delivery
from ecart.uiMain.ventanas.processes.base import Base
import ecart.gestorAplicacion.errors as errors
from ecart.uiMain.commons import Commons
from ecart.gestorAplicacion.entites.admin import Admin
import random


class MakeDelivery(Base):
   PROFILE_ICON = Utils.get_file("assets", "profile.png")

   def __init__(self, master: tk.Misc) -> None:

      self._icon = tk.PhotoImage(file=MakeDelivery.PROFILE_ICON)
      self.current_delivery: Delivery | None = None

      super().__init__(
          master, "Realizar Entrega",
          "Aquí puede asignar ordenes a tus deliveries")

   def save_callback(self, form: FieldFrame, entries: dict):
      form.check_empty_values()

      curr_store = Admin.current.get_current_store()
      if curr_store:
         order: Order = curr_store.get_order_by_id(int(entries["Orden"]))

         ok, _ = errors.pcall(
             lambda: self.current_delivery.deliver(order) if self.current_delivery else None)

         if not ok: return

      self.current_delivery = None

      form.destroy()
      self.setup_ui()

   def is_current_delivery(self):
      if not self.current_delivery:
         MW.show("e", "Por favor haga click en alguno de los deliveries", self)
         return False

      return True

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
         self.current_delivery = delivery

         orders: list[Order] = []
         curr_store = Admin.current.get_current_store()
         if curr_store:
            for order in curr_store.get_orders():
               if not order.is_delivered():
                  orders.append(order)

         if len(orders) == 0:
            return MW.show("w", "No hay ordenes que entregar.\n\nCree ordenes en el proceso 'Administrar Ordenes'")

         self.personnel_pseudoframe.destroy()
         self.header_frame.destroy()

         order_ids = []
         for order in orders:
            order_ids.append(order.getId())


         FORM = [
            ["Orden", order_ids, True]
         ]

         form = FieldFrame(master=self,
                           title="Producto",
                           fields_title="Propiedades",
                           entries_title="Valores",
                           fields=FORM,
                           save_callback=lambda input: errors.pcall(
                               self.save_callback, form, input))
         form.pack(expand=True, fill="both")

      # put it inside the pseudo frame
      self.personnel_pseudoframe.window_create("end", window=item)

      item.bind("<Button-1>", lambda _: set_current_delivery())

   def setup_ui(self):
      self.header_frame = tk.Frame(self, bg="lightblue")
      self.header_frame.pack(fill="x", padx=10, side="top", anchor="center")
      instructions = tk.Label(self.header_frame, text="Haga click al Delivery que le gustaria asignar una orden", font=Commons.TEXT_FONT, bg="lightblue")

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

      instructions.grid(row=0, column=1, pady=10)

      self.header_frame.columnconfigure(1, weight=1)
      self.personnel_pseudoframe.pack(fill="both", expand=True, padx=10)
