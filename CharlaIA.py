 #!/usr/bin/python3
#######################################
##Creado por: Sebastian Roa meneses ###
#######################################
import sys
import os
import csv

if sys.platform == 'linux' or sys.platform == 'linux2':
	limpiarPantalla = 'clear'
elif sys.platform == 'Windows':
	limpiarPantalla = 'cls'
else:
	os.system('clear')
	limpiarPantalla = 'clear'

"""falta regresion lineal sobre cada pregunta y su respuesta para tener siempre la mejor respuesta
    falta agragar reconocimiento de voz, reconocimiento facial, argregar npl procesamiento de lenguaje natural, regresion lineal simple euristica etc...."""
class datos:
	def __init__(self):

		self.Nombre = "Serome"
		self.a="string"
		self.vacio=[] # lista vacia necesaria para comparacion triste pero real
		self.primeras50=[] # aqui se guardan todos los datos de entrada
		self.datosRespuesta=[] # respuestas que se le ensenaron
		self.datosPR={}
		self.BuscarMayor=[] # aqui se agragan los numeros de repeticiones
		self.i=0
		self.pregunta=""
		self.c=0
		self.aprende=["aprende esto","aprendizaje","se dice a si"] # en uso
		self.nuevaPOT=[] # nueva palabra o texto
	def yo(self):

		self.Nombre = input("Nombre :")

	def ensenar(self):
		for contador in range (0,6):
			self.a = input(" Lord: ")
			self.Sistema()
			self.Sobremi()
			self.aprender()
			if(self.a in self.datosPR): # si la palabra  ya tiene respuesta
				print ("",self.Nombre," --> ",self.datosPR[self.a]) # imprime la respuesta

			else: # si no la tiene
				self.primeras50.append(self.a) # agrega la palabra a la lista primeras50
				while self.i<contador: # mientras que 0 sea menor que contador
					break
		for contador in self.primeras50:
			self.i +=1
			count = self.primeras50.count(self.primeras50[self.i-1]) # cuenta el numero de veces que esta la palabra en primeras50
			self.BuscarMayor.append(count)

		if self.primeras50 == self.vacio: # si no existe ninguna palabra nueva preguntara de nuevo
			self.ensenar()
		posicion = self.BuscarMayor.index(max(self.BuscarMayor))
		self.pregunta=self.primeras50[posicion] # aqui va la pregunta que mas se repite :v
		self.recordar()
	def recordar(self):

		print (" ",self.Nombre, " --> ", self.pregunta) # datosRespuesta[0]
		self.datosRespuesta = input(" Lord: ")
		self.datosPR[self.pregunta]=self.datosRespuesta # aqui se guarda la pregunta y la respuesta
		self.csv()
		#print(self.datosPR)
		self.primras50=[]
		self.i=0
		self.BuscarMayor=[]
		while (self.pregunta in self.primeras50):
			self.primeras50.remove(self.pregunta)
		self.ensenar()
	def aprender(self):

		if (self.a == self.aprende[0] or self.a == self.aprende[1] or self.a == self.aprende[2]):
			print ("Genial necesito aprender dime")
			self.pregunta = input("Cual es la pregunta: ") # self.nuevaPOT
			self.datosRespuesta = input("cual es la respuesta: ")
			self.datosPR[self.pregunta]=self.datosRespuesta # aqui se guarda la pregunta y la respuesta self.nuevaPOT
			self.csv()
			self.ensenar()
	def Sistema(self):

		if (self.a == "salir"):
			self.almacenar() #antes de salir guarda todo
			exit()
		elif(self.a == "clear"):
			os.system('clear')
	def Sobremi(self):
		if self.a == "--help":
			print ("#############################")
			print ("##","  Palabras reservadas    ","##")
			print ("##","                         ","##")
			print ("##","  Preguntas y Respuestas ","##")
			print ("##","  -primeras50            ","##")
			print ("##","  Aprende esto           ","##")
			print ("##","  Se dice a si           ","##")
			print ("#############################")
		elif(self.a == "Preguntas y Respuestas"):
			print (self.datosPR)
		elif(self.a == "-primeras50"):
			print (self.primeras50)
		elif(self.a == "Guardar primeras50"): #esto no esta agregado en la vista pero se mejorara posteriormente
			self.almacenar()

	def csv(self): # este es utilizado para crear el csv y para anexar palabras nuevas
		archivo = csv.writer(open("Datos_De_Entrenamiento.csv","a", newline=''))#ab
		archivo.writerow([self.pregunta,self.datosRespuesta])

	def entrenar(self):
		archivo = csv.reader(open("Datos_De_Entrenamiento.csv","r"))
		for index,row in enumerate(archivo):
			self.datosPR[row[0]]=row[1]
			# print "pregunta", row[0]
			# print "respuesta",row[1]
	def almacenar(self):
		archivo_1 = csv.writer(open("primeras50.csv","a", newline=''))
		for index,row in enumerate(self.primeras50):
			archivo_1.writerow([self.primeras50[index]])
			cantidad = str(index+1)

		print ("se han Guardado ", cantidad, "datos")

	def entrenar2(self):

		archivo_3 = csv.reader(open("primeras50.csv","r"))
		for index,row in enumerate(archivo_3):
			self.primeras50.append(row[0])


per=datos()
print ("                 Bienvenido                       ")
print (" para iniciar por favor llene la informacion necesaria")
print (" ")
print (" Escribe el nombre que le daras a tu Robot")
per.yo()
print (" Deseas cargar datos de entrenamiento")
print (" Digite 'si' o 'no' ")
print ("")
pg= input("-->> ")
if(pg == "si"):
	per.entrenar()
	print (" Desea cargar las preguntas sin responder?")
	print (" Digite 'si o 'no'' ")
	pg2= input("-->> ")
	if(pg2 == "si"):
		per.entrenar2()

os.system('clear')
per.ensenar()
