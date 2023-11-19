import tkinter as tk
from typing import Optional
from ecart.gestorAplicacion.entites.admin import Admin
from ecart.gestorAplicacion.merchandise.store import Store

from ecart.uiMain.utils import Utils
from ecart.uiMain.commons import Commons
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MW
from ecart.uiMain.helpers.scrollable_text import ScrollableText
from ecart.uiMain.ventanas.processes.choose_store import ChooseStore
import random


class VentanaPrincipal(tk.Frame):

   STORE_ICON = Utils.get_file("assets", "store.png")

   def __init__(self, master: tk.Tk, *args, **kwargs) -> None:

      super().__init__(master, *args, **kwargs)

      self.master: tk.Tk = master
      master.wm_title("Ecart - Usuario")

      self.setup_menubar()
      self.setup_welcome()

   @staticmethod
   def start(root: tk.Tk) -> tk.Frame:
      v = VentanaPrincipal(root, bg="lightblue")
      v.pack(fill="both", side="top", expand=True)

      return v

   def configure_process_frame(self, do_switch=False) -> None:

      new_frame = Utils._build_frame(self)

      if do_switch:
         self.process_frame.destroy()

      self.process_frame = new_frame
      self.process_frame.pack(side="top",
                              fill="both",
                              expand=True,
                              padx=10,
                              pady=10)

   BANNER = '''     _______   ________  ________  ________  _________    
     |\\  ___ \\ |\\   ____\\|\\   __  \\|\\   __  \\|\\___   ___\\  
     \\ \\   __/|\\ \\  \\___|\\ \\  \\|\\  \\ \\  \\|\\  \\|___ \\  \\_|  
      \\ \\  \\_|/_\\ \\  \\    \\ \\   __  \\ \\   _  _\\   \\ \\  \\   
       \\ \\  \\_|\\ \\ \\  \\____\\ \\  \\ \\  \\ \\  \\\\  \\|   \\ \\  \\  
        \\ \\_______\\ \\_______\\ \\__\\ \\__\\ \\__\\\\ _\\    \\ \\__\\ 
         \\|_______|\\|_______|\\|__|\\|__|\\|__|\\|__|    \\|__| 
         '''

   def regresar_inicio(self) -> None:

      should_return = MW.show("ay",
                              "Estas seguro que deseas regresar al inicio?",
                              self)
      if should_return:

         self.master.config(menu=tk.Menu())  # destroy master menu
         self.destroy()  # destroy current frame

         # avoid circular imports
         from ecart.uiMain.ventanas.inicio import VentanaInicio
         VentanaInicio(self.master, bg="lightblue").pack(fill="both",
                                                         side="top",
                                                         expand=True)

   def show_authors(self) -> None:

      msg = "Autores de la aplicacion:\n\n"
      for a in Commons.AUTHORS.values():

         msg += f"🤵 {a[0]}: {a[2]}\n"

      MW.show("i", msg[:-1], self)

   def show_description(self) -> None:

      info = Utils.left_align("""
         1. ECart es tu plataforma para convertir tus pasatiempos creativos en oportunidades de negocio rentables.
         2. Vende tus creaciones de Crochet, Origami, Dibujo y más.
         3. Facilitamos la comercialización de tus productos ofreciéndote hosting, exposición, manejo de trámites y envío rentable.
         4. ¡Muestra tu talento, gana dinero y explora productos únicos en nuestra comunidad!

        ¡Gracias por ser parte de ECart!""")

      MW.show("i", info, self)

   def setup_upper_zone(self) -> None:

      banner_label = tk.Label(self.upper_zone,
                              text=VentanaPrincipal.BANNER,
                              font=Commons.HEADER_FONT,
                              bg="lightsteelblue")

      banner_label.pack(side="bottom",
                        expand=True,
                        padx=10,
                        pady=10,
                        fill="both")

   def setup_lower_zone(self) -> None:
      f = ChooseStore(self.lower_zone)
      f.pack(expand=True, fill="both")

   def setup_welcome(self) -> None:
      self.configure_process_frame()

      self.upper_zone = tk.Frame(self.process_frame)
      self.upper_zone.place(relwidth=1, relheight=0.35)

      self.lower_zone = tk.Frame(self.process_frame, bg="lightpink")
      self.lower_zone.place(rely=0.35, relwidth=1, relheight=0.65)

      self.setup_upper_zone()
      self.setup_lower_zone()

   def pick_process(self, Process) -> None:

      if not Admin.current.get_current_store():
         MW.show("w", "Necesita primero escoger una tienda para administrar")
         return

      self.configure_process_frame(True)
      f = Process(self.process_frame)

      color = random.choice(
          ("pink", "yellow", "green", "blue", "salmon", "violet"))

      title_frame = tk.Frame(self.process_frame,
                             highlightthickness=3,
                             highlightbackground=color)
      description_frame = tk.Frame(self.process_frame,
                                   highlightthickness=3,
                                   highlightbackground=color)


      store: Store | None = Admin.current.get_current_store()

      title = tk.Label(title_frame, text=f"{f.title}\n({store.get_name() if store else ''})", font=Commons.HEADER_FONT)
      description = tk.Label(description_frame,
                             text=f.description,
                             font=Commons.DESC_FONT)


      title_frame.pack(pady=(10, 5))
      description_frame.pack(pady=(0, 10))

      title.pack(expand=True, fill="both")
      description.pack(expand=True, fill="both")
      f.pack(expand=True, fill="both")

   def setup_menubar(self) -> None:

      menubar = tk.Menu(self.master)

      archivo_menu = tk.Menu(menubar, tearoff=False)
      procesos_menu = tk.Menu(menubar, tearoff=False)
      ayuda_menu = tk.Menu(menubar, tearoff=False)

      menubar.add_cascade(label="Archivo", menu=archivo_menu)
      menubar.add_cascade(label="Procesos y Consultas", menu=procesos_menu)
      menubar.add_cascade(label="Ayuda", menu=ayuda_menu)

      archivo_menu.add_command(label="Aplicación",
                               command=self.show_description)
      archivo_menu.add_command(label="Salir", command=self.regresar_inicio)

      # se supone que los 'commands' van a ser de la forma:
      # command=lambda: self.configure_process_frame(Process1.start())
      procesos_menu.add_command(label="Choose Store",
                                command=lambda: self.pick_process(ChooseStore))
      procesos_menu.add_command(label="Funcion 2", command=self.show_authors)
      procesos_menu.add_command(label="Funcion 3", command=self.show_authors)
      procesos_menu.add_command(label="Funcion 4", command=self.show_authors)
      procesos_menu.add_command(label="Funcion 5", command=self.show_authors)

      ayuda_menu.add_command(label="Acerca de", command=self.show_authors)

      self.master.config(menu=menubar)
