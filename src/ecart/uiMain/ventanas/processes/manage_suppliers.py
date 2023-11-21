import tkinter as tk
from typing import Callable
from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.entites.admin import Admin
from ecart.gestorAplicacion.merchandise.product import Product
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.gestorAplicacion.transactions.order import Order
from ecart.uiMain.commons import Commons
from ecart.uiMain.helpers.field_frame import FieldFrame
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW
from ecart.uiMain.helpers.scrollable_text import ScrollableText
from ecart.uiMain.utils import Utils
import random

from ecart.uiMain.ventanas.processes.base import Base

"""
ManageSuppliers Class:

La clase tiene atributos de clase (BASKET_ICON, BOXES_ICON, STORE_ICON) que representan las rutas 
de las imágenes de varios iconos.


El método is_current verifica si hay una orden o un producto seleccionado actualmente.

El método create_or_update_order permite al usuario crear o actualizar una orden. 
Si use_current es True, se utiliza la orden actualmente seleccionada.

El método delete_order permite al usuario borrar una orden.

El método add_to_grid agrega una etiqueta representando una orden o un producto al área de texto desplazable.

El método setup_ui configura la interfaz de usuario para la selección de tiendas.

Estos vendrian siendo los metodosnativos para esta ventana en especifico la cual se encarga de 
tener la tienda surtida de productos que pueden haberse agotado.

El método get_orders obtiene las órdenes no entregadas asociadas a la tienda actual.

El método setup_order_ui configura la interfaz de usuario para la gestión de órdenes.
"""


