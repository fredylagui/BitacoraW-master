# -*- coding: utf-8 *-*
#!/usr/bin/ python
'''
Created on 19/03/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
#import logging
from datetime import datetime
import pygame
from pygame.locals import *
import sys
sys.path.append("..")
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import Clases.usuario
import Clases.modulos
import Login.controller
import InterfazUsuario.controller
import Asistencia.controller
import Configuracion.controller
# ------------------------------
# Funcion principal de la Aplicacion
# ------------------------------
"Vista de La Aplicacion para llevar un control de los Alumnos y los Equipos en las Aulas"
 
class Main():
     
    def main(self):
        "Metodo Main Principal"
        # Obtenemos el S.O Esto es para pruebas en Windows.
        self.sistemaop = sys.platform
        print self.sistemaop

        # Creamos una instancia al Objeto Usuario
        self.usuario = Clases.usuario.Usuario()
        
        # Modulos Integrados
        self.modulo = Clases.modulos.Modulo(self.sistemaop)
        self.modulo_asistencia = self.modulo.leer_datos("[asistencia]")
        
        # Cargamos todo lo relacionado a pygame
        pygame.init()
        
        # Creamos las Instancias a los Controladores
        self.login_controlador = Login.controller.controlador(self.sistemaop,self.usuario)
        self.user_controlador = InterfazUsuario.controller.controlador(self.sistemaop,self.usuario,self.modulo_asistencia)
        self.asist_controlador = Asistencia.controller.controlador(self.sistemaop,self.usuario)
        self.config_controlador = Configuracion.controller.controlador(self.sistemaop)
        
        # create the pygame clock
        self.clock = pygame.time.Clock()
    
    """---------------------------------------Metodos-------------------------------------------------------"""
    
    def iniciar(self):
        "Metodo para El bucle Principal de la Aplicacion"
        
        # Inicializamos la variable de edo_aplicacion.
        edo_aplicacion = "Login"
        
        # Ciclo Infinito Principal
        while True:
            # Nos Aseguramos que el codigo corre a 30 fps
            self.clock.tick(30)
                                    
            if edo_aplicacion == "Login":
                # Creamos la Ventana Login
                self.login_controlador.crear_interfaz()
                
                # Se Configura para el Inicio de una Sesion de Usuario
                self.login_controlador.configurar_inicio()
                
                # Monitorear los Eventos de la Vista Login
                edo_aplicacion = self.login_controlador.eventos_loginview()

            elif edo_aplicacion == "Usuario":
                # Creamos la Ventana de Usuario
                self.user_controlador.crear_interfaz()
                
                # Monitorear los Eventos de la Vista Usuario
                edo_aplicacion = self.user_controlador.eventos_userview()
                
            elif edo_aplicacion == "Asistencia" and self.modulo_asistencia == "True":
                # Creamos la Ventana de Asistencia
                self.asist_controlador.crear_interfaz()
                
                # Monitorear los Eventos de la Vista Asistencia
                edo_aplicacion = self.asist_controlador.eventos_asistview()
                
            elif edo_aplicacion == "Config":
                # Creamos la Ventana de Configuracion
                self.config_controlador.crear_interfaz()
                
                # Monitorear los Eventos de la Vista Configuracion
                edo_aplicacion = self.config_controlador.eventos_config()
    
if __name__ == "__main__":
    inicio = Main()
    inicio.main()
    inicio.iniciar()