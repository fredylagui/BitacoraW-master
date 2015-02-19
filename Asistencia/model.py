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
""" Modelo de Asist View"""
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
        
    def gpo_alum(self,matAluNov):
        try:
            "Se Realiza la Consulta para Obtener el Grupo del Alumno"
            query = "Select DISTINCT clvGpoNov FROM TAluMatNov WHERE matAluNov = %s"
            values = matAluNov
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta del Gpo del Alumno"
            #logging.critical('***No se Pudo Realizar la Consulta de Hora del Sistema')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_GET_GPO")        

    def clase_horario(self,clvGpoNov,diaHorNov,horHorNov):
        try:
            "Se Realiza la Consulta para Obtener la Clase del Alumno de esa Hora"
            query = "Select clvHorNov,clvMatNov FROM THorMatNov WHERE clvGpoNov=%s AND diaHorNov=%s AND horHorNov=%s"
            values = (clvGpoNov,diaHorNov,horHorNov)
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta de la Clase del Alumno"
            #logging.critical('***No se Pudo Realizar la Consulta de Hora del Sistema')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_GET_CLASS")
        
    def nombre_materia(self,clvMatNov):
        try:
            "Se Realiza la Consulta para Obtener el Nombre de la Materia"
            query = "Select nomMatNov FROM TEntMatNov WHERE clvMatNov=%s"
            values = clvMatNov
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta del Nombre de la Materia"
            #logging.critical('***No se Pudo Realizar la Consulta de Hora del Sistema')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_GET_MAT")
        
    def buscar_asist_alum(self,clvHorNov,fecAsiNov,matAluNov):
        try:
            "Se Realiza la Consulta para Obtener el status de la Asistencia del Alumno"
            query = "SELECT * FROM TAsiAluNov WHERE clvHorNov=%s AND fecAsiNov=%s AND matAluNov=%s"
            values = (clvHorNov,fecAsiNov,matAluNov)
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta del Status de la Asistencia"
            #logging.critical('***No se Pudo Realizar la Consulta de Hora del Sistema')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_GET_ASIST")
        
    def buscar_ip_asist(self,clvHorNov,fecAsiNov,ipAluNova):
        try:
            "Se Realiza la Consulta para Obtener el status de la Asistencia del Alumno"
            query = "SELECT * FROM TAsiAluNov WHERE clvHorNov=%s AND fecAsiNov=%s AND ipAluNova=%s"
            values = (clvHorNov,fecAsiNov,ipAluNova)
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta de lA IP en las Asistencias"
            #logging.critical('***No se Pudo Realizar la Consulta de Hora del Sistema')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_GET_IP_ASIST")
        
    def fecha_calendario(self,fecAsiNov):
        try:
            "Se Realiza la Consulta para Obtener el Estado de una Fecha en el Calendario Escolar"
            query = "SELECT staCalEsc, staCalEs2 FROM TEntCalEsc WHERE fecAsiNov =%s "
            values = fecAsiNov
            return (self.db.ejecutar(query,values),"SUCCESS")
        except(Exception), e:
            print "No se Pudo Realizar la Consulta en el Calendario Escolar"
            #logging.critical('***No se Pudo Realizar la Consulta de Hora del Sistema')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)
            return (None,"FAILED_GET_DATE_CALENDAR")

        
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#

#-----------------------------------------------INSERCION------------------------------------------------------
    
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-#
    def registrar_asistencia(self,matAluNov,clvHorNov,fecAsiNov,horIniAsi,staAluAsi,ipAluNov):
        try:
            "Se Realiza la Consulta del Registro Asistencia del Alumno"
            query = "INSERT INTO TAsiAluNov (matAluNov,clvHorNov,fecAsiNov,horIniAsi,staAluAsi,ipAluNova) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (matAluNov,clvHorNov,fecAsiNov,horIniAsi,staAluAsi,ipAluNov)
            self.db.ejecutar(query,values)
            return "SUCCESS_QUERY_ATTENDANCE"
        except(Exception), e:
            print "No se Pudo Realizar el Registro de Asistencia del Alumno"
            #logging.critical('***No se Pudo Realizar el Registro de Fin de Sesion')
            print "Tipo de Error:"
            print e
            cad = str (e)
            #logging.critical("Tipo de Error:")
            #logging.critical(cad)            
            return "FAILED_QUERY_ATTENDANCE"
