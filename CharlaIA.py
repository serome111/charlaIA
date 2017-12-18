 
#!/usr/bin/python
#######################################
##Creado por: Sebastian Roa meneses ###
#######################################
import sys
"""falta regresion lineal sobre cada respuesta para tener siempre la mejor respuesta
    falta agragar reconocimiento de voz, reconocimiento facial, etc...."""
class datos:
	def __init__(self):
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
	def ensenar(self):
		for contador in range (0,6):
			self.a = raw_input("Lord:")
			self.Sistema()
			self.Sobremi()
			self.aprender()
			if(self.a in self.datosPR): # si la palabra  ya tiene respuesta
				print self.datosPR[self.a] # imprime la respuesta

			else: # si no la tiene
				self.primeras50.append(self.a) # agrega la palabra a la lista primeras50
				while self.i<contador: # mientras que 0 sea menor que contador
					break
		for contador in self.primeras50:
			self.i +=1
			count = self.primeras50.count(self.primeras50[self.i-1]) # cuenta el numero de veces que esta la palabra en primeras50
			#print self.primeras50
			self.BuscarMayor.append(count)
			#print self.BuscarMayor

		if self.primeras50 == self.vacio: # si no existe ninguna palabra nueva preguntara de nuevo
			self.ensenar()
		posicion = self.BuscarMayor.index(max(self.BuscarMayor))
		self.pregunta=self.primeras50[posicion] # aqui va la pregunta que mas se repite :v
		self.recordar()
	def recordar(self):

		# print self.primeras50
		# print ("palabra guardada en self.a",self.a)
		print "aprendio a decir -->",self.pregunta # datosRespuesta[0]
		res = raw_input("Lord:")
		self.datosPR[self.pregunta]=res
		#print(self.datosPR) ###############################################
		self.primras50=[]
		self.i=0
		self.BuscarMayor=[]
		#print ("Este es self.datosRespuesta" , self.datosRespuesta)
		while (self.pregunta in self.primeras50):
			self.primeras50.remove(self.pregunta)
		self.ensenar()
	def aprender(self):

		if (self.a == self.aprende[0] or self.a == self.aprende[1] or self.a == self.aprende[2]):
			print "Genial necesito aprender dime"
			self.nuevaPOT = raw_input("Cual es la pregunta: ")
			self.datosRespuesta = raw_input("cual es la respuesta: ")
			self.datosPR[self.nuevaPOT]=self.datosRespuesta # aqui se guarda la pregunta y la respuesta
			self.ensenar()
	def Sistema(self):

		if (self.a == "salir"):
			exit()
	def Sobremi(self):
		if self.a == "--help":
			print ("#############################")
			print "##","  Palabras reservadas    ","##"
			print "##","                         ","##"
			print "##","  Preguntas y Respuestas ","##"
			print "##","  -Primeras50            ","##"
			print "##","  Aprende esto           ","##"
			print "##","  Se dice a si           ","##"
			print ("#############################")
		elif(self.a == "Preguntas y Respuestas"):
			print self.datosPR
		elif(self.a == "-primeras50"):
			print self.primeras50


per=datos()
per.ensenar()
