import tkinter as tk

from ecart.uiMain.utils import Utils

from .commons import Commons
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MB


class VentanaPrincipal(tk.Frame):

   def __init__(self, master: tk.Tk, *args, **kwargs) -> None:

      super().__init__(master, *args, **kwargs)

      self.master: tk.Tk = master
      master.wm_title("Ecart - Usuario")

      self.setup_menubar()

   @staticmethod
   def start(root: tk.Tk) -> None:
      VentanaPrincipal(root, bg="lightgreen").pack(fill="both",
                                                   side="top",
                                                   expand=True)

   def regresar_inicio(self) -> None:
      should_return = MB.show("ay",
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

      MB.show("i", msg[:-1], self)

   def show_description(self) -> None:
      info = Utils.left_align("""
         1. ECart es tu plataforma para convertir tus pasatiempos creativos en oportunidades de negocio rentables.
         2. Vende tus creaciones de Crochet, Origami, Dibujo y más.
         3. Facilitamos la comercialización de tus productos ofreciéndote hosting, exposición, manejo de trámites y envío rentable.
         4. ¡Muestra tu talento, gana dinero y explora productos únicos en nuestra comunidad!

        ¡Gracias por ser parte de ECart!""")

      MB.show("i", info, self)

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

      ayuda_menu.add_command(label="Acerca de", command=self.show_authors)


      self.master.config(menu=menubar)

   def setup_ui(self):
      self.master.resizable(False, False)
      self.configure(bg="#cedae0")
      self.pack_propagate(False)

      menuBar = tk.Menu(self.master)
      self.master.option_add("*tearOff", False)
      self.master.config(menu=menuBar)

      menu1 = tk.Menu(menuBar)
      menuBar.add_cascade(label="Archivo", menu=menu1)

      # Funcion de aplicacion
      def aplicacion():
         texto = """Bienvenido a ECart.

"Empower Your Passion, Share Your Creations"

Descripción

ECart (Carrito Electrónico) es una aplicación de E-commerce para la compra y venta de productos 
creados por los usuarios. ECart permite convertir hobbies como Crochet, Origami, Dibujo, etc., en 
fuentes de ingresos rentable, facilitando la comercialización de dichos productos misceláneos 
ofreciendo hosting, exposición, manejo de trámites y Delivery rentable.
                    """
         # tk.messagebox.showinfo("Informacion de la aplicacion", texto)

      menu1.add_cascade(label="Aplicacion", command=aplicacion)

      # Funcion salir
      def salir():
         self.destroy()

      menu1.add_cascade(label="Salir", command=salir)

      menu2 = tk.Menu(menuBar)
      menuBar.add_cascade(label="Procesos y Consultas", menu=menu2)

      # Funciones
      def funcion1():
         pass

      def funcion2():
         pass

      def funcion3():
         pass

      def funcion4():
         pass

      def funcion5():
         pass

      menu2.add_cascade(label="Funcion 1", command=funcion1)
      menu2.add_cascade(label="Funcion 2", command=funcion2)
      menu2.add_cascade(label="Funcion 3", command=funcion3)
      menu2.add_cascade(label="Funcion 4", command=funcion4)
      menu2.add_cascade(label="Funcion 5", command=funcion5)

      menu3 = tk.Menu(menuBar)
      menuBar.add_cascade(label="Ayuda", menu=menu3)

      # Funcion de mostrar autores

      def mostrarAutores():
         autores = ("Autores de la aplicacion:\n\n" + "Sebas Cadavid\n" +
                    "Rodrigo\n" + "Santiago Giraldo\n" + "Angell Pimienta\n")
         # messagebox.showinfo("Autores", autores)

      menu3.add_cascade(label="Acerca de", command=mostrarAutores)

      self.master.configure(bd=2, relief="solid")

      frame = tk.Frame(self.master)
      frame.pack(anchor="center")

      bienvenida_label = tk.Label(frame,
                                  text="Bienvenido a",
                                  font=("Arial", 14, "bold"))
      bienvenida_label.pack(anchor="n", pady=10)

      self.texto_inicio = """
           ▄████████  ▄████████    ▄████████    ▄████████     ███     
          ███    ███ ███    ███   ███    ███   ███    ███ ▀█████████▄ 
          ███    █▀  ███    █▀    ███    ███   ███    ███    ▀███▀▀██ 
         ▄███▄▄▄     ███          ███    ███  ▄███▄▄▄▄██▀     ███   ▀ 
        ▀▀███▀▀▀     ███        ▀███████████ ▀▀███▀▀▀▀▀       ███     
          ███    █▄  ███    █▄    ███    ███ ▀███████████     ███     
          ███    ███ ███    ███   ███    ███   ███    ███     ███     
          ██████████ ████████▀    ███    █▀    ███    ███    ▄████▀   
            """

      # self.inicio()

      label_dibujo = tk.Label(frame,
                              text=self.texto_inicio,
                              font=("Courier", 11),
                              width=200)
      label_dibujo.pack(anchor="n")

      informacion = """

        1. ECart es tu plataforma para convertir tus pasatiempos creativos en oportunidades de negocio rentables.
        2. Vende tus creaciones de Crochet, Origami, Dibujo y más.
        3. Facilitamos la comercialización de tus productos ofreciéndote hosting, exposición, manejo de trámites y envío rentable.
        4. ¡Muestra tu talento, gana dinero y explora productos únicos en nuestra comunidad!\n
        ¡Gracias por ser parte de ECart!

        """

      info_text = tk.Label(frame,
                           text=informacion,
                           font=("Arial", 10),
                           fg="black",
                           bg="lightblue",
                           width=110)
      info_text.pack(anchor="s", pady=5)

      self.mainloop()
