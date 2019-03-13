#IP ADDRESS 192.168.1.19
'''
solo para Set de la ruta en este computador
'''
#para este computador C:/projects/Rigtools
import os

try:
    riggingToolRoot= os.environ["RIGGING_TOOL_ROOT"]
except:
    print "RIGGING_TOOL_ROOT Entorno no configurado"
else:
     import sys
     print riggingToolRoot
     path = riggingToolRoot + "/Modules"
     
     if not path in sys.path:
         sys.path.append(path)
         
     print sys.path

     import System.beprint_UI as beprint_UI
     reload(beprint_UI)

     UI = beprint_UI.Beprint_UI()