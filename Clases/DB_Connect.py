# -*- coding: utf-8 *-*
'''
Created on 29/01/2014
@author: Admin
'''
import MySQLdb

class DB_Connect:

    def __init__(self,d):    
        self.db_host = d[0]
        self.db_port = int(d[1])
        self.db_user = d[2]
        self.db_pass = d[3]
        self.db_name = d[4]

    def conectar(self):
        """Crear una conexión con la base de datos"""
        self.db = MySQLdb.connect(host=self.db_host, port=self.db_port, user=self.db_user,
                              passwd=self.db_pass, db=self.db_name)


    def abrir_cursor(self):
        """Abrir un cursor"""
        self.cursor = self.db.cursor()

    def ejecutar_consulta(self, query, values=''):
        """Ejecutar una consulta"""
        if values != '':
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

    def traer_datos(self):
        """Traer todos los registros"""
        self.rows = self.cursor.fetchall()

    def send_commit(self, query):
        """Enviar commit a la base de datos"""
        sql = query.lower()
        es_lectura = sql.count('select')
        if es_lectura < 1:
            self.db.commit()

    def cerrar_cursor(self):
        """Cerrar cursor"""
        self.cursor.close()

    def cerrar_conexion(self):
        """Cerrar Conexion BD"""
        self.db.close()

    def ejecutar(self, query, values=''):
        """Compilar todos los procesos"""
        self.conectar()
        self.abrir_cursor()
        self.ejecutar_consulta(query, values)
        self.send_commit(query)        
        self.traer_datos()
        self.cerrar_cursor()
        self.cerrar_conexion()
        return self.rows
