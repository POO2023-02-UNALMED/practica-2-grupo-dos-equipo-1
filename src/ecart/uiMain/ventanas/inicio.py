import tkinter as tk
from typing import Tuple

from ecart.uiMain.utils import Utils
from .principal import VentanaPrincipal
from ecart.uiMain.commons import Commons
from ecart.uiMain.helpers.msgbox_wrapper import MsgboxWrapper as MB

"""
Esta la ventana de inicio la cual cuenta con:


Inicialización (__init__):
Configura la ventana principal (master) y establece el título de la ventana.
Llama a varios métodos para configurar la barra de menú, el área derecha e izquierda de la ventana.


start (Método Estático):
Método estático para crear una instancia de VentanaInicio y empaquetarla en la ventana principal (root).


show_description (Método):
Muestra la descripción del sistema en el área de la ventana, ocultando otras secciones.
Permite al usuario regresar a la visualización de imágenes del proyecto.


exit_program (Método):
Muestra un cuadro de diálogo de confirmación y sale de la aplicación si el usuario confirma.


setup_menubar (Método):
Configura la barra de menú en la parte superior de la ventana con opciones como "Inicio", "Salir" y "Descripción"


setup_right_frameholder (Método):
Configura el área derecha de la ventana, que contiene información sobre los autores del proyecto y sus imágenes.
ademas de permitirle al usuario navegar entre las distintas biografías de los autores


setup_left_frameholder (Método):
Configura el área izquierda de la ventana, que contiene un mensaje de bienvenida
y un área para mostrar imágenes del proyecto.


configure_project_images (Método):
Configura un área para mostrar imágenes del proyecto en la parte inferior izquierda de la ventana.

Permite al usuario navegar entre las imágenes del proyecto al pasar el ratón 
sobre el área y hacer clic en el botón "Ingresar".



"""


