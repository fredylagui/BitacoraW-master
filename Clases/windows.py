'''
Created on 09/04/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import ctypes
#from ctypes import wintypes
from ctypes import *
import win32gui
# -----------
# Constantes
# -----------
SPI_GETFILTERKEYS = 0x0032;
SPI_SETFILTERKEYS = 0x0033;
SPI_GETTOGGLEKEYS = 0x0034;
SPI_SETTOGGLEKEYS = 0x0035;
SPI_GETSTICKYKEYS = 0x003A;
SPI_SETSTICKYKEYS = 0x003B;

SKF_STICKYKEYSON = 0x00000001;
TKF_TOGGLEKEYSON = 0x00000001;
SKF_CONFIRMHOTKEY = 0x00000008;
SKF_HOTKEYACTIVE = 0x00000004;
TKF_CONFIRMHOTKEY = 0x00000008;
TKF_HOTKEYACTIVE = 0x00000004;
FKF_CONFIRMHOTKEY = 0x00000008;
FKF_HOTKEYACTIVE = 0x00000004;

# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
# ------------------------------
# Descripcion de la Clase
""" Clase para Manejo de Elementos de Windows"""
# ------------------------------
class struct_skey(Structure):
    # Estructura para SKEY
    _fields_ = [("cbSize",ctypes.c_uint),
                ("dwFlags",ctypes.c_uint)]

class struct_sfilterkey(Structure):
    # Estructura para SFILTERKEY
    _fields_ = [("cbSize",ctypes.c_uint),
                ("dwFlags",ctypes.c_uint),
                ("iWaitMSec",ctypes.c_uint),
                ("iDelayMSec",ctypes.c_uint),
                ("iRepeatMSec",ctypes.c_uint),
                ("iBounceMSec",ctypes.c_uint)]     

class Windows():
    def __init__(self):
        #self.SKEYSize = ctypes.sizeof(ctypes.c_uint)*2
        self.FKEYSize = ctypes.sizeof(ctypes.c_uint)*6

        #self.SSTICKYKEY = struct_skey(self.SKEYSize,0)
        #self.STOGGLEKEY = struct_skey(self.SKEYSize,0)
        self.SFILTERKEY = struct_sfilterkey(self.FKEYSize,0)

        self.user32 = ctypes.WinDLL('user32.dll')
        self.SystemParametersInfo = self.user32.SystemParametersInfoW
        self.SystemParametersInfo.restype = wintypes.BOOL
        self.SystemParametersInfo.argtypes = [
                                              ctypes.c_uint,  #action
                                              ctypes.c_uint,  #param
                                              #POINTER(struct_skey),  #SKEY vparam
                                              POINTER(struct_sfilterkey),  #SKEY vparam
                                              ctypes.c_uint, #init
                                              ]

        self.StartupAccessibilitySet = False

        #self.SystemParametersInfo(SPI_GETSTICKYKEYS,self.SKEYSize,byref(self.SSTICKYKEY),0)
        #self.SystemParametersInfo(SPI_GETTOGGLEKEYS,self.SKEYSize,byref(self.STOGGLEKEY),0)
        self.SystemParametersInfo(SPI_GETFILTERKEYS,self.FKEYSize,byref(self.SFILTERKEY),0)
                        
    def Enable_Shorcut(self):
        "Metodo Para Habilitar El uso de Atajos en Win"
        #SK = self.SSTICKYKEY
        #TK = self.STOGGLEKEY
        FK = self.SFILTERKEY
        #self.SystemParametersInfo(SPI_SETSTICKYKEYS,self.SKEYSize,byref(SK),0)
        #self.SystemParametersInfo(SPI_SETTOGGLEKEYS,self.SKEYSize,byref(TK),0)
        self.SystemParametersInfo(SPI_SETFILTERKEYS,self.FKEYSize,byref(FK),0)
        
        
    def Disenable_Shorcut(self):
        "Metodo Para Deshabilitar El uso de Atajos en Win"
        #SK = struct_skey(self.SKEYSize,0)
        #TK = struct_skey(self.SKEYSize,0)
        #FK = struct_skey(self.FKEYSize,0)
        #SK = self.SSTICKYKEY
        #TK = self.STOGGLEKEY
        FK = self.SFILTERKEY
        # Se Hace un AND con Guardado en la Bandera dwFlags And (Negacion Bit a Bit SKF_HOTKEYACTIVE)
        print "Tamano de Registro",ctypes.sizeof(ctypes.c_uint)
        #print "SK.dwFlags: ",SK.dwFlags
        #print "SKF_HOTKEYACTIVE: ", SKF_HOTKEYACTIVE
        #print "~SKF_HOTKEYACTIVE: ", ~SKF_HOTKEYACTIVE
        
        #SK.dwFlags = SK.dwFlags and ~SKF_HOTKEYACTIVE
        #print "SK.dwFlags: ",SK.dwFlags
        #SK.dwFlags = SK.dwFlags and ~SKF_CONFIRMHOTKEY
        
        #TK.dwFlags = SK.dwFlags and ~TKF_HOTKEYACTIVE
        #TK.dwFlags = SK.dwFlags and ~TKF_CONFIRMHOTKEY
        
        print "FK.dwFlags: ",FK.dwFlags
        print "FKF_HOTKEYACTIVE: ", FKF_HOTKEYACTIVE
        print "~FKF_HOTKEYACTIVE: ", ~FKF_HOTKEYACTIVE
        
        FK.dwFlags = FK.dwFlags and ~FKF_HOTKEYACTIVE
        print "SK.dwFlags: ",FK.dwFlags
        
        print "FKF_CONFIRMHOTKEY: ", FKF_CONFIRMHOTKEY
        print "~FKF_CONFIRMHOTKEY: ", ~FKF_CONFIRMHOTKEY
        FK.dwFlags = FK.dwFlags and ~FKF_CONFIRMHOTKEY
        print "SK.dwFlags: ",FK.dwFlags
                
        #self.SystemParametersInfo(SPI_SETSTICKYKEYS,self.SKEYSize,byref(SK),0)
        #self.SystemParametersInfo(SPI_SETTOGGLEKEYS,self.SKEYSize,byref(TK),0)        
        self.SystemParametersInfo(SPI_SETFILTERKEYS,self.FKEYSize,byref(FK),0)
    
    def Show_taskbar(self):
        "Metodo para Mostrar Barra de Tareas de Windows"        
        handleW1 = win32gui.FindWindow("Shell_traywnd", None)
        win32gui.ShowWindow(handleW1, True)
    
    def Hide_taskbar(self):
        "Metodo para Ocultar Barra de Tareas de Windows"        
        handleW1 = win32gui.FindWindow("Shell_traywnd", None)
        win32gui.ShowWindow(handleW1, False)        

    def Show_starbutton(self):
        "Metodo para Mostrar Boton de Inicio de Windows"        
        buttonHandle = win32gui.FindWindowEx(None, None, "Button", None)
        win32gui.ShowWindow(buttonHandle, True)
        
    def Hide_starbutton(self):
        "Metodo para Mostrar Boton de Inicio de Windows"        
        buttonHandle = win32gui.FindWindowEx(None, None, "Button", None)
        win32gui.ShowWindow(buttonHandle, False)