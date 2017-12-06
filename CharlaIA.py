#!/usr/bin/python
class datos:
	def __init__(self):
		self.a="string"
		self.primeras50=[] #aqui se guardan todos los datos de entrada
		self.datosRespuesta=[]
		self.datosPR={}
		self.BuscarMayor=[] #aqui se agragan los numeros de repeticiones
		self.i=0
		self.pregunta=""
		self.c=0
	def ensenar(self):
		for contador in range (0,6):
			a = raw_input("Que ordenas mi Lord:")
			if(a in self.datosPR): # si la palabra  ya tiene respuesta
				print self.datosPR[a]
				while (a in self.primeras50):
					self.primeras50.remove(a)

			else:
				self.primeras50.append(a)
				while self.i<contador:
					break
		for contador in self.primeras50:
			self.i += 1
			count = self.primeras50.count(self.primeras50[self.i-1])
			#print count
			#print "el dato ",self.primeras50[self.i-1],"se repite ",count, "veces "
			self.BuscarMayor.append(count)
			#print(self.primeras50[])

		posicion = self.BuscarMayor.index(max(self.BuscarMayor))
		n=self.pregunta=self.primeras50[posicion]
		#print (self.primeras50())
			#drop propiedades de las listas
			#npl procesamiento de lenguaje natutral
			#regresion lineal simple 3euristica
		print (contador)
		print (self.BuscarMayor)
		self.recordar()
	def recordar(self):
		print "aprendio a decir -->",self.pregunta # datosRespuesta[0]
		res = raw_input("Lord:")
		self.datosPR[self.pregunta]=res
		print(self.datosPR)
		self.primras50=[]
		self.i=0
		self.BuscarMayor=[]
		self.ensenar()

per=datos()
per.ensenar()
