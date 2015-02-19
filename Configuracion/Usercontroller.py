# -*- coding: utf-8 *-*
'''
Created on 05/06/2014

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
import UserConfigView
import Clases.encriptador
# ------------------------------
# Funcion principal del Programa
""" Controlador de la Interfaz del Usuario"""
# ------------------------------


class UserController:
    def __init__(self,sistemaop):
        # Guardamos el SO
        self.sistemaop = sistemaop    
                
        # Instancia para la VISTA
        self.vista = UserConfigView.UserConfigView(sistemaop)

        if sistemaop == "linux2":
            archivo = "/opt/BitacoraL/src/files/profile1"
        else:
            archivo = "C:/Program Files/Bitacora/src/files/profile1"

        # Configuracion del Objeto a la Instancia de la Clase
        lista_tags = ["[user]","[pwd]"]
        # Instancia para el Encriptador
        self.encriptador = Clases.encriptador.Encriptador(sistemaop,lista_tags,archivo)

        # Cargamos todo lo relacionado a pygame
        pygame.init() 

    """---------------------------------------Metodos-------------------------------------------------------"""
    def crear_interfaz(self):
        self.vista.crear_interfaz()
        
    def actualizar_datos(self):
        "Metodo para Configurar Usuario y Pwd del Super Usuario"
        mensaje = ""
        user = self.vista.t_usuario.getTxt()
        if user != "":
            tmp = ""
            for caracter in user:
                entero = ord(caracter)
                tmp += chr(entero)
            pwd = self.vista.t_pwd.getTxt()
            if pwd != "":
                tmp2 = ""
                for caracter in pwd:
                    entero = ord(caracter)
                    tmp2 += chr(entero)
        
                lista_newdata = [tmp,tmp2]
                self.encriptador.actualizar_archivo(lista_newdata)
                mensaje = "Usuario Actualizado"
            else:
                mensaje = "Ingresar Pwd"
        else:
            mensaje = "Ingresar Usuario"
        self.vista.mensaje.update_prompt(mensaje)
        return
            #tmp ="cadena"


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
                if event.type == pygame.KEYDOWN:
                    # Para iterar entre los dos TextBox de Usuario y Pwd
                    if event.key == pygame.K_TAB:
                        #print "Click en tecla TAB"
                        if band_write < 2:
                            band_write += 1
                        elif band_write == 2:
                            band_write = 1
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.vista.mensaje.update_prompt("")                    
                    # Dependiendo de la zona donde se hizo click se realiza una accion
                    x, y = event.pos
                    if x>= 45 and x <= 295 and y >= 75 and y<= 100:
                        # Click en Textbox usuario
                        band_write = 1
                    elif x>= 45 and x <= 295 and y >= 125 and y<= 150:
                        # Click en Textbox pwd
                        band_write = 2
                    
                    elif self.vista.actualizar.collidepoint(x, y):
                        # Click en Boton Actualizar
                        self.actualizar_datos()

                    elif self.vista.regresar.collidepoint(x, y):
                        # Click en Boton Regresar
                        return
                    
            if band_write == 1:
                # Se ingresan datos en el TextBox del Usuario
                self.vista.t_usuario.update(events,self.sistemaop)
            elif band_write == 2:
                # Se ingresan datos en el TextBox del Pwd
                self.vista.t_pwd.update(events,self.sistemaop)
            self.vista.surface()
            self.vista.refresh_display()