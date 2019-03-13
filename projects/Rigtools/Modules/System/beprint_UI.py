import maya.cmds as mc
#IP ADDRESS 192.168.1.19
'''
Esto es para llamar el UI o Interfase
 : Pablo Sepulveda
 : 3/07/2019


'''

class Beprint_UI:
	def __init__(self):
		#almacenamos elemntos en el dic del UI
		self.UIElements = {}

		if mc.window("beprint_UI_window", exists=True):
			mc.deleteUI("beprint_UI_window")

		windowWidth = 400
		windowHeight = 598

		self.UIElements["window"]= mc.window("beprint_UI_window", width=windowWidth, height=windowHeight, title= "Sepulveda Tools Believe UI", sizeable= False)
		#print"Estamos en el constructor C "


		#DISPLAY WIN//para la ventana
		mc.showWindow(self.UIElements["window"] )