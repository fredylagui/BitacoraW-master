'''
Created on 26/03/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import re
import os
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
# ------------------------------
# Funcion principal de la Aplicacion
# ------------------------------


class filtro():
    
    def __init__(self):
        # Cadena Ingresada por Usuario
        self.input = ""
        # Diccionarios para filtrar de la Cadena Input
        self.signs = {"punto":".","barra":"/","comillas":"'","igual":"=","barrai":"\\","asterisco":"*","comillad":"\"","puntoc":";","porcentaje":"%"}
        self.reserved_words = {"select":"select","while":"while","from":"from","delete":"delete","truncate":"truncate","table":"table","update":"update","insert":"insert","drop":"drop","like":"like","where":"where","order":"order","where":"by","or":"or","and":"and","count":"count"}

    def filtrar_cadena(self,cadena):
        "Metodo en Filtrar la Cadena"
        self.input = cadena
        self.borrar_caracteres()
        self.borrar_palabras_reservadas()
        return self.input
        
    def borrar_caracteres(self):
        "Metodo que Limpia la Cadena de Caracteres no Permitidos"
        pos = 0
        for key in self.signs.keys():
            pos = self.input.find(self.signs[key])
            while pos >= 0:
                if pos >= 0:
                    cad1 = self.input[:pos]
                    cad2 = self.input[pos+1:]
                    self.input =  cad1+cad2
                pos = self.input.find(self.signs[key])
            pos = 0

    def borrar_palabras_reservadas(self):
        "Metodo que Limpia la Cadena de Palabras reservadas"
        for key in self.reserved_words.keys():
            # Se borra la Palabra Reservada al Inicio de la Cadena
            cad = '^'+self.reserved_words[key]+'(\s)'
            patron = re.compile(str(cad), re.I)
            self.input = patron.sub(" ", self.input)
            
            # Se borra la Palabra Reserveda en medio de la Cadena
            cad = '(\s)'+self.reserved_words[key]+'(\s)'
            patron = re.compile(str(cad), re.I)
            self.input = patron.sub("", self.input)
            
            # Se borra la Palabra Reservada al Final de la Cadena
            cad = '(\s)'+self.reserved_words[key]+'$'
            patron = re.compile(str(cad), re.I)
            self.input = patron.sub("", self.input)