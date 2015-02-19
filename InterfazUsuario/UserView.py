'''
Created on 14/04/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import pygame
from pygame.locals import *
# -----------
# Constantes
# -----------
S_WIDTH = 480
S_HEIGHT = 150
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import Clases.eztext
# ------------------------------
# Descripcion de la Clase
""" Clase para la Interfaz del Usuario"""
# ------------------------------

class UserView():
    def __init__(self,sistemaop,modulo_asistencia):
        "Definimos los Atributos de la Clase"
        # Guardamos el SO
        self.sistemaop = sistemaop
        
        # Guardamos bandera para Habilitar Modulos
        self.modulo_asistencia = modulo_asistencia
        
        # Cargamos todo lo relacionado a pygame
        pygame.init()
        
        # Cargamos el Tipo de Fuente a Usar
        self.fuente = pygame.font.SysFont("Arial", 14, bold=True, italic=False)
        
    def crear_interfaz(self):
        self.dimencionar_ventana()
        self.cargar_imagenes()
        self.cargar_textbox()
        self.cargar_botones()

    def cargar_imagenes(self):
        "Metodo para Cargar las Imagenes a la Interfaz"
        # Cargamos el fondo y las imagenes para la Ventana UserView
        if self.sistemaop == "linux2":
            imagenuser_interface = "/opt/BitacoraL/src/images/user_interface.png"
            imagenbAsistencia = "/opt/BitacoraL/src/images/Asistencia.png"
            imagenbCerrar = "/opt/BitacoraL/src/images/Cerrar.png"
            imagenbApagar = "/opt/BitacoraL/src/images/Apagar.png"
        else:
            imagenuser_interface = "C:/Program Files/Bitacora/src/images/user_interface.png"
            imagenbAsistencia = "C:/Program Files/Bitacora/src/images/Asistencia.png"
            imagenbCerrar = "C:/Program Files/Bitacora/src/images/Cerrar.png"
            imagenbApagar = "C:/Program Files/Bitacora/src/images/Apagar.png"
            
        self.user_interface = pygame.image.load(imagenuser_interface).convert()
        self.basistencia = pygame.image.load(imagenbAsistencia).convert_alpha()
        self.bapagar = pygame.image.load(imagenbApagar).convert_alpha()
        self.bsalir = pygame.image.load(imagenbCerrar).convert_alpha()
        
    def cargar_textbox(self):
        "Metodo para cargar TextBox y Textos a la Interfaz"
        # Cargamos Item para los Mensajes al Usuario
        self.usuario_logeado = Clases.eztext.Input(x=25, y=45, font = self.fuente, maxlength=20, color=(109,110,113), prompt='')
        self.mensaje = Clases.eztext.Input(x=150, y=110, font = self.fuente, maxlength=50, color=(255,0,0), prompt='')

    def cargar_botones(self):
        "Metodo para cargar Botones a la Interfaz"
        # Cargamos los Botones para la Interfaz
        self.apagar = self.bapagar.get_rect(center=(434, 103))
        self.asistencia = self.basistencia.get_rect(center=(380, 40))        
        self.salir = self.bsalir.get_rect(center=(45, 103))

    def dimencionar_ventana(self):
        "Metodo Para Dimencionar la Ventana"
        # Modo Resizable para Usuario
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Usuario")

    def refresh_display(self):
        # refresh the display
        pygame.display.flip()
        
    def surface(self,tipo_usuario):
        "Metodo para Agregar los Surface a la Ventana Usuario"
        self.screen.blit(self.user_interface, (0,0))
        self.screen.blit(self.bsalir, self.bsalir.get_rect(center=(45, 103)))
        # Si el Usuario Logeado es un Alumno se dibuja en la pantalla el boton de Asistencia.
        if tipo_usuario == "alum" and self.modulo_asistencia == "True":
            self.screen.blit(self.basistencia, self.basistencia.get_rect(center=(380, 40)))
        self.screen.blit(self.bapagar, self.bapagar.get_rect(center=(434, 103)))
        self.usuario_logeado.draw(self.screen)
        self.mensaje.draw(self.screen)       
