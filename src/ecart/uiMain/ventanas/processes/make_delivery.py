import tkinter as tk

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
            "Aquí puede realizar entregas y registrar los productos entregados")

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

        def set_current_delivery(use_current: bool = False):
            self.current_delivery = delivery
            self.personnel_pseudoframe.destroy()
            self.header_frame.destroy()

            FORM = ["Escoje el pedido"]

            if use_current:
                if self.current_product:
                    orders_list = [str(order) for order in Admin.current.get_current_store().get_orders()]
                    FORM = [["Pedido", order] for order in orders_list]

            form = FieldFrame(master=self,
                              title="Producto",
                              fields_title="Propiedades",
                              entries_title="Valores",
                              fields=FORM,
                              save_callback=lambda input: errors.pcall(
                                  self.save_callback, form, use_current, input))
            form.pack(expand=True, fill="both")

        # put it inside the pseudo frame
        self.personnel_pseudoframe.window_create("end", window=item)

        item.bind("<Button-1>", lambda _: set_current_delivery(use_current=False))

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

        self.selected_delivery.grid(row=0, column=1, pady=(10, 0))

        self.header_frame.columnconfigure(1, weight=1)
        self.personnel_pseudoframe.pack(fill="both", expand=True, padx=10)


"""
    PROFILE_ICON = Utils.get_file("assets", "profile.png")
    FORM = [
        "Nombre del producto",
        ["Tienda", Store.get(), True],  # Assuming you have a method to get store names
        "Cantidad",
        "Dirección de entrega",
        "Notas",
    ]

    def __init__(self, master: tk.Misc) -> None:
        self._icon = tk.PhotoImage(file=MakeDelivery.PROFILE_ICON)

        super().__init__(master, "Realizar Entrega",
                         "Aquí puede realizar entregas y registrar los productos entregados")


    def save_callback(self, form: FieldFrame, entries: dict) -> None:
        form.check_empty_values()

        # Assuming you have a Delivery class with a method like create
        ok, _ = errors.pcall(
            lambda: Delivery.create.values())

        if not ok:
            return

        form.destroy()
        self.setup_ui()

    def show_field_frame(self):
        self.instances_pseudoframe.destroy()
        self.add_button.destroy()

        form = FieldFrame(
            master=self,
            title="Registro de Entrega",
            fields_title="Propiedades",
            entries_title="Valores",
            fields=MakeDelivery.FORM,
            save_callback=lambda input: errors.pcall(self.save_callback, form, input)
        )
        form.pack(expand=True, fill="both")

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
        self.header_frame.columnconfigure(1, weight=1)
        self.personnel_pseudoframe.pack(fill="both", expand=True, padx=10)


    def setup_ui(self):
        self.instances_pseudoframe = ScrollableText(
            self,
            wrap="char",
            borderwidth=0,
            highlightthickness=0,
            state="disabled",
            cursor="arrow"
        )

        for delivery in Delivery.get_all_instances():
            self.add_delivery_to_grid(delivery)

        self.add_button = tk.Button(
            self,
            text="   Realizar Entrega   ",
            command=self.show_field_frame
        )

        self.add_button.pack(pady=(0, 10))
        self.instances_pseudoframe.pack(fill="both", expand=True, padx=10)
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
        self.header_frame.columnconfigure(1, weight=1)
        self.personnel_pseudoframe.pack(fill="both", expand=True, padx=10)


    def setup_ui(self):
        self.instances_pseudoframe = ScrollableText(
            self,
            wrap="char",
            borderwidth=0,
            highlightthickness=0,
            state="disabled",
            cursor="arrow"
        )

        for delivery in Delivery.get_all_instances():
            self.add_delivery_to_grid(delivery)

        self.add_button = tk.Button(
            self,
            text="   Realizar Entrega   ",
            command=self.show_field_frame
        )

        self.add_button.pack(pady=(0, 10))
        self.instances_pseudoframe.pack(fill="both", expand=True, padx=10)
"""
