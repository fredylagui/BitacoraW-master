'''
Created on 14/04/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
from ctypes import windll
import pygame
from pygame.locals import *
# -----------
# Constantes
# -----------
SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 900
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import Clases.eztext
# ------------------------------
# Descripcion de la Clase
""" Clase para la Interfaz del Login"""
# ------------------------------

class LoginView():
    def __init__(self,sistemaop,usuario):
        "Definimos los Atributos de la Clase"
        # Guardamos el SO
        self.sistemaop = sistemaop
        
        # Set up a variable that calls the "SetWindowPos" in user32
        self.SetWindowPos = windll.user32.SetWindowPos
        
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
        # Cargamos el fondo y las imagenes para la Ventana Login
        if self.sistemaop == "linux2":
            imagenfondo = "/opt/BitacoraL/src/images/Fondo.png"
            imagenform = "/opt/BitacoraL/src/images/Fondo_Panel.png"
            imagenbEntrar = "/opt/BitacoraL/src/images/Entrar.png"
            imagenbApagar = "/opt/BitacoraL/src/images/Apagar.png"
        else:
            imagenfondo = "C:/Program Files/Bitacora/src/images/Fondo.png"
            imagenform = "C:/Program Files/Bitacora/src/images/Fondo_Panel.png"
            imagenbEntrar = "C:/Program Files/Bitacora/src/images/Entrar.png"
            imagenbApagar = "C:/Program Files/Bitacora/src/images/Apagar.png"

            
        self.fondo = pygame.image.load(imagenfondo).convert()
        self.form = pygame.image.load(imagenform).convert_alpha()
        self.bentrar = pygame.image.load(imagenbEntrar).convert_alpha()
        self.bapagar = pygame.image.load(imagenbApagar).convert_alpha()

    def cargar_textbox(self):
        "Metodo para cargar TextBox y Textos a la Interfaz"
        # Cargamos los TextBox
        self.usuario = Clases.eztext.Input(x=570, y=365, font = self.fuente, maxlength=20, color=(159,161,164), prompt='')
        self.pwd = Clases.eztext.Input(x=570, y=415, font = self.fuente, maxlength=20, color=(159,161,164), prompt='')

        # Cargamos Item para los Mensajes al Usuario
        self.mensaje = Clases.eztext.Input(x=520, y=335, font = self.fuente, maxlength=20, color=(255,0,0), prompt='')
    
    def cargar_botones(self):
        "Metodo para cargar Botones a la Interfaz"
        # Cargamos los Botones para la Interfaz
        self.entrar = self.bentrar.get_rect(center=(543, 484))
        self.apagar = self.bapagar.get_rect(center=(797, 501))

    def dimencionar_ventana(self):
        "Metodo Para Dimencionar la Ventana"
        # Modo Sin Bordes para el Login
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.NOFRAME)
        # Supply the hWnd(Window Handle) with the window ID returned from a call to display.get_wm_info()
        # This sets the window to be on top of other windows.
        self.SetWindowPos(pygame.display.get_wm_info()['window'], -1, 0, 0, 0, 0, 0x0001)
        pygame.display.set_caption("Login")
    
    def refresh_display(self):
        # refresh the display
        pygame.display.flip()
        
    def surface(self):
        "Metodo para Agregar los Surface a la Ventana Login"
        self.screen.blit(self.fondo, (0,0))
        self.screen.blit(self.form, (420,300))
        self.screen.blit(self.bentrar, self.bentrar.get_rect(center=(543, 484)))
        self.screen.blit(self.bapagar, self.bapagar.get_rect(center=(797, 501)))
        self.usuario.draw(self.screen)
        self.pwd.draw_pwd(self.screen)
        self.mensaje.draw(self.screen)

    def reset_inputs(self):
        "Metodo para Restear los Inputs de la Vista"
        self.usuario.reset_input()
        self.pwd.reset_input()
