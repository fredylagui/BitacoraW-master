'''
Created on 30/05/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
from pyDes import *
# ------------------------------
# Descripcion de la Clase
""" Clase para Encriptar Informacion"""
# ------------------------------



class Encriptador():
    def __init__(self,sistemaop,tags,archivo):
        "Init de Class"
        self.k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
        self.etiquetas = tags
        
        self.sistemaop = sistemaop

        self.file = archivo

        # Apuntar al Archivo
        self.f = None

    def actualizar_lista_tags(self,lista_tags):
        self.etiquetas = lista_tags
        
    def actualizar_nombre_archivo(self,archivo):
        self.file = archivo
    
    def encriptar(self,data):
        "Metodo para Encriptar"
        d = self.k.encrypt(data)
        return d
        
    def desecriptar(self,data):
        "Metodo para Desencriptar"
        d = self.k.decrypt(data)
        return d

    def abrir_archivo(self,modo):
        "Metodo para Abrir Archivo"
        try:
            self.f = open(self.file,modo)
        except Exception:
            print "No se Abrio Archivo"
            self.f = None

    def actualizar_archivo(self,lista):
        "Metodo para Actualizar Archivo"
        self.abrir_archivo("w")
        cont = 0
        # Por cada Tag se agrega el valor encriptado en el Archivo
        for tag in self.etiquetas:
            data = self.encriptar(lista[cont])
            d = "["
            # Guardamos el valor entero del caracter ASCII en el Archivo
            for caracter in data:
                d += str( ord(caracter)) + ","
            d += "]"
            linea = tag + d + "\n"
            self.f.write(linea)
            cont += 1
            
        self.f.close()
        
    def leer_datos(self):
        "Metodo para leer los valores de los tags"
        self.abrir_archivo("r")
        lista_datos = []
        datos = ""
        tmp = ""
        # Por cada Tag leemos el valor guardado en el Archivo
        for tag in self.etiquetas:
            datos = self.leer_tag(tag)
            tmp = ""
            # Pasamos a Caracter el valor entero que se guardo en el Archivo
            while datos != "":
                tmp += chr(int(datos[:datos.find(",")]))
                datos = datos[datos.find(",")+1:]
            #print "Decrypted: %r" % self.desecriptar(tmp)
            lista_datos.append(self.desecriptar(tmp))
        
        self.f.close()
        return lista_datos
    
    def leer_tag(self,tag):
        "Metodo para Buscar el Tag en el Archivo y leer el contenido"
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