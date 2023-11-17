import tkinter as tk
from tkinter import Menu, messagebox, Frame, Text, END, Label, ttk


class VentanaPrincipal(tk.Frame):

   def __init__(self, master: tk.Tk, *args, **kwargs) -> None:
      super().__init__(master, *args, **kwargs)
      self.master: tk.Tk = master
      master.wm_title("Ecart - Usuario")

      self.configure_ui()

   def configure_ui(self):
      self.master.resizable(False, False)
      self.configure(bg="#cedae0")
      self.pack_propagate(False)

      menuBar = Menu(self.master)
      self.master.option_add("*tearOff", False)
      self.master.config(menu=menuBar)

      menu1 = Menu(menuBar)
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
         messagebox.showinfo("Informacion de la aplicacion", texto)

      menu1.add_cascade(label="Aplicacion", command=aplicacion)

      # Funcion salir
      def salir():
         self.destroy()

      menu1.add_cascade(label="Salir", command=salir)

      menu2 = Menu(menuBar)
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

      menu3 = Menu(menuBar)
      menuBar.add_cascade(label="Ayuda", menu=menu3)

      # Funcion de mostrar autores

      def mostrarAutores():
         autores = ("Autores de la aplicacion:\n\n" + "Sebas Cadavid\n" +
                    "Rodrigo\n" + "Santiago Giraldo\n" + "Angell Pimienta\n")
         messagebox.showinfo("Autores", autores)

      menu3.add_cascade(label="Acerca de", command=mostrarAutores)

      self.master.configure(bd=2, relief="solid")

      frame = Frame(self.master)
      frame.pack(anchor="center")

      bienvenida_label = Label(frame,
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

      label_dibujo = Label(frame,
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

      info_text = Label(frame,
                        text=informacion,
                        font=("Arial", 10),
                        fg="black",
                        bg="lightblue",
                        width=110)
      info_text.pack(anchor="s", pady=5)

      self.mainloop()
