
'''
Created on 10/02/2014

@author: Admin
'''
# -----------
# Librerias
# -----------
import sys, os.path, ctypes, ctypes.wintypes
# -----------
# Constantes
# -----------
# ------------------------------
# Clases y Funciones utilizadas
# ------------------------------
# ------------------------------
# Descripcion de la Clase
""" Clase para Manejo de Procesos de Windows"""
# ------------------------------


class Procesos():
    def __init__(self):
        self.Psapi = ctypes.WinDLL('Psapi.dll')
        self.EnumProcesses = self.Psapi.EnumProcesses
        self.EnumProcesses.restype = ctypes.wintypes.BOOL
        self.GetProcessImageFileName = self.Psapi.GetProcessImageFileNameA
        self.GetProcessImageFileName.restype = ctypes.wintypes.DWORD
    
        self.Kernel32 = ctypes.WinDLL('kernel32.dll')
        self.OpenProcess = self.Kernel32.OpenProcess
        self.OpenProcess.restype = ctypes.wintypes.HANDLE
        self.TerminateProcess = self.Kernel32.TerminateProcess
        self.TerminateProcess.restype = ctypes.wintypes.BOOL
        self.CloseHandle = self.Kernel32.CloseHandle

        self.MAX_PATH = 260
        self.PROCESS_TERMINATE = 0x0001
        self.PROCESS_QUERY_INFORMATION = 0x0400

        self.count = 256

    def Finalizar_Proceso(self,nombre_proceso):
        "Se Finaliza el Proceso dado en la variable nombre_proceso"
        resultado = self.Buscar_Proceso(nombre_proceso)
        if resultado == 1:
            self.TerminateProcess(self.hProcess, 1)
            self.CloseHandle(self.hProcess)
                
    def Buscar_Proceso(self,nombre_proceso):
        "Se busca el Proceso"
        while True:
            ProcessIds = (ctypes.wintypes.DWORD*self.count)()
            cb = ctypes.sizeof(ProcessIds)
            BytesReturned = ctypes.wintypes.DWORD()
            if self.EnumProcesses(ctypes.byref(ProcessIds), cb, ctypes.byref(BytesReturned)):
                if BytesReturned.value<cb:
                    break
                else:
                    self.count *= 2
            else:
                sys.exit("Call to EnumProcesses failed")
        
        for index in range(BytesReturned.value / ctypes.sizeof(ctypes.wintypes.DWORD)):
            ProcessId = ProcessIds[index]
            self.hProcess = self.OpenProcess(self.PROCESS_TERMINATE | self.PROCESS_QUERY_INFORMATION, False, ProcessId)
            if self.hProcess:
                ImageFileName = (ctypes.c_char*self.MAX_PATH)()
                if self.GetProcessImageFileName(self.hProcess, ImageFileName, self.MAX_PATH)>0:
                    filename = os.path.basename(ImageFileName.value)
                    if filename == nombre_proceso:
                        return 1
                self.CloseHandle(self.hProcess)
        return 0