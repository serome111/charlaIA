#!/usr/bin/python

class datos:
	def __init__(self):
		self.primeras50=[] #aqui se guardan todos los datos de entrada
		self.datosPreguta=[] #aqui se deben guardar los datos que hacen preguntas
		self.datosRespuesta=[] #aqui se guardan todas las respuestas
		self.datosPR={}	#aqui se guardan las preguntas con sus respuestas
		self.BuscarMayor=[] #aqui se agragan los numeros de repeticiones
		self.i=0
		self.pregunta=""
	def ensenar(self):
		for contador in range (0,6): #que se repita todo en un rango de ("1" a lo que ponga) entrenador
			self.primeras50.append(raw_input("Lord "))
		
		for contador in self.primeras50:
			self.i += 1
			count = self.primeras50.count(self.primeras50[self.i-1]) #contador de datos mas repetidos
			#print count
			#print "el dato ",self.primeras50[self.i-1],"se repite ",count, "veces "
			self.BuscarMayor.append(count)

		posicion = self.BuscarMayor.index(max(self.BuscarMayor)) #posicion del dato mas repetido
		self.pregunta=self.primeras50[posicion]
			
		print (contador)
		print (self.BuscarMayor)
		self.recordar()
	def recordar(self):
		print "pregunta aprendida -->",self.pregunta #datosRespuesta[0] #lo que aprende a decir
		res = raw_input("Lord:") #Pues aqui debe ir se supone el dato de respuesta a la pregunta
		self.datosPR[self.pregunta]=res
		print(self.datosPR)
		self.primeras50=[]
		self.i=0
		self.BuscarMayor=[]
		self.ensenar()
		

per=datos()
per.ensenar()
