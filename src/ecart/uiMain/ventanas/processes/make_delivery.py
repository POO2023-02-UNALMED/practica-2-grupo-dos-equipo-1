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


class MakeDelivery(Base):
    # DELIVERY_ICON = Utils.get_file("assets", "delivery.png")  # Adjust the icon path
    FORM = [
        "Nombre del producto",
        ["Tienda", Store.get(), True],  # Assuming you have a method to get store names
        "Cantidad",
        "Dirección de entrega",
        "Notas",
    ]

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, "Realizar Entrega",
                         "Aquí puede realizar entregas y registrar los productos entregados")

    # self._icon = tk.PhotoImage(file=MakeDelivery.DELIVERY_ICON)

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

    def add_delivery_to_grid(self, delivery: Delivery) -> None:
        item = tk.Label(
            bd=5,
            padx=5,
            image=self._icon,
            text=delivery.get_product_name(),
            compound=tk.TOP,
            font=Commons.HEADER_FONT,
            relief="solid",
            bg=random.choice(
                ("lightpink", "lightyellow", "lightgreen", "lightblue", "lightsalmon")
            )
        )

        # You can define a function to handle the delivery selection similar to set_current_store
        # and bind it to the label's click event

        self.instances_pseudoframe.window_create("end", window=item)

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
