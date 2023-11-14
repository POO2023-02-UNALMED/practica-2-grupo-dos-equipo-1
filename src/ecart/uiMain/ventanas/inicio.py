import tkinter as tk
import os, sys
from tkinter import font
from ecart.uiMain.parts.msgbox_wrapper import MsgboxWrapper as MB
from ecart.uiMain.utils import Utils
from ecart.uiMain.ventanas.principal import VentanaPrincipal


class VentanaInicio(tk.Frame):
   def __init__(self, master: tk.Tk, *args, **kwargs) -> None:

      super().__init__(master, *args, **kwargs)
      self.master: tk.Tk = master
      
      master.wm_title("Ecart - Inicio")

      hello = os.path.join(Utils.get_module_rootdir(), "ecart", "images", "hello.png")
      print(hello)

      self.configure_menubar()
      self.configure_right_frameholder()
      self.configure_left_frameholder()

   def exit_program(self) -> None:

      should_exit = MB.show("ay", "Estas seguro que deseas salir de la aplicación?")
      if should_exit:
         self.master.destroy()

   def show_description(self) -> None:

      self.project_images_frame.destroy()
      self.project_ingresar_button.destroy()

      tmp_frame = tk.Frame(self.p4)
      tmp_frame.pack(expand=True, fill="both")

      system_description = Utils._build_label(tmp_frame,
      
         text="""📃 Descripcion del sistema 📚


Gracias a nutra interfaz intuitiva y funcionalidades avanzadas,
Ecart le permite establecer y personalizar sus propias tiendas
en línea, de manera sencilla y eficiente. Brindando las
siguientes funcionalidades:

  1. Crear y administrar tiendas
  2. Contratar personal
  3. Hacer entregas
  4. Sugerir productos
  5. Gestionar ingresos
"""
      )

      system_description.pack(expand=True, fill="both")

      def _destroy() -> None:
         tmp_frame.destroy()
         self.configure_project_images()

      regresar_button = tk.Button(tmp_frame, text="Regresar", command=_destroy)
      regresar_button.pack(side="bottom", padx=10, pady=10)

   def configure_menubar(self) -> None:

      menubar = tk.Menu(self.master)

      inicio_menu = tk.Menu(menubar, tearoff=False)
      menubar.add_cascade(label="Inicio", menu=inicio_menu)

      inicio_menu.add_command(label="Salir", command=self.exit_program)
      inicio_menu.add_separator()
      inicio_menu.add_command(label="Descripción", command=self.show_description)

      self.master.config(menu=menubar)

   def configure_right_frameholder(self):

      right_zone = tk.Frame(self)
      right_zone.place(relx=0.5, relwidth=0.5, relheight=1)

      # holds all the actual frames
      p2 = Utils._build_frame(right_zone)
      p2.pack(expand=True, fill="both", padx=(5, 10), pady=10)

      class Author:
         def __init__(self, name, semester, info):
            self.name = name
            self.semester = semester
            self.info = info

      authors = {
         "angel": Author("Angel", "3", "Desarrollador de software apasionado"),
         "sebastian": Author("Sebastian", "3", "Desarrollador de software apasionado"),
         "rodrigo": Author("Rodrigo", "3", "Desarrollador de software apasionado"),
         "santiago": Author("Santiago", "3", "Desarrollador de software apasionado")
      }

      names = Utils.iterate_inf(authors.keys())
      biographies = Utils.iterate_inf(authors.values())
   
      # (P5) Authors biographies
      biography_frame = Utils._build_frame(p2)
      biography_frame.pack(side="top", padx=10, pady=10, fill="x")

      current_biography = ""

      biography_display = Utils._build_label(biography_frame, text=current_biography)
      biography_display.pack(expand=True, fill="x", padx=10, pady=10)

      def set_next_biography() -> None:

         author: Author = next(biographies)

         biography_display.config(text=Utils.left_align(
            f"""Hoja de Vida de los Autores
            (haga click)

            🗯️ Nombre: {author.name}
            📙 Semestre: {author.semester}
            📃 Informacion: {author.info}""")
         )

      set_next_biography()
      biography_display.bind("<Button-1>", lambda _: set_next_biography())


      # (P6) Authors images
      p6 = Utils._build_frame(p2)
      p6.pack(side="bottom", expand=True, padx=10, pady=10, fill="both")

      images_frame = tk.Frame(p6)
      images_frame.pack(side="top", expand=True, fill="both")

      current_path = "/home/pocco81/Documents/uni/poo/practica-2/src/ecart/images/authors/angel/profile1.png"
      current_image = tk.PhotoImage(file=current_path)

      image_displays = []
      image_displays[0] = tk.Label(images_frame, text="hello")
      image_displays[1] = tk.Label(images_frame, text="hello")
      image_displays[2] = tk.Label(images_frame, text="hello")
      image_displays[3] = tk.Label(images_frame, text="hello")

      # current_images = [tk.PhotoImage(file=img_path) for img_path in Utils.get_images("authors", next(names))]
      # current_pics = Utils.get_images("authors", next(names))
      # images_displays = [tk.Label(images_frame, text="hello", image=image_) for image_ in current_images]

      # images_displays[0].grid(row=0, column=0, padx=(5,0), pady=(5,0), sticky="nsew")
      # images_displays[1].grid(row=0, column=1, padx=(0,5), pady=(5,0), sticky="nsew")
      # images_displays[2].grid(row=1, column=0, padx=(5,0), pady=(0,5), sticky="nsew")
      # images_displays[3].grid(row=1, column=1, padx=(0,5), pady=(0,5), sticky="nsew")

      # make each row and column expand
      images_frame.grid_rowconfigure(0, weight=1)
      images_frame.grid_rowconfigure(1, weight=1)
      images_frame.grid_columnconfigure(0, weight=1)
      images_frame.grid_columnconfigure(1, weight=1)

      # image_displays = [[tk.Label(images_frame, image=image) for image in current_images[i*2:(i+1)*2]] for i in range(2)]
      

      # for i, row in enumerate(image_displays):
      #    for j, label in enumerate(row):
      #       label.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")


      # def set_next_images():
      #    current_images = [tk.PhotoImage(file=img_path) for img_path in Utils.get_images(next(names))]

      # def set_next_images() -> None:
      #
      #    author_images = Utils.get_images_iterator("authors", next(names)) 
      #    current_image = tk.PhotoImage()
      #
      #    for _, row in enumerate(image_displays):
      #       for _, label in enumerate(row):
      #          current_image.config(file=next(author_images))
      #          label.config(image=current_image)
      #
      # set_next_images()

   def configure_left_frameholder(self):

      left_zone = tk.Frame(self)
      left_zone.place(relwidth=0.5, relheight=1)

      # holds all the actual frames
      p1 = Utils._build_frame(left_zone)
      p1.pack(expand=True, fill="both", padx=(10, 5), pady=10)

      # area del mensaje de bienvenida
      p3 = Utils._build_frame(p1)
      p3.pack(side="top", padx=10, pady=10, fill="x")

      # no cambiar! hace que se vea mejor en la interfaz
      welcome_message = Utils._build_label(p3, text=Utils.left_align(
         """🛍️ Bienvenido a Ecart 👷
         Ecart le permite gestionar todo sobre sus negocioes,
         incluyendo sus mercancias, pedidos y personal""")
      )

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
         self.master.config(menu=tk.Menu()) # destroy master menu
         self.destroy() # destroy current frame
         VentanaPrincipal(self.master, bg="lightgreen").pack(fill="both", side="top", expand = True)

      self.project_ingresar_button = tk.Button(self.p4, text="Ingresar", command=ingresar)
      self.project_ingresar_button.pack(side="bottom", padx=10, pady=10)
