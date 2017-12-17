#!/usr/bin/python
class datos:
	def __init__(self):
		self.a="string"
		self.primeras50=[] # aqui se guardan todos los datos de entrada
		self.datosRespuesta=[]
		self.datosPR={}
		self.BuscarMayor=[] # aqui se agragan los numeros de repeticiones
		self.i=0
		self.pregunta=""
		self.c=0
	def ensenar(self):
		for contador in range (0,6):
			self.a = raw_input("Lord:")
			if(self.a in self.datosPR): # si la palabra  ya tiene respuesta
				print self.datosPR[self.a]
				# while (self.a in self.primeras50):
					# self.primeras50.remove(self.a)

			else:
				self.primeras50.append(self.a)
				while self.i<contador:
					break
		for contador in self.primeras50:
			self.i += 1
			count = self.primeras50.count(self.primeras50[self.i-1]) # cuenta el numero de veces que esta la palabra en primeras50
			# print count
			# print "el dato ",self.primeras50[self.i-1],"se repite ",count, "veces "
			self.BuscarMayor.append(count)
			# print(self.primeras50[])

		posicion = self.BuscarMayor.index(max(self.BuscarMayor))
		self.pregunta=self.primeras50[posicion] # aqui va la pregunta que mas se repite :v
		print (contador)
		print (self.BuscarMayor)
		self.recordar()
	def recordar(self):

		print self.primeras50
		print ("palabra guardada en self.a",self.a)
		print "aprendio a decir -->",self.pregunta # datosRespuesta[0]
		res = raw_input("Lord:")
		self.datosPR[self.pregunta]=res
		# while (self.pregunta in self.primeras50):
			 # self.primeras50.remove(self.a)

		print(self.datosPR)
		self.primras50=[]
		self.i=0
		self.BuscarMayor=[]
		while (self.pregunta in self.primeras50):
			self.primeras50.remove(self.pregunta)
		self.ensenar()
		# while (a in sel.primeras50):
			# self.primeras50.remove(a)

per=datos()
per.ensenar()
