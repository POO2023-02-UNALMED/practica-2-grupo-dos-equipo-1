import tkinter as tk
from ecart.gestorAplicacion import errors
from ecart.gestorAplicacion.entites.admin import Admin
from ecart.gestorAplicacion.merchandise.store import Store
from ecart.uiMain.helpers.field_frame import FieldFrame
from ecart.gestorAplicacion.merchandise.tags import Tags
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW

from ecart.uiMain.ventanas.processes.base import Base

"""
UpdateSettings Class:

En esta clase se buscaba la implementacion de configurar tiendas ya creadas para que los usuarios
tuvieran la posibilidad de que en dado caso que quisieran actualizar su tienda pudieran hacerlo 

El constructor (__init__) toma dos parámetros: master y who. 
who especifica si se están actualizando las configuraciones de una tienda ("store") o de un administrador ("admin").

El método save_callback se ejecuta cuando se guarda la información del formulario de configuración. 
Realiza la validación de entrada y actualiza las configuraciones según sea necesario.

El método setup_ui configura la interfaz de usuario para la actualización de configuraciones. 
Crea un formulario (FieldFrame) con campos específicos según si se está actualizando una tienda o un administrador.

"""


class UpdateSettings(Base):

    def __init__(self, master: tk.Misc, who: str) -> None:

        self.who = who

        super().__init__(master, "Actualizar Configuraciones",
                         "Aqui puede actualizar sus configuraciones")

    def save_callback(self, form: FieldFrame, entries: dict, admin: Admin, store: Store):
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

        if "Tag" in entries:
            entries["Tag"] = Tags.get_entry_for_tag(entries["Tag"])

        def update() -> str:
            if self.who == "store":
                return store.update_settings(*entries.values())
            else:
                return admin.update_settings(*entries.values())

        ok, _ = errors.pcall(update)
        if not ok: return

    def setup_ui(self):

        admin: Admin = Admin.current
        store: Store | None = admin.get_current_store()

        FORM_STORE = []

        if store:
            FORM_STORE = [
                ["Nombre de la tienda", store.get_name()],
                ["Calle", str(store.get_address()[0])],
                ["Carrera", str(store.get_address()[1])],
                ["Tag", Tags.get_list(), True],
                ["Descripcion\n", store.get_description()]
            ]

        FORM_ADMIN = [
            ["Nombre", "Administrador", True],
            ["Calle", str(admin.get_address()[0])],
            ["Carrera", str(admin.get_address()[1])]
        ]

        form = FieldFrame(
            master=self,
            title=f"Ajustes de {'Tienda' if self.who == 'store' else 'Administrador'}",
            fields_title="Propiedades",
            entries_title="Valores",
            fields=FORM_STORE if self.who == "store" else FORM_ADMIN,
            save_callback=lambda input: errors.pcall(self.save_callback, form, input, admin, store)
        )

        form.pack(expand=True, fill="both")
