# -*- coding: utf-8 *-*
'''
Created on 04/06/2014

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
import DBConfigView
import Clases.encriptador
# ------------------------------
# Funcion principal del Programa
""" Controlador de la Interfaz del Usuario"""
# ------------------------------


class DBController:
    def __init__(self,sistemaop):
        # Guardamos el SO
        self.sistemaop = sistemaop    
                
        # Instancia para la VISTA
        self.vista = DBConfigView.DBConfigView(sistemaop)

        if sistemaop == "linux2":
            archivo = "/opt/BitacoraL/src/files/profile3"
        else:
            archivo = "C:/Program Files/Bitacora/src/files/profile3"

        # Configuracion del Objeto a la Instancia de la Clase
        lista_tags = ["[host]","[port]","[user]","[pwd]","[db]"]
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
        host = self.vista.t_host.getTxt()
        if host != "":
            tmp = ""
            for caracter in host:
                entero = ord(caracter)
                tmp += chr(entero)
            puerto = self.vista.t_puerto.getTxt()
            if puerto != "":
                tmp2 = ""
                for caracter in puerto:
                    entero = ord(caracter)
                    tmp2 += chr(entero)
                user = self.vista.t_usuario.getTxt()
                if user != "":
                    tmp3 = ""
                    for caracter in user:
                        entero = ord(caracter)
                        tmp3 += chr(entero)
                    pwd = self.vista.t_pwd.getTxt()
                    tmp4 = ""
                    for caracter in pwd:
                        entero = ord(caracter)
                        tmp4 += chr(entero)
                    db = self.vista.t_db.getTxt()
                    if db != "":
                        tmp5 = ""
                        for caracter in db:
                            entero = ord(caracter)
                            tmp5 += chr(entero)
                        lista_newdata = [tmp,tmp2,tmp3,tmp4,tmp5]
                        self.encriptador.actualizar_archivo(lista_newdata)
                        mensaje = "Conexion a BD Actualizada"
                    else:
                        mensaje = "Ingresar Nombre de BD"
                else:
                    mensaje = "Ingresar Usuario"
            else:
                mensaje = "Ingresar Puerto"
        else:
            mensaje = "Ingresar Host"
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
                        if band_write < 5:
                            band_write += 1
                        elif band_write == 5:
                            band_write = 1
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.vista.mensaje.update_prompt("")                    
                    # Dependiendo de la zona donde se hizo click se realiza una accion
                    x, y = event.pos
                    if x>= 45 and x <= 295 and y >= 35 and y<= 60:
                        # Click en Textbox Host
                        band_write = 1
                    elif x>= 45 and x <= 295 and y >= 70 and y<= 95:
                        # Click en Textbox Puerto
                        band_write = 2
                    elif x>= 45 and x <= 295 and y >= 105 and y<= 130:
                        # Click en Textbox Usuario
                        band_write = 3
                    elif x>= 45 and x <= 295 and y >= 140 and y<= 165:
                        # Click en Textbox Pwd
                        band_write = 4
                    elif x>= 45 and x <= 295 and y >= 175 and y<= 200:
                        # Click en Textbox DB
                        band_write = 5
                    elif self.vista.actualizar.collidepoint(x, y):
                        # Click en Boton Actualizar
                        self.actualizar_datos()

                    elif self.vista.regresar.collidepoint(x, y):
                        # Click en Boton Regresar
                        return
                    
            if band_write == 1:
                # Se ingresan datos en el TextBox del Host
                self.vista.t_host.update(events,self.sistemaop)
            elif band_write == 2:
                # Se ingresan datos en el TextBox del Puerto
                self.vista.t_puerto.update(events,self.sistemaop)
            elif band_write == 3:
                # Se ingresan datos en el TextBox del Usuario
                self.vista.t_usuario.update(events,self.sistemaop)
            elif band_write == 4:
                # Se ingresan datos en el TextBox del Pwd
                self.vista.t_pwd.update(events,self.sistemaop)
            elif band_write == 5:
                # Se ingresan datos en el TextBox del DB
                self.vista.t_db.update(events,self.sistemaop)
                
            self.vista.surface()
            self.vista.refresh_display()