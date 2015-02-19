# -*- coding: utf-8 *-*
'''
Created on 06/02/2014

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
# Funcion principal del codigo
""" Modelo de User View"""
# ------------------------------

class modelo():
    def __init__(self,d):
        self.db = DB_Connect(d)
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

#-----------------------------------------------CONSULTAS------------------------------------------------------
    
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
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

    def registrar_salida(self,clvUsu,hora_inicio,hora_salida,IP_Equipo):
        try:
            "Se Realiza la Consulta del Registro de Salida del Usuario"
            query = "UPDATE TUsuAulas SET HorFinEquipo = %s WHERE clvUsuNov=%s AND HorIniEquipo=%s AND IPEquipoAula=%s"
            values = (hora_salida,clvUsu,hora_inicio,IP_Equipo)
            self.db.ejecutar(query,values)
            return "SUCCESS_QUERY_REGISTER"
        except(Exception), e:
            print "No se Pudo Realizar el Registro de Fin de Sesion"
            #logging.critical('***No se Pudo Realizar el Registro de Fin de Sesion')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)            
            return "FAILED_QUERY_REGISTER"