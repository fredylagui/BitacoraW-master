# -*- coding: utf-8 *-*
'''
Created on 18/06/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import pygame
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import ModConfigView
import Clases.modulos
# ------------------------------
# Funcion principal del Programa
""" Controlador de la Interfaz de los Modulos Complementarios"""
# ------------------------------


class ModController:
    def __init__(self,sistemaop):
        # Guardamos el SO
        self.sistemaop = sistemaop    
                
        # Instancia para la VISTA
        self.vista = ModConfigView.ModConfigView(sistemaop)

        # Instancia para el Objeto Modulo
        self.modulo = Clases.modulos.Modulo(self.sistemaop)

        # Cargamos todo lo relacionado a pygame
        pygame.init() 

    """---------------------------------------Metodos-------------------------------------------------------"""
    def crear_interfaz(self):
        self.vista.crear_interfaz()
        
    def actualizar_datos_mod_asistencia(self,modo):
        "Metodo para Habilitar - Deshabilitar Modulo de Asistencia"
        if modo == "True":
            mensaje = "Modulo Habilitado"
        else:
            mensaje = "Modulo Deshabilitado"
        self.modulo.guardar_tag_dato("[asistencia]", modo)
        self.vista.mensaje.update_prompt(mensaje)

    """--------------------------------------Eventos-------------------------------------------------------"""
    def eventos_config(self):
        "Metodo para Los Eventos en la Vista del Usuario"
        # Iniciamos con el foco en el textbox del Usuario
        band_write = 1
                
        res = ""
        while True:
            # Empezamos a capturar la lista de Eventos
            events = pygame.event.get()
            for event in events:
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.vista.mensaje.update_prompt("")                    
                    # Dependiendo de la zona donde se hizo click se realiza una accion
                    x, y = event.pos
                    if self.vista.asistencia_habilitar.collidepoint(x, y):
                        # Click en Boton Habilitar Modulo Asistencia
                        self.actualizar_datos_mod_asistencia("True")
                        
                    elif self.vista.asistencia_deshabilitar.collidepoint(x, y):
                        # Click en Boton Deshabilitar Modulo Asistencia
                        self.actualizar_datos_mod_asistencia("False")

                    elif self.vista.regresar.collidepoint(x, y):
                        # Click en Boton Regresar
                        return
            self.vista.surface()
            self.vista.refresh_display()