import tkinter as tk
from tkinter import ttk


class ScrollableText(tk.Text):

   def __init__(self, master=None, *args, **kwargs):

      tk.Text.__init__(self, master, *args, **kwargs)

      # create vertical scrollbar
      scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.yview)
      self.configure(yscrollcommand=scrollbar.set)

      scrollbar.pack(side="right", fill="y")
