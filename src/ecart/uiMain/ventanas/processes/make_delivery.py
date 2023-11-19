import tkinter as tk

from ecart.uiMain.ventanas.processes.base import Base
from ecart.uiMain.helpers.field_frame import FieldFrame
from ecart.uiMain.helpers.scrollable_text import ScrollableText
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW


class MakeDelivery(Base):

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master, "Hacer Delivery",
                         "Aqui puede asignar deliveries a sus empleados")

    

    def setup_ui(self):
        pass
