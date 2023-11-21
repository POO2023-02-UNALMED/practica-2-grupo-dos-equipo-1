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

from ecart.uiMain.ventanas.processes.base import Base

"""
ChooseStore Class:

La clase ChooseStore hereda de la clase Base.

La clase tiene un atributo de clase llamado STORE_ICON, 
que representa la ruta de la imagen de un ícono de tienda.

La clase tiene otro atributo de clase llamado FORM, que es una lista que 
define los campos para el formulario de registro de la tienda.

El constructor (__init__) inicializa la clase base (Base) con un título y una descripción específicos para esta ventana.

La clase tiene un método llamado save_callback, que se ejecuta cuando se guarda
la información del formulario de registro de la tienda.

El método show_field_frame se encarga de mostrar el formulario de registro de la tienda en la interfaz de usuario.

El método add_to_grid agrega las tiendas a una cuadricula en un área de texto desplazable.

El método setup_ui configura la interfaz de usuario de la ventana, 
mostrando las tiendas existentes y permitiendo la creación de nuevas tiendas.


"""


class ChooseStore(Base):
    STORE_ICON = Utils.get_image_file("assets", "store.png")
    FORM = [
        "Nombre de la tienda", "Calle", "Carrera",
        ["Tag", Tags.get_list(), True], "Descripcion\n"
    ]

    def __init__(self, master: tk.Misc) -> None:
        self._icon = tk.PhotoImage(file=ChooseStore.STORE_ICON)

        super().__init__(
            master, "Escoger Tienda",
            "Aqui pueda cambiar de tiendas y escoger cual quiere administrar")

    def save_callback(self, form: FieldFrame, entries: dict) -> None:

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

        entries["Tag"] = Tags.get_entry_for_tag(entries["Tag"])

        ok, _ = errors.pcall(
            lambda: Admin.current.create_store(*entries.values()))
        if not ok: return

        form.destroy()
        self.setup_ui()

    def show_field_frame(self):

        self.stores_pseudoframe.destroy()
        self.add_button.destroy()

        form = FieldFrame(
            master=self,
            title="Registro de Tienda",
            fields_title="Propiedades",
            entries_title="Valores",
            fields=ChooseStore.FORM,
            save_callback=lambda input: errors.pcall(self.save_callback, form, input))
        form.pack(expand=True, fill="both")

    def add_to_grid(self, store: Store) -> None:
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
            self.add_to_grid(store)

        self.add_button = tk.Button(self,
                                    text="   Crear Tienda   ",
                                    command=self.show_field_frame)

        self.add_button.pack(pady=(0, 10))
        self.stores_pseudoframe.pack(fill="both", expand=True, padx=10)
