'''
Created on 18/06/2014

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
S_HEIGHT = 250
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import Clases.eztext
# ------------------------------
# Descripcion de la Clase
""" Clase para la Interfaz de los Modulos Complementarios"""
# ------------------------------

class ModConfigView():
    def __init__(self,sistemaop):
        "Definimos los Atributos de la Clase"
        # Guardamos el SO
        self.sistemaop = sistemaop
        
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
            imagenconfig_interface = "/opt/BitacoraL/src/images/config_submenu.png"
            imagenbActivar = "/opt/BitacoraL/src/images/Activar.png"
            imagenbDesactivar = "/opt/BitacoraL/src/images/Desactivar.png"
            imagenbRegresar = "/opt/BitacoraL/src/images/Regresar.png"
            imagenEtiqueta = "/opt/BitacoraL/src/images/Etiqueta.png"            
        else:
            imagenconfig_interface = "C:/Program Files/Bitacora/src/images/config_submenu.png"
            imagenbActivar = "C:/Program Files/Bitacora/src/images/Activar.png"
            imagenbDesactivar = "C:/Program Files/Bitacora/src/images/Desactivar.png"
            imagenbRegresar = "C:/Program Files/Bitacora/src/images/Regresar.png"
            imagenEtiqueta = "C:/Program Files/Bitacora/src/images/Etiqueta.png"
                        
        self.config_interface = pygame.image.load(imagenconfig_interface).convert()

        self.basistencia_habilitar = pygame.image.load(imagenbActivar).convert_alpha()
        self.basistencia_deshabilitar = pygame.image.load(imagenbDesactivar).convert_alpha()
        self.bregresar = pygame.image.load(imagenbRegresar).convert_alpha()
        
    def cargar_textbox(self):
        "Metodo para cargar TextBox y Textos a la Interfaz"
        # Cargamos Item para los Mensajes al Usuario
        self.titulo = Clases.eztext.Input(x=25, y=30, font = self.fuente, maxlength=20, color=(109,110,113), prompt='Configuracion de Modulos')
        self.modulo_asistencia = Clases.eztext.Input(x=50, y=80, font = self.fuente, maxlength=20, color=(109,110,113), prompt='Asistencia  ')
        self.mensaje = Clases.eztext.Input(x=150, y=180, font = self.fuente, maxlength=20, color=(255,0,0), prompt='')

    def cargar_botones(self):
        "Metodo para cargar Botones a la Interfaz"
        # Cargamos los Botones para la Interfaz
        self.asistencia_habilitar = self.basistencia_habilitar.get_rect(center=(180, 90))
        self.asistencia_deshabilitar = self.basistencia_deshabilitar.get_rect(center=(280, 90))
        self.regresar = self.bregresar.get_rect(center=(400, 90))

    def dimencionar_ventana(self):
        "Metodo Para Dimencionar la Ventana"
        # Modo Resizable para Usuario
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Configuracion de Modulos Complementarios")

    def refresh_display(self):
        # refresh the display
        pygame.display.flip()
            
    def surface(self):
        "Metodo para Agregar los Surface a la Ventana Usuario"
        self.screen.blit(self.config_interface, (0,0))
        self.screen.blit(self.basistencia_habilitar, self.basistencia_habilitar.get_rect(center=(180, 90)))
        self.screen.blit(self.basistencia_deshabilitar, self.basistencia_deshabilitar.get_rect(center=(280, 90)))
        self.screen.blit(self.bregresar, self.bregresar.get_rect(center=(400, 90)))
        self.titulo.draw(self.screen)
        self.modulo_asistencia.draw(self.screen)
        self.mensaje.draw(self.screen)