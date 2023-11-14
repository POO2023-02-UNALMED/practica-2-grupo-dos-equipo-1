import tkinter as tk
import os, sys
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

   def toggle_description(self) -> None:
      pass

   def configure_menubar(self) -> None:

      menubar = tk.Menu(self.master)

      inicio_menu = tk.Menu(menubar, tearoff=False)
      menubar.add_cascade(label="Inicio", menu=inicio_menu)

      inicio_menu.add_command(label="Salir", command=self.exit_program)
      inicio_menu.add_separator()
      inicio_menu.add_command(label="Descripción", command=self.toggle_description)

      self.master.config(menu=menubar)

   def configure_right_frameholder(self):
      pass

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
      welcome_message = Utils._build_label(p3,
         text="""🛍️ Bienvenido a Ecart 👷
Ecart le permite gestionar todo sobre sus negocioes,
incluyendo sus mercancias, pedidos y personal"""
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

      def set_next_image() -> None:
         next_image_path = \
            Utils.get_image_path("project", next(project_images))
         current_image.config(file=next_image_path)

      project_images = Utils.iterate_inf([
         "analyzing.png",
         "business.png",
         "ecommerce.png",
         "purchasing.png",
         "shopping_cart.png"
      ])

      current_image = tk.PhotoImage()
      set_next_image()

      image_display = tk.Label(self.project_images_frame, image=current_image)
      image_display.pack(expand=True)
      image_display.bind("<Enter>", lambda _: set_next_image())


      # login button
      def ingresar() -> None:
         self.master.config(menu=tk.Menu()) # destroy master menu
         self.destroy() # destroy current frame
         VentanaPrincipal(self.master, bg="lightgreen").pack(fill="both", side="top", expand = True)

      self.ingresar_button = tk.Button(self.p4, text="Ingresar", command=ingresar)
      self.ingresar_button.pack(side="bottom", padx=10, pady=10)



