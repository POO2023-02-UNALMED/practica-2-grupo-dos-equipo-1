from tkinter import *
from tkinter import messagebox


class VentPrincipal(Tk):
    def __init__(self):
        super().__init__()
        self.title("Ecart - Usuario")
        self.resizable(False, False)
        self.geometry("865x480+400+200")
        self.configure(bg="#cedae0")
        self.pack_propagate(False)

        menuBar = Menu(self)
        self.option_add("*tearOff", False)
        self.config(menu=menuBar)

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
            messagebox.showinfo(
                "Informacion de la aplicacion", texto
            )

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

        class Author:
            def __init__(self, name, semester, info):
                self.name = name
                self.semester = semester
                self.info = info

        authors = {
            "angell": Author("Angell", "3", "Desarrollador de software apasionado"),
            "sebastian": Author("Sebastian", "3", "Desarrollador de software apasionado"),
            "rodrigo": Author("Rodrigo", "3", "Desarrollador de software apasionado"),
            "santiago": Author("Santiago", "3", "Desarrollador de software apasionado")
        }

        def mostrar_autores():
            mensaje = ""
            for autor in authors.values():
                mensaje += f"Nombre: {autor.name}\nSemestre: {autor.semester}\nInformación: {autor.info}\n\n"

            if mensaje:
                messagebox.showinfo("Información de integrantes", mensaje)
            else:
                messagebox.showwarning("Error", "No se encontró información de los integrantes")

        menu3.add_cascade(label="Acerca de", command=mostrar_autores)

        frame = Frame(self)
        frame.pack(anchor="center", expand=True)
        """
        bienvenida_label = Label(frame, text=inicio, font=("Arial", 14),
                                 fg="white", bg="#085870")
        bienvenida_label.pack(padx=10, pady=10)
        """

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

        self.inicio()

    def inicio(self):
        # Widget Text para mostrar el texto formateado
        texto = Text(self, font=("Courier", 10), height=100)
        texto.insert(END, self.texto_inicio)
        texto.pack()

        self.mainloop()
"""
    def mostrar_texto_bienvenida(self):
        # Crear una etiqueta para el texto de bienvenida
        texto_bienvenida = 
        ¡Bienvenido a ECart!

        ECart es tu plataforma para convertir tus pasatiempos creativos en oportunidades de negocio rentables. Aquí puedes vender tus creaciones de Crochet, Origami, Dibujo y más. Facilitamos la comercialización de tus productos misceláneos ofreciéndote hosting, exposición, manejo de trámites y envío rentable.

        ¡Comienza a mostrar tu talento y gana dinero con tus habilidades creativas! Explora, compra y vende productos únicos en nuestra comunidad.

        ¡Gracias por ser parte de ECart!


        # Crear una etiqueta para mostrar el texto de bienvenida centrado
        label_bienvenida = tk.Label(self, text=texto_bienvenida, font=("Arial", 12), bg="#cedae0", justify="center")
        label_bienvenida.pack()
"""

# Probar
if __name__ == "__main__":
    ventana_principal = VentPrincipal()
