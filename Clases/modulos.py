'''
Created on 10/06/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import sys
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
# ------------------------------
# Descripcion de la Clase
""" Clase para Cargar Configuracion para Modulos Extras al Codigo"""
# ------------------------------

class Modulo():
    def __init__(self,sistemaop):
        self.sistemaop = sistemaop

        if sistemaop == "linux2":
            self.file = "/opt/BitacoraL/src/files/modulo"
        else:
            self.file = "C:/Program Files/Bitacora/src/files/modulo"
        
        # Apuntar al Archivo
        self.f = None
        
        # Listas para Guardar Tags y Datos del Archivo
        self.lista_tags = []
        self.lista_datos = []
        
    def abrir_archivo(self,modo):
        "Metodo para Abrir Archivo"
        try:
            self.f = open(self.file,modo)
        except Exception:
            print "No se Abrio Archivo"
            self.f = None
            
    def leer_datos(self,tag):
        "Metodo para Buscar el Tag en el Archivo y leer el contenido"
        self.abrir_archivo("r")
        etiqueta = ""
        cad = ""
        data = self.f.readline()
        try:
            while data != "":
                etiqueta = data[:data.find("]")+1]
                tmp = data[data.find("]")+1:]
                # Buscamos en el Archivo el Tag
                if etiqueta == tag:
                    # Obtenemos el Contenido del Tag
                    cad = tmp[tmp.find("[")+1:]
                    cad = cad[:cad.find("]")]
                    return cad
                else:
                    etiqueta = ""
                    cad = ""
                data = self.f.readline()
        except Exception:
            print "No se Abrio Archivo para Leer"
            self.f = None

        self.f.close()
        return data

    def guardar_tag_dato(self,etiqueta,dato):
        "Metodo para Actualizar Archivo"
        self.guardar_datos_archivo()
        
        self.abrir_archivo("w")
        cont = 0
        # Por cada Tag se agrega el valor encriptado en el Archivo
        for tag in self.lista_tags:
            if tag == etiqueta:
                linea = tag +" = [" + dato + "]\n"
            else:
                linea = tag +" = [" + self.lista_datos[cont] + "]\n"
            self.f.write(linea)
            cont += 1
        self.f.close()

    def guardar_datos_archivo(self):
        "Metodo para Respaldar los Datos del Archivo"
        self.abrir_archivo("r")
        data = self.f.readline()
        try:
            while data != "":
                self.lista_tags.append(data[:data.find("]")+1])
                tmp = data[data.find("]")+1:]
                cad = tmp[tmp.find("[")+1:]
                self.lista_datos.append(cad[:cad.find("]")])
                data = self.f.readline()
        except Exception:
            print "No se Abrio Archivo para Leer"
            self.f = None        
        
if __name__ == "__main__":
    sistemaop = sys.platform
    inicio = Modulo(sistemaop)
    #cadena = inicio.leer_datos("[asistencia]")
    #print cadena
    inicio.guardar_tag_dato("[asistencia]", "True")
