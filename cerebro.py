from flask import Flask, render_template, request,redirect,url_for,jsonify,make_response
from flask_mysqldb import MySQL

class cerebro:
	def __init__(self):

		self.Nombre = "Serome"
		self.palabra="string"
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

	def pruebas(self,palabra):
		self.palabra = palabra
		print(palabra)

	def transmisor(self,palabra):
		self.palabra = palabra
		self.sistema(palabra)
		# self.aprender()
		# if(self.a in self.datosPR): # si la palabra  ya tiene respuesta
		# 	print ("",self.Nombre," --> ",self.datosPR[self.a]) # imprime la respuesta

		# else: # si no la tiene
		# 	self.primeras50.append(self.a) # agrega la palabra a la lista primeras50
		# 	while self.i<contador: # mientras que 0 sea menor que contador
		# 		break
		# for contador in self.primeras50:
		# 	self.i +=1
		# 	count = self.primeras50.count(self.primeras50[self.i-1]) # cuenta el numero de veces que esta la palabra en primeras50
		# 	self.BuscarMayor.append(count)

		# if self.primeras50 == self.vacio: # si no existe ninguna palabra nueva preguntara de nuevo
		# 	self.ensenar()
		# posicion = self.BuscarMayor.index(max(self.BuscarMayor))
		# self.pregunta=self.primeras50[posicion] # aqui va la pregunta que mas se repite :v
		# self.recordar()

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

	def sistema(self,palabra):
		print(palabra)
		if (palabra == "salir"):
			print('Apagando sistema')
			return redirect(url_for('Index'))
		

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
