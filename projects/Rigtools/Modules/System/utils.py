import maya.cmds as mc
# Utilidades

def findAllModules(relativeDirectory):
	# Busca el archivo relativo para todos los modulos disponibles
	# devuelve una lista con todos los modulos y sus nombres (exluye el ".py")
	allPyFiles = findAllFiles(relativeDirectory,".py")

	returModules = []

	