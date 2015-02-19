'''
Created on 21/04/2014

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

class AttendanceView():
    def __init__(self,sistemaop,usuario):
        "Definimos los Atributos de la Clase"
        # Guardamos la instancia del objeto Usuario
        self.usuario = usuario
        
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
        # Cargamos el fondo y las imagenes para la Asistencia View
        if self.sistemaop == "linux2":        
            imagenuser_interface = "/opt/BitacoraL/src/images/user_interface.png"
            imagenbAsistencia = "/opt/BitacoraL/src/images/Asistencia.png"
            imagenbRegresar = "/opt/BitacoraL/src/images/Regresar.png"
        else:
            imagenuser_interface = "C:/Program Files/Bitacora/src/images/user_interface.png"
            imagenbAsistencia = "C:/Program Files/Bitacora/src/images/Asistencia.png"
            imagenbRegresar = "C:/Program Files/Bitacora/src/images/Regresar.png"

        self.user_interface = pygame.image.load(imagenuser_interface).convert()
        self.basistencia = pygame.image.load(imagenbAsistencia).convert_alpha()
        self.bregresar = pygame.image.load(imagenbRegresar).convert_alpha()
        
    def cargar_textbox(self):
        "Metodo para cargar TextBox y Textos a la Interfaz"
        # Cargamos Item para los Mensajes al Usuario
        self.usuario_logeado = Clases.eztext.Input(x=25, y=45, font = self.fuente, maxlength=20, color=(109,110,113), prompt='')
        self.tmp = Clases.eztext.Input(x=20, y=70, font = self.fuente, maxlength=20, color=(109,110,113), prompt='Clase: ')
        self.clase = Clases.eztext.Input(x=25, y=90, font = self.fuente, maxlength=50, color=(109,110,113), prompt='')
        self.tmp2 = Clases.eztext.Input(x=20, y=110, font = self.fuente, maxlength=20, color=(109,110,113), prompt='Asistencia: ')
        self.edo_asist = Clases.eztext.Input(x=25, y=130, font = self.fuente, maxlength=50, color=(109,110,113), prompt='')
        self.mensaje = Clases.eztext.Input(x=150, y=110, font = self.fuente, maxlength=50, color=(255,0,0), prompt='')

    def cargar_botones(self):
        "Metodo para cargar Botones a la Interfaz"
        # Cargamos los Botones para la Interfaz
        self.regresar = self.bregresar.get_rect(center=(380, 40))
        self.asistencia = self.basistencia.get_rect(center=(380, 90))

    def dimencionar_ventana(self):
        "Metodo Para Dimencionar la Ventana"
        # Modo Resizable para Usuario
        self.screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Asistencia")

    def refresh_display(self):
        # refresh the display
        pygame.display.flip()
        
    def surface(self):
        "Metodo para Agregar los Surface a la Ventana de Asistencia"
        self.screen.blit(self.user_interface, (0,0))
        self.screen.blit(self.bregresar, self.bregresar.get_rect(center=(380, 40)))
        self.screen.blit(self.basistencia, self.basistencia.get_rect(center=(380, 90)))
        self.tmp.draw(self.screen)
        self.clase.draw(self.screen)
        self.tmp2.draw(self.screen)
        self.edo_asist.draw(self.screen)
        self.usuario_logeado.draw(self.screen)
        self.mensaje.draw(self.screen)
