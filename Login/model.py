# -*- coding: utf-8 *-*
'''
Created on 30/01/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
#import logging
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas

from Clases.DB_Connect import DB_Connect
DB_Connect = DB_Connect
# ------------------------------
# ------------------------------
# Funcion principal de la App
""" Modelo del Login"""
# ------------------------------


class modelo():
    def __init__(self,d):
        self.db = DB_Connect(d)
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

#-----------------------------------------------CONSULTAS------------------------------------------------------
    
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
    def validar_usuario_alumno(self,usuario,pwd):
        try:
            "Se Realiza la Consulta para validar el Usuario Alumno Logeado"            
            query = "SELECT * FROM TEntAluNov WHERE matAluNov=%s AND pasAluNov= MD5(%s)"
            values = (usuario,pwd)        
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta de Validar Alumno"
            #logging.critical('***No se Pudo Realizar la Consulta de Validar Alumno')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_VALIDATE")

    def validar_usuario_profesor(self,usuario,pwd):
        try:
            "Se Realiza la Consulta para validar el Usuario Profesor Logeado"
            query = "SELECT * FROM TEntProNov WHERE logProNov=%s AND pasProNov= MD5(%s)"
            values = (usuario,pwd)        
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta de Validar Profesor"
            #logging.critical('***No se Pudo Realizar la Consulta de Validar Profesor')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_VALIDATE")
                
    def validar_usuario_tecaux(self,usuario,pwd):
        try:
            "Se Realiza la Consulta para validar el Usuario TecAux Logeado"
            query = "SELECT * FROM TEntTecAux WHERE logTecAux=%s AND pasTecAux= MD5(%s)"
            values = (usuario,pwd)        
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta de Validar Asistente"
            #logging.critical('***No se Pudo Realizar la Consulta de Validar Asistente')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_VALIDATE")

    def hora_sistema(self):
        try:
            "Se Realiza la Consulta para Obtener la Hora del Servidor"        
            query = "SELECT CURRENT_TIMESTAMP()"
            values = ''
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta de Hora del Sistema"
            #logging.critical('***No se Pudo Realizar la Consulta de Hora del Sistema')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_GET_HOUR")

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

#-----------------------------------------------INSERCION------------------------------------------------------
    
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
    def registrar_inicio(self,clvUsuario,hora_inicio,IP_Equipo):
        try:
            "Se Realiza la Consulta del Registro de Inicio del Usuario"
            query = "INSERT INTO TUsuAulas (clvUsuNov,HorIniEquipo,IPEquipoAula) VALUES (%s,%s,%s)"
            values = (clvUsuario,hora_inicio,IP_Equipo)
            self.db.ejecutar(query,values)
            return "SUCCESS_QUERY_REGISTER"
        except(Exception), e:
            print "No se Pudo Realizar el Registro de Inicio de Sesion"
            #logging.critical('***No se Pudo Realizar el Registro de Inicio de Sesion')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return "FAILED_QUERY_REGISTER"