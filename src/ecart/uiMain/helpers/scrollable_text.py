import tkinter as tk
from tkinter import ttk

"""
ScrollableText Class:
Esta clase representa un widget de texto con funcionalidad de desplazamiento vertical.

Crea una barra de desplazamiento vertical (ttk.Scrollbar) y la configura para
controlar el desplazamiento vertical del widget de texto (self.yview).

Asocia la barra de desplazamiento con el widget de texto llamando a self.configure(yscrollcommand=scrollbar.set).
"""


class ScrollableText(tk.Text):

    def __init__(self, master=None, *args, **kwargs):
        tk.Text.__init__(self, master, *args, **kwargs)

        # create vertical scrollbar
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
