# -*- coding: utf-8 *-*
'''
Created on 05/02/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import time
import datetime
import pygame
from pygame.locals import *
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
import model
import AttendanceView
import Clases.encriptador
# ------------------------------
# Funcion principal del Programa
""" Controlador de Asistencia del Usuario"""
# ------------------------------


class controlador:
    def __init__(self,sistemaop,usuario):
        # Guardamos la instancia del objeto Usuario
        self.usuario = usuario
        
        # Guardamos el SO
        self.sistemaop = sistemaop 

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
        self.vista = AttendanceView.AttendanceView(sistemaop,usuario)
        
        # Cargamos todo lo relacionado a pygame
        pygame.init()

    """---------------------------------------Metodos-------------------------------------------------------"""
    def crear_interfaz(self):
        "Metodo para llamar todos los componentes para crear la Vista"
        self.vista.crear_interfaz()
        self.vista.usuario_logeado.update_prompt(self.usuario.get_nombre_usuario())
        self.clase_asistencia_alumno()

    def reset_asist_values(self):
        "Reseteamos las Variables para La Interfaz de Asistencia"
        self.band_clase = False
        self.asistencia_alumno = False
        self.usuario.clvHor = ""
        self.usuario.materia = ""

        """************************************************************************************************"""
                                        # Metodos para Mostrar:
                                        # Grupo
                                        # Nombre de la Materia
                                        # La Asistencia del Alumno a la Materia
        """************************************************************************************************"""        
    def clase_asistencia_alumno(self):
        "Metodo para Mostrar la Clase en la vista de Asistencia"
        self.reset_asist_values()
        self.vista.clase.update_prompt("Sin Clase")
        self.vista.edo_asist.update_prompt("Sin Asistencia")
                
        (fecha_consulta,hora_consulta,dia,hora,minuto),edo_consulta = self.obtener_Hora_Fecha_Servidor()
        if edo_consulta == "SUCCESS":
            clase,res = self.obtener_clase_alumno(fecha_consulta,dia,hora)
            if res == "FAILED_GET_GPO":
                self.vista.mensaje.update_prompt("Grupo No Valido")
            elif res == "FAILED_GET_CLASS":
                self.vista.mensaje.update_prompt("Clase No Valida")
            elif res == "FAILED_GET_MAT":
                self.vista.mensaje.update_prompt("Materia No Valida")
            elif res == "FAILED_GET_HOUR":
                self.vista.mensaje.update_prompt("Hora No Valida")
            else:
                self.vista.clase.update_prompt(clase)
                self.vista.mensaje.update_prompt(res)
                # Obtenemos el status de la Asistencia del Alumno
                asist,res = self.obtener_asist_alum(fecha_consulta)
                if res == "FAILED_GET_ASIST":
                    self.vista.mensaje.update_prompt("Edo. de Asistencia No Valido")
                else:
                    self.vista.edo_asist.update_prompt(asist)
        else:
            self.vista.mensaje.update_prompt("Hora no Valida")
    
    def obtener_Hora_Fecha_Servidor(self):
        "Se Verifica la Fecha del Servidor"
        fecha_consulta = ""
        dia = ""
        hora = ""
        minuto = ""
        edo_consulta = ""
        hora_consulta = ""
        consulta,edo_consulta = self.modelo.hora_sistema()
        if edo_consulta == "SUCCESS":
            # Obtenemos la Fecha se solicito Boton de Registrar Asistencia
            fecha = datetime.datetime.strptime(str (consulta[0][0]),"%Y-%m-%d %H:%M:%S")
            tmp = str (consulta[0][0])
            fecha_consulta = str (tmp[:tmp.find(' ')] )
            hora_consulta = str (tmp[tmp.find(' ')+1:] )

            # Guardamos el Dia y la Hora
            # 0 es Domingo 6 es Sabado

            dia = int(fecha.strftime('%w'))
            # 24 Hrs  00 - 23
            hora = int(fecha.strftime('%H'))
            # 0 - 60 Min
            minuto = int(fecha.strftime('%M'))
        return (fecha_consulta,hora_consulta,dia,hora,minuto),edo_consulta
    
    def obtener_clvhor_clvmat(self,fecha_consulta,dia,hora):
        "Obtenemos la Clave del Horario y la Clave de la Materia"
        consulta = ""
        edo_consulta = ""
        # Buscamos La clave de la Materia en el Horario
        consulta,edo_consulta = self.modelo.clase_horario(self.usuario.get_gpo(),dia,hora)
        if edo_consulta == "SUCCESS":
            if consulta:
                # La entrada esta marcada en el Horario
                return consulta,edo_consulta
            else:
                # Verificar si es Clase Normal=8 o Laboral Permutable=6
                consulta2,edo_consulta2 = self.modelo.fecha_calendario(fecha_consulta)
                if edo_consulta2 == "SUCCESS":
                    if consulta2:
                        staCalEsc = consulta2[0][0]
                        staCalEsc2 = consulta2[0][1]
                        if staCalEsc == 6 or staCalEsc == 8 or staCalEsc2 == 6 or staCalEsc2 == 8:
                            dia = 1
                            consulta,edo_consulta = self.modelo.clase_horario(self.usuario.get_gpo(),dia,hora)        
                        else:
                            consulta = consulta2
                            edo_consulta = edo_consulta2
                    else:
                        consulta = consulta2
                        edo_consulta = edo_consulta2
                else:
                    consulta = consulta2
                    edo_consulta = edo_consulta2
        return consulta,edo_consulta 
    
    def obtener_clase_alumno(self,fecha_consulta,dia,hora):
        "Obtener la Clase del Alumno"
        clase = ""
        mensaje = ""
        consulta,edo_consulta = self.modelo.gpo_alum(self.usuario.get_clvUsu())
        if edo_consulta == "SUCCESS":
            if consulta:
                for gpo in consulta:
                    self.usuario.set_gpo(gpo[0])
                    # Buscamos La clave de la Materia en el Horario
                    consulta2,edo_consulta2 = self.obtener_clvhor_clvmat(fecha_consulta,dia,hora)
                    if edo_consulta2 == "SUCCESS":
                        if consulta2:
                            #consulta2[0][0] Clave del Horario ClvHorNov
                            #hora_materia = hora
                            #consulta2[0][1] Clave de la Materia ClvMatNov
                            self.usuario.guardar_datos_clase(self.usuario.get_gpo(),consulta2[0][1],hora,consulta2[0][0])
                            self.band_clase = True # Si hay Clase a esta Hora
                            
                            # Buscamos el Nombre de la Materia
                            consulta3,edo_consulta3 = self.modelo.nombre_materia(consulta2[0][1])
                            if edo_consulta3 == "SUCCESS":
                                if consulta3:
                                    clase = str (consulta3[0][0]) # Nombre de la Materia
                                else:
                                    clase = str (consulta2[0][1]) # Clave de la Materia (La Clave no esta relacionada con algun Nombre)
                                mensaje = ""
                                return clase,mensaje
                            else:
                                print "Fallo Consulta a Nombre de Materia"
                                clase = ""
                                mensaje = edo_consulta
                                self.band_clase = False
                                return clase,mensaje
                        else:
                            clase = "NO HAY CLASE A ESTA HORA"
                            mensaje = ""
                            self.band_clase = False # No hay Clase a esta Hora
                            #return clase,mensaje
                    else:
                        print "Fallo Consulta a Clase del Horario"
                        clase = ""
                        mensaje = edo_consulta
                        return clase,mensaje
            else:
                clase = "SIN GRUPO"
                mensaje = "EL ALUMNO NO TIENE UN GRUPO ASIGNADO"
        else:
            print "Fallo Consulta a Grupo del Alumno"
            clase = ""
            mensaje = edo_consulta
        return clase,mensaje
    
    def obtener_asist_alum(self,fecha_consulta):
        "Se Obtiene la Asistencia del Alumno para esa Clase"
        mensaje = ""
        asistencia = ""
        consulta,edo_consulta2 =self.modelo.buscar_asist_alum(self.usuario.get_clvHor(),fecha_consulta,self.usuario.get_clvUsu())
        if edo_consulta2 == "SUCCESS":
            if consulta:
                asistencia = "("+ str (consulta[0][5]) + ") " + str (consulta[0][4])
                self.asistencia_alumno = True
            else:
                asistencia = "Sin Asistencia"
                self.asistencia_alumno = False
        else:
            asistencia = "No se Puede Determinar"
        mensaje = edo_consulta2
        return asistencia,mensaje

        """************************************************************************************************"""
                                        # Metodos para Registrar la Asistencia del Alumno:
        """************************************************************************************************"""        

    def chck_asistencia(self):
        "Metodo para Registrar Asistencia del Usuario"
        (fecha_consulta,hora_consulta,dia,hora,minuto),edo_consulta = self.obtener_Hora_Fecha_Servidor()
        if edo_consulta == "SUCCESS":
            asistencia,res = self.registrar_asistencia(fecha_consulta,hora_consulta,dia,hora,minuto)
            if res == "FAILED_GET_IP_ASIST":
                self.vista.mensaje.update_prompt("IP no Valida")
            elif res == "SIN_CLASE":
                print "No se Hace Insercion en DB"
                self.vista.mensaje.update_prompt("No hay Clase para Registrar Asistencia")
            elif res == "ASISTENCIA_FALTA":
                print "No se Hace Insercion en DB"
                self.vista.mensaje.update_prompt("Tiempo excedido para Registrar Asistencia")
            elif res == "ASISTENCIA_DESTIEMPO":
                print "No se Hace Insercion en DB"
                self.vista.mensaje.update_prompt("La Clase ya Finalizo para Registrar Asistencia")                
            elif res == "SIN_INSERCION":
                print "No se Hace Insercion en DB"
                self.vista.mensaje.update_prompt("Ya se Tiene Registrada la Asistencia")
            else:
                self.vista.edo_asist.update_prompt(asistencia)
                self.vista.mensaje.update_prompt(res)
    
    def registrar_asistencia(self,fecha_consulta,hora_consulta,dia,hora,minuto):
        "Se Registra Asistencia del Alumno"
        # Si es True el alumno ya tiene Asistencia para esta Materia en este dia
        asistencia = ""
        edo_asistencia = ""
            
        if minuto >= 0 and minuto <=10:
            print "A"
            status = "A"
        elif minuto >10 and minuto <=40:
            print "R"
            status = "R"
        else:
            print "F"
            status = "F"
        
        if self.band_clase ==False:
            print "No Hay Clase a Esta Hora"
            edo_asistencia = "SIN_CLASE"
            return asistencia,edo_asistencia

        # Antes de Registrar Asistencia Corroboramos que no se haya registrado Asistencia del Alumno desde otro Equipo.
        self.obtener_asist_alum(fecha_consulta)
        if self.asistencia_alumno == True:
            print "EL alumno ya Tiene Asistencia para la Materia"
            asistencia = ""                
            edo_asistencia = "SIN_INSERCION"
        else:
            # Consultar si el Equipo ya fue usado para Registrar la Asistencia de un Alumno
            consulta,edo_consulta = self.modelo.buscar_ip_asist(self.usuario.get_clvHor(),fecha_consulta,self.usuario.get_IP())
            if edo_consulta == "SUCCESS":
                if consulta:
                    # "La IP ya esta ocupada.Favor de registrarse en otra maquina"
                    asistencia = "Sin Asistencia"
                    edo_asistencia = "La IP ya esta ocupada.Favor de registrarse en otra maquina"
                else:
                    # Hay Clase para registrar la Asistencia
                    if self.band_clase == True:
                        if self.usuario.hora_materia == hora:
                            # "En Tiempo para Registrar Asistencia"
                            if status == "A" or status == "R": 
                                edo_consulta = self.modelo.registrar_asistencia(self.usuario.get_clvUsu(),self.usuario.get_clvHor(),fecha_consulta,hora_consulta,status,self.usuario.get_IP())
                                if edo_consulta == "SUCCESS_QUERY_ATTENDANCE":
                                    # "Insercion hecha"
                                    consulta2,edo_consulta2 = self.obtener_asist_alum(fecha_consulta)
                                    if edo_consulta2 == "SUCCESS":
                                        asistencia = consulta2
                                        edo_asistencia = edo_consulta2
                                    else:
                                        asistencia = "Error al Obtener la Asistencia"
                                        edo_asistencia = edo_consulta2
                                else:
                                    print "Error en Insercion"
                                    asistencia = "Sin Asistencia"
                                    edo_asistencia = edo_consulta
                            else:
                                print "Minutos mayores a 40 No se Registra Asistencia"
                                asistencia = "Sin Asistencia"
                                edo_asistencia = "ASISTENCIA_FALTA"
                        else:
                            print "En Destiempo para Registrar Asistencia"
                            asistencia = "En Destiempo para Registrar Asistencia"
                            edo_asistencia = "ASISTENCIA_DESTIEMPO"
                    else:
                        print "No hay Asistencia que Marcar"
                        asistencia = "Sin Asistencia"
                        edo_asistencia = "SIN_INSERCION"
            else:
                print "No se Puede Consultar la IP en la Tabla de Asistencia"
                asistencia = "Sin Asistencia"                
                edo_asistencia = edo_consulta
        return asistencia,edo_asistencia
    
    """--------------------------------------Eventos-------------------------------------------------------"""
    def eventos_asistview(self):
        "Metodo para Los Eventos en la Vista de Asistencia"
        while True:
            # Empezamos a capturar la lista de Eventos
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Borramos Mensaje para el Usuario
                    self.vista.mensaje.update_prompt("")
                    x, y = event.pos
                    # Click en Boton de Registrar Asistencia
                    if self.vista.asistencia.collidepoint(x, y):
                        self.chck_asistencia()
                    
                    # Click en Boton de Regresar a Interfaz de Usuario 
                    elif self.vista.regresar.collidepoint(x, y):
                        access = "Usuario"
                        return access
            self.vista.surface()
            self.vista.refresh_display()