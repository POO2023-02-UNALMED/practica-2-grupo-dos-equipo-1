import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from ecart.uiMain.ventanas.processes.base import Base
from ecart.uiMain.helpers.scrollable_text import ScrollableText


class AnalysePerformance(Base):

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(
            master, "Analizar Rendimiento",
            "Aqui puede ver como ha sido en rendimiento de su negocio")

    def crear_grafica(self):
        # Datos de ejemplo
        tiempo = [1, 2, 3, 4, 5]
        ventas = [100, 120, 90, 150, 110]

        # Crear una figura de matplotlib
        fig = Figure(figsize=(5, 4), dpi=100)
        plot = fig.add_subplot(1, 1, 1)
        plot.plot(tiempo, ventas, marker='o', linestyle='-')
        plot.set_xlabel('Tiempo')
        plot.set_ylabel('Ventas')
        plot.set_title('Cantidad Histórica vs Ventas')

        # Crear lienzo de Tkinter para la figura
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

        # Desactivar el botón después de crear la gráfica
        self.add_button.config(state="disabled")

    def setup_ui(self):
        ScrollableText(
            self,
            wrap="char",
            borderwidth=0,
            highlightthickness=0,
            state="disabled",
            cursor="arrow"
        )
        self.add_button = tk.Button(
            self,
            text="   Mostrar Grafica   ",
            command=self.crear_grafica
        )

        self.add_button.pack(pady=(0, 10))
        self.pack(side="bottom", fill="both", padx=10)
