# -*- coding: utf-8 *-*
'''
Created on 05/02/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import os
import time
import datetime
import pygame
# -----------
# Constantes
# -----------
apagarW = "shutdown /s /f /t 01"
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import model
import UserView
import Clases.encriptador
# ------------------------------
# Funcion principal del Programa
""" Controlador de la Interfaz del Usuario"""
# ------------------------------


class controlador:
    def __init__(self,sistemaop,usuario,modulo_asistencia):
        # Guardamos el SO
        self.sistemaop = sistemaop    
        
        # Instancia para los Datos del Usuario Logeado
        self.usuario = usuario

        # Instancia a la Clase Encriptador
        self.tags_db = ("[host]","[port]","[user]","[pwd]","[db]")

        if sistemaop == "linux2":
            self.archivo = "/opt/BitacoraL/src/files/profile3"
        else:
            self.archivo = "C:/Program Files/Bitacora/src/files/profile3"
        
        self.encriptador = Clases.encriptador.Encriptador(self.sistemaop,self.tags_db,self.archivo)

        d = self.encriptador.leer_datos()

        # Instancia para el Modelo
        self.modelo = model.modelo(d)

        # Instancia para la VISTA
        self.vista = UserView.UserView(sistemaop,modulo_asistencia)

        # Instancia a la Bandera Modulo de Asistencia
        self.modulo_asistencia = modulo_asistencia

        # Cargamos todo lo relacionado a pygame
        pygame.init() 

    """---------------------------------------Metodos-------------------------------------------------------"""
    def crear_interfaz(self):
        self.vista.crear_interfaz()
        self.vista.usuario_logeado.update_prompt(self.usuario.get_nombre_usuario())
    
    def get_name_user(self):
        "Metodo que nos da el Nombre Completo del Usuario Logeado"
        return self.usuario.obtener_usuario()
    
    def get_user_type(self):
        "Metodo que nos da el Tipo de Usuario Logeado"
        return self.usuario.obtener_tipo_usuario()

    def reset_usuario(self):
        self.usuario.reset_usuario()
        
    def imprimir_datos_usuario(self):
        self.usuario.Imprimir_valores()

    def obtener_Hora_Servidor(self):
        "Se Verifica la Hora del Servidor"
        consulta,edo_consulta = self.modelo.hora_sistema()
        if edo_consulta == "SUCCESS":
            self.usuario.set_hora_final(consulta[0][0])
        return edo_consulta
    
    def registrar_Salida(self):
        "Se Registra el Fin de Sesion"
        return self.modelo.registrar_salida(self.usuario.clvUsu,self.usuario.hora_inicio,self.usuario.hora_salida,self.usuario.IP_Equipo)

    def salir_sistema(self):
        "Metodo para La Salida del Usuario"
        res = ""
        access = ""
        mensaje = ""
        
        res = self.obtener_Hora_Servidor()
        if res == "SUCCESS":
            res = self.registrar_Salida()
            if res == "SUCCESS_QUERY_REGISTER":
                access = res
                mensaje = ""
            elif res == "FAILED_QUERY_REGISTER":
                # Fallo en Realizar Registro de Fin de Sesion
                "Fallo en Realizar Registro de Fin de Sesion"
                access = ""
                mensaje = "No se Realizo el Fin de Sesion"
        else:
            # Fallo Al Obtener la Hora del Servidor
            "Fallo en Realizar Registro de Fin de Sesion"
            access = ""
            mensaje = "Hora No Valida"

        self.vista.mensaje.update_prompt(mensaje)
        return access

    def ApagarEquipo(self):
        "Click en Boton Apagar Equipo"
        os.system(apagarW)
    
    """--------------------------------------Eventos-------------------------------------------------------"""
    def eventos_userview(self):
        "Metodo para Los Eventos en la Vista del Usuario"
        access = "Usuario"
        res = ""
        while True:
            # Empezamos a capturar la lista de Eventos
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Borramos Mensaje para el Usuario
                    self.vista.mensaje.update_prompt("")
                    x, y = event.pos
                    if self.vista.salir.collidepoint(x, y) or self.vista.apagar.collidepoint(x, y):
                        # Click para Cerrar Sesion o Apagar Equipo
                        res = ""
                        res = self.salir_sistema()
                        # Click en Cerrar Sesion
                        if self.vista.salir.collidepoint(x, y) and res == "SUCCESS_QUERY_REGISTER":
                            access = "Login"
                            return access
                        # Click en Boton Apagar
                        elif self.vista.apagar.collidepoint(x, y) and res == "SUCCESS_QUERY_REGISTER":
                            self.ApagarEquipo()
                    elif self.vista.asistencia.collidepoint(x, y):
                        if self.usuario.get_tipo_usuario() == "alum" and self.modulo_asistencia == "True":
                            access = "Asistencia"
                            return access

            self.vista.surface(self.usuario.get_tipo_usuario())
            self.vista.refresh_display()