class VentanaInicio(tk.Frame):

    def __init__(self, master: tk.Tk, *args, **kwargs) -> None:

        super().__init__(master, *args, **kwargs)
        self.master: tk.Tk = master

        master.wm_title("Ecart - Inicio")

        self.setup_menubar()
        self.setup_right_frameholder()
        self.setup_left_frameholder()

    @staticmethod
    def start(root: tk.Tk) -> tk.Frame:
        v = VentanaInicio(root)
        v.pack(fill="both", side="top", expand=True)

        return v

    def show_description(self) -> None:

        self.project_images_frame.destroy()
        self.project_ingresar_button.destroy()

        tmp_frame = tk.Frame(self.p4)
        tmp_frame.pack(expand=True, fill="both")

        system_description = Utils._build_label(
            tmp_frame,
            text=Utils.left_align("""📃 Descripcion del sistema 📚


            Gracias a nutra interfaz intuitiva y funcionalidades avanzadas,
            Ecart le permite establecer y personalizar sus propias tiendas
            en línea, de manera sencilla y eficiente. Brindando las
            siguientes funcionalidades:

              1. Crear y administrar tiendas
              2. Contratar personal
              3. Hacer entregas
              4. Sugerir productos
              5. Gestionar ingresos
            """),
            font=Commons.TEXT_FONT)

        system_description.pack(expand=True, fill="both")

        def _destroy() -> None:
            tmp_frame.destroy()
            self.configure_project_images()

        regresar_button = tk.Button(tmp_frame, text="Regresar", command=_destroy)
        regresar_button.pack(side="bottom", padx=10, pady=10)

    def exit_program(self) -> None:

        should_exit = MB.show("ay",
                              "Estas seguro que deseas salir de la aplicación?")
        if should_exit:
            self.master.destroy()

    def setup_menubar(self) -> None:

        menubar = tk.Menu(self.master)

        inicio_menu = tk.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Inicio", menu=inicio_menu)

        inicio_menu.add_command(label="Salir", command=self.exit_program)
        inicio_menu.add_command(label="Descripción",
                                command=self.show_description)

        self.master.config(menu=menubar)

    def setup_right_frameholder(self) -> None:

        right_zone = tk.Frame(self)
        right_zone.place(relx=0.5, relwidth=0.5, relheight=1)

        # holds all the actual frames
        p2 = Utils._build_frame(right_zone)
        p2.pack(expand=True, fill="both", padx=(5, 10), pady=10)

        authors = Commons.AUTHORS

        names = Utils.iterate_inf(authors.keys())
        biographies = Utils.iterate_inf(authors.values())

        # (P5) Authors biographies
        biography_frame = Utils._build_frame(p2)
        biography_frame.pack(side="top", padx=10, pady=10, fill="x")

        current_biography = ""

        biography_display = Utils._build_label(biography_frame,
                                               text=current_biography)
        biography_display.pack(expand=True, fill="x", padx=10, pady=10)

        def set_next_biography() -> None:

            author: Tuple = next(biographies)

            biography_display.config(
                text=Utils.left_align(f"""Hoja de Vida de los Autores
            (haga click)

            🗯️ Nombre: {author[0]}
            📙 Semestre: {author[1]}
            📃 Informacion: {author[2]}"""))

        set_next_biography()

        # (P6) Authors images
        p6 = Utils._build_frame(p2)
        p6.pack(side="bottom", expand=True, padx=10, pady=10, fill="both")

        images_frame = tk.Frame(p6)
        images_frame.pack(expand=True)

        self.current_images = [
            tk.PhotoImage(file=img_path)
            for img_path in Utils.get_images("authors", next(names))
        ]
        images_displays = [
            tk.Label(images_frame, text="hello", image=image)
            for image in self.current_images
        ]

        for i, display in enumerate(images_displays):
            row, col = divmod(i, 2)
            display.grid(row=row,
                         column=col,
                         padx=(5, 0),
                         pady=(5, 0),
                         sticky="nsew")

        # configure row and column weights to center the cluster
        for i in range(2):
            images_frame.grid_rowconfigure(i, weight=1)
            images_frame.grid_columnconfigure(i, weight=1)

        def set_next_images() -> None:
            next_images = Utils.get_images("authors", next(names))
            for i in range(4):
                self.current_images[i].config(file=next_images[i])

        # putting it all together
        def set_next_author() -> None:
            set_next_biography()
            set_next_images()

        biography_display.bind("<Button-1>", lambda _: set_next_author())

    def setup_left_frameholder(self) -> None:

        left_zone = tk.Frame(self)
        left_zone.place(relwidth=0.5, relheight=1)

        # holds all the actual frames
        p1 = Utils._build_frame(left_zone)
        p1.pack(expand=True, fill="both", padx=(10, 5), pady=10)

        # area del mensaje de bienvenida
        p3 = Utils._build_frame(p1)
        p3.pack(side="top", padx=10, pady=10, fill="x")

        welcome_message = Utils._build_label(
            p3,
            text=Utils.left_align("""🛍️ Bienvenido a Ecart 👷
         Ecart le permite gestionar todo sobre sus negocioes,
         incluyendo sus mercancias, pedidos y personal"""),
            font=Commons.TEXT_FONT)

        welcome_message.pack(expand=True, fill="x", padx=10, pady=10)

        # project images area
        self.p4 = Utils._build_frame(p1)
        self.p4.pack(side="bottom", expand=True, padx=10, pady=10, fill="both")

        self.configure_project_images()

    # p4
    def configure_project_images(self) -> None:

        # project images frame
        self.project_images_frame = tk.Frame(self.p4)
        self.project_images_frame.pack(side="top", expand=True, fill="both")

        project_images = Utils.get_images_iterator("project")
        current_image = tk.PhotoImage()

        def set_next_image() -> None:
            current_image.config(file=next(project_images))

        set_next_image()

        image_display = tk.Label(self.project_images_frame, image=current_image)
        image_display.pack(expand=True)
        image_display.bind("<Enter>", lambda _: set_next_image())

        # login button
        def ingresar() -> None:
            self.master.config(menu=tk.Menu())  # destroy master menu
            self.destroy()  # destroy current frame
            VentanaPrincipal.start(self.master)

        self.project_ingresar_button = tk.Button(self.p4,
                                                 text="    Ingresar    ",
                                                 command=ingresar)
        self.project_ingresar_button.pack(side="bottom", padx=10, pady=10)
