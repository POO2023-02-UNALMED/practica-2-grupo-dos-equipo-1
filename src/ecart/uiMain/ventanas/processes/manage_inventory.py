import tkinter as tk
from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.entites.admin import Admin
from ecart.gestorAplicacion.merchandise.product import Product
from ecart.uiMain.commons import Commons
from ecart.uiMain.helpers.field_frame import FieldFrame
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW
from ecart.uiMain.helpers.scrollable_text import ScrollableText
from ecart.uiMain.utils import Utils
import random
from ecart.uiMain.ventanas.processes.base import Base

"""
ManageInventory Class:

La clase ManageInventory hereda de la clase Base.
La clase tiene un atributo de clase llamado FRUIT_ICON, que representa el ícono de una frutas.

De la misma forma como en todas lasc las clases que heredan de Base estas inicializan con el titul y la descripcion 
y también inicializa la variable current_product que se utiliza para administrar el inventario de productos.


La clase tiene un método llamado save_callback, que se ejecuta cuando se guarda la información del formulario de producto.

El método is_current_product verifica si hay un producto seleccionado actualmente.

El método create_or_update_product permite al usuario crear o actualizar un producto. Si use_current es True, 
se utiliza el producto actualmente seleccionado.

El método delete_product permite al usuario borrar un producto.

El método add_to_grid agrega una etiqueta representando un producto a un área de texto desplazable.

El método setup_ui configura la interfaz de usuario de la ventana, mostrando productos disponibles y permitiendo crear, 
actualizar o borrar productos.



"""


class ManageInventory(Base):
    FRUIT_ICON = Utils.get_file("assets", "fruit.png")

    def __init__(self, master: tk.Misc) -> None:

        self._icon = tk.PhotoImage(file=ManageInventory.FRUIT_ICON)
        self.current_product: Product | None = None

        super().__init__(master, "Administrar Inventario",
                         "Aqui pueda crear, borrar y actualizar productos")

    def save_callback(self, form: FieldFrame, update: bool, entries: dict):
        form.check_empty_values()

        price = entries["Precio"]
        quantity = entries["Cantidad"]

        try:
            entries["Precio"] = float(price)
            entries["Cantidad"] = int(quantity)
        except Exception:
            errors.display(
                errors.ErrorInputType(
                    "Precio y cantidad solo pueden recibir numeros"))
            return

        ok = True

        if update:
            ok, _ = errors.pcall(lambda: self.current_product.update_settings(
                Admin.current.get_current_store_products(), *entries.values())
            if self.current_product else None)
        else:
            ok, _ = errors.pcall(
                lambda: Admin.current.create_product(*entries.values()))

        if not ok: return

        self.current_product = None

        form.destroy()
        self.setup_ui()

    def is_current_product(self):
        if not self.current_product:
            MW.show("e", "Por favor haga click en alguno de los productos", self)
            return False

        return True

    def create_or_update_product(self, use_current: bool = False):
        if use_current:
            if not self.is_current_product(): return

        self.products_pseudoframe.destroy()
        self.header_frame.destroy()

        FORM = ["Nombre", "Precio", "Cantidad", "Descripcion\n"]

        if use_current:
            if self.current_product:
                FORM = [["Nombre", self.current_product.get_name()],
                        ["Precio", str(self.current_product.get_price())],
                        ["Cantidad",
                         str(self.current_product.get_quantity())],
                        [
                            "Descripcion\n",
                            str(self.current_product.get_description())
                        ]]

        form = FieldFrame(master=self,
                          title="Producto",
                          fields_title="Propiedades",
                          entries_title="Valores",
                          fields=FORM,
                          save_callback=lambda input: errors.pcall(
                              self.save_callback, form, use_current, input))
        form.pack(expand=True, fill="both")

    def delete_product(self):
        if not self.is_current_product(): return

        perform = MW.show("ay", "Estas seguro que deseas borrar este product?",
                          self)

        if perform:
            ok, _ = errors.pcall(lambda: Admin.current.delete_product(
                self.current_product) if self.current_product else None)
            if not ok: return

            self.current_product = None
            self.products_pseudoframe.destroy()
            self.header_frame.destroy()

            self.setup_ui()

    def add_to_grid(self, product: Product) -> None:
        item = tk.Label(bd=5,
                        padx=5,
                        image=self._icon,
                        text=product.get_name(),
                        compound=tk.TOP,
                        font=Commons.HEADER_FONT,
                        relief="solid",
                        bg=random.choice(
                            ("lightpink", "lightyellow", "lightgreen",
                             "lightblue", "lightsalmon")))

        def set_current_product():
            self.selected_product.config(
                text=f"Producto seleccionado: {product.get_name()}")
            self.current_product = product
            MW.show(
                "i",
                f"Bien! la tienda el product seleccionado ahora es: {product.get_name()}"
            )

        item.bind("<Button-1>", lambda _: set_current_product())

        # put it inside the pseudo frame
        self.products_pseudoframe.window_create("end", window=item)

    def setup_ui(self):
        self.header_frame = tk.Frame(self, bg="lightblue")
        self.header_frame.pack(fill="x", padx=10, side="top", anchor="center")

        self.products_pseudoframe = ScrollableText(self,
                                                   wrap="char",
                                                   borderwidth=0,
                                                   highlightthickness=0,
                                                   state="disabled",
                                                   cursor="arrow")

        admin: Admin = Admin.current

        products = admin.get_current_store_products()

        if products is not None:
            for product in products:
                self.add_to_grid(product)

        self.selected_product = tk.Label(self.header_frame,
                                         text="Producto seleccionado: ninguno",
                                         font=Commons.TEXT_FONT_BI,
                                         bg="lightblue")
        add_button = tk.Button(self.header_frame,
                               text="   Crear   ",
                               command=self.create_or_update_product)
        delete_button = tk.Button(
            self.header_frame,
            text="   Editar Propiedades   ",
            command=lambda: self.create_or_update_product(True))
        edit_button = tk.Button(self.header_frame,
                                text="   Borrar   ",
                                command=self.delete_product)

        self.selected_product.grid(row=0, column=1, pady=(10, 0))
        add_button.grid(row=1, column=0, padx=(30, 0), pady=10)
        delete_button.grid(row=1, column=1, pady=10)
        edit_button.grid(row=1, column=3, padx=(0, 30), pady=10)

        self.header_frame.columnconfigure(1, weight=1)
        self.products_pseudoframe.pack(fill="both", expand=True, padx=10)