class ManageSuppliers(Base):
    BASKET_ICON = Utils.get_image_file("assets", "basket.png")
    BOXES_ICON = Utils.get_image_file("assets", "boxes.png")
    STORE_ICON = Utils.get_image_file("assets", "store.png")

    def __init__(self, master: tk.Misc) -> None:

        self._basket_icon = tk.PhotoImage(file=ManageSuppliers.BASKET_ICON)
        self._store_icon = tk.PhotoImage(file=ManageSuppliers.STORE_ICON)
        self._boxes_icon = tk.PhotoImage(file=ManageSuppliers.BOXES_ICON)
        self.current_order: Order | None = None
        self.current_store: Store | None = None
        self.current_product: Product | None = None

        super().__init__(
            master, "Administrar Proveedores",
            "Aqui puede distribuir recursos entre sus tiendas mediante ordenes")

    def save_callback(self, form: FieldFrame, update: bool,
                      products_dict: dict[str, int], entries: dict):
        form.check_empty_values()

        calle = entries["Calle"]
        carrera = entries["Carrera"]

        entries["Calle"] = (int(calle), int(carrera))
        entries.pop("Carrera")

        ok = True

        # switch stores
        old_current_store = Admin.current.get_current_store()
        if self.current_store:
            Admin.current.set_current_store(self.current_store)

        if update:
            ok, _ = errors.pcall(lambda: self.current_order.update_settings(
                products_dict, *entries.values()) if self.current_order else None)
        else:
            ok, _ = errors.pcall(lambda: Admin.current.create_order(
                products_dict, *entries.values()))

        # restore old store
        if self.current_store:
            if old_current_store:
                Admin.current.set_current_store(old_current_store)

        if not ok: return

        self.current_order = None

        form.destroy()
        self.left_zone.destroy()
        self.right_zone.destroy()
        self.setup_order_ui()

    def is_current(self, current_what):
        check = self.current_order
        if current_what == "current_product": check = self.current_product
        if not check:
            MW.show("e", "Por favor haga click en alguno de los elementos", self)
            return False

        return True

    def create_or_update_order(self, use_current: bool = False):
        if use_current:
            if not self.is_current("current_order"): return

        self.orders_pseudoframe.destroy()
        self.header_frame.destroy()

        FORM = []
        system_store: Store | None = Admin.current.get_current_store()
        if system_store:
            FORM = [
                ["Calle", system_store.get_address()[0], True],
                ["Carrera", system_store.get_address()[1], True],
            ]

        self.left_zone = tk.Frame(self)
        self.left_zone.place(relwidth=0.5, relheight=1)

        self.right_zone = tk.Frame(self)
        self.right_zone.place(relx=0.5, relwidth=0.5, relheight=1)

        products_dict: dict[str, int] = {}

        form = FieldFrame(
            master=self.left_zone,
            title="Orden de productos",
            fields_title="Propiedades",
            entries_title="Valores",
            fields=FORM,
            save_callback=lambda input: errors.pcall(
                self.save_callback, form, use_current, products_dict, input))

        products_list = tk.Text(self.left_zone,
                                height=10,
                                width=20,
                                wrap=tk.WORD,
                                state="disabled",
                                font=Commons.TEXT_FONT)

        header_frame = tk.Frame(self.right_zone, bg="lightblue")
        header_frame.pack(fill="x", padx=10, side="top", anchor="center")

        selected_product = tk.Label(header_frame,
                                    text="Seleccionado: ninguno",
                                    font=Commons.TEXT_FONT_BI,
                                    bg="lightblue")

        def update_products_list():
            text = ""
            for k, v in products_dict.items():
                text += f"{k}: {v}\n"

            products_list.config(state="normal")
            products_list.delete(1.0, tk.END)
            products_list.insert(tk.END, text)
            products_list.config(state="disabled")

        def update_quantity(quantity):
            if not self.is_current("current_product"): return

            if self.current_product:
                product = self.current_product.get_name()
                addition = 0

                if product in products_dict:
                    addition = products_dict[product] + quantity
                else:
                    addition = quantity

                if addition > self.current_product.get_quantity():
                    return MW.show(
                        "w",
                        "Está intentando comprar mas productos de los que hay disponibles"
                    )

                if addition <= 0:
                    if product in products_dict:
                        products_dict.pop(product)
                else:
                    products_dict[product] = addition

                update_products_list()

        if use_current:
            if self.current_order:
                products_dict = self.current_order.getProducts()
                update_products_list()

        increase_button = tk.Button(header_frame,
                                    text="   Incrementar Cantidad   ",
                                    command=lambda: update_quantity(+1))
        decrease_button = tk.Button(header_frame,
                                    text="   Disminuir Cantidad   ",
                                    command=lambda: update_quantity(-1))

        selected_product.grid(row=0, column=1, padx=20, pady=10)
        increase_button.grid(row=1, column=0, padx=(10, 0), pady=10)
        decrease_button.grid(row=1, column=2, padx=(0, 10), pady=10)

        header_frame.columnconfigure(0, weight=1)
        header_frame.columnconfigure(2, weight=1)

        products_pseudoframe = ScrollableText(self.right_zone,
                                              wrap="char",
                                              borderwidth=0,
                                              highlightthickness=0,
                                              state="disabled",
                                              cursor="arrow")

        def set_current_product(product: Product):
            selected_product.config(text=f"Seleccionado: {product.get_name()} ")
            self.current_product = product

        products = []
        if self.current_store:
            products = self.current_store.get_products()

        if products is not None:
            for product in products:
                self.add_to_grid(
                    f"{product.get_name()} ${str(product.get_price())} - #{str(product.get_quantity())}",
                    self._basket_icon, products_pseudoframe, set_current_product,
                    product)

        products_pseudoframe.pack(fill="both", expand=True, padx=10)
        form.pack(expand=True, fill="both")
        products_list.pack(expand=True, fill="both", padx=(10, 0), pady=(0, 10))

    def delete_order(self):
        if not self.is_current("current_order"): return

        perform = MW.show("ay", "Estas seguro que deseas borrar esta orden?",
                          self)

        def delete(self):

            old_current_store = Admin.current.get_current_store()
            if self.current_store:
                Admin.current.set_current_store(self.current_store)

            Admin.current.delete_order(self.current_order)

            # restore old store
            if self.current_store:
                if old_current_store:
                    Admin.current.set_current_store(old_current_store)

        if perform:
            ok, _ = errors.pcall(lambda: delete(self))
            if not ok: return

            self.current_order = None

            self.orders_pseudoframe.destroy()
            self.header_frame.destroy()

            self.setup_order_ui()

    def add_to_grid(self, text: str, icon, pseudoframe, fn: Callable,
                    *args) -> None:
        item = tk.Label(bd=5,
                        padx=5,
                        image=icon,
                        text=text,
                        compound=tk.TOP,
                        font=Commons.HEADER_FONT,
                        relief="solid",
                        bg=random.choice(
                            ("lightpink", "lightyellow", "lightgreen",
                             "lightblue", "lightsalmon")))

        item.bind("<Button-1>", lambda _: fn(*args))

        # put it inside the pseudo frame
        pseudoframe.window_create("end", window=item)

    def setup_ui(self):
        stores_pseudoframe = ScrollableText(self,
                                            wrap="char",
                                            borderwidth=0,
                                            highlightthickness=0,
                                            state="disabled",
                                            cursor="arrow")

        stores_pseudoframe.pack(fill="both", expand=True, padx=10)

        def set_current_store(store: Store):
            self.current_store = store
            MW.show(
                "i",
                f"Bien! la tienda seleccionada ahora es: {store.get_name()}\n\nSi deseas cambiar de tienda, de click de nuevo al proceso"
            )
            stores_pseudoframe.destroy()
            self.setup_order_ui()

        stores = Store.get_instances()
        if stores is not None:
            if len(stores) == 1:
                MW.show(
                    "e",
                    Utils.left_align(f"""No hay ninguna otra tienda de la que hacer pedidos.
                Tiene que haber por lo menos una otra tienda para hacer este proceso.\n\n
                Cree otra tienda en el proceso 'Escoger Tienda'""")
                )
            else:
                for store in stores:
                    if store != Admin.current.get_current_store():
                        self.add_to_grid(store.get_name(), self._store_icon,
                                         stores_pseudoframe, set_current_store,
                                         store)

    def get_orders(self):
        if self.current_store:
            orders = self.current_store.get_orders()
            final_orders = []
            curr_store = Admin.current.get_current_store()
            if curr_store:
                for order in orders:
                    if order.getDestinationAddress() == curr_store.get_address() and not order.isDelivered():
                        final_orders.append(order)

            return final_orders

    def setup_order_ui(self):
        self.header_frame = tk.Frame(self, bg="lightblue")
        self.header_frame.pack(fill="x", padx=10, side="top", anchor="center")

        self.orders_pseudoframe = ScrollableText(self,
                                                 wrap="char",
                                                 borderwidth=0,
                                                 highlightthickness=0,
                                                 state="disabled",
                                                 cursor="arrow")

        def set_current_order(order: Order):
            self.selected_order.config(
                text=
                f"Orden seleccionada: ID: {order.getId()}"
            )
            self.current_order = order
            MW.show(
                "i",
                f"Bien! la orden seleccionada ahora es: ID: {order.getId()}"
            )

        orders = self.get_orders()

        if orders is not None:
            for order in orders:
                self.add_to_grid(
                    f"ID: {order.getId()}",
                    self._boxes_icon, self.orders_pseudoframe, set_current_order,
                    order)

        self.selected_order = tk.Label(self.header_frame,
                                       text="Orden seleccionada: ninguno",
                                       font=Commons.TEXT_FONT_BI,
                                       bg="lightblue")
        add_button = tk.Button(self.header_frame,
                               text="   Crear   ",
                               command=self.create_or_update_order)
        delete_button = tk.Button(
            self.header_frame,
            text="   Editar Propiedades   ",
            command=lambda: self.create_or_update_order(True))
        edit_button = tk.Button(self.header_frame,
                                text="   Borrar   ",
                                command=self.delete_order)

        self.selected_order.grid(row=0, column=1, pady=(10, 0))
        add_button.grid(row=1, column=0, padx=(30, 0), pady=10)
        delete_button.grid(row=1, column=1, pady=10)
        edit_button.grid(row=1, column=3, padx=(0, 30), pady=10)

        self.header_frame.columnconfigure(1, weight=1)
        self.orders_pseudoframe.pack(fill="both", expand=True, padx=10)
