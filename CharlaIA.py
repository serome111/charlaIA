#!/usr/bin/python
primeras50=[] #aqui se guardan todos los datos de entrada
datosPreguta=[] #aqui se deben guardar los datos que hacen preguntas
datosRespuesta=[] #aqui se guardan todas las respuestas
datosPR=[] #aqui se guardan las preguntas con sus respuestas
BuscarMayor=[] #aqui se agragan los numeros de repeticiones
i = 0
print "Welcome Lord"
for contador in range (0,6): #que se repita todo en un rango de ("1" a lo que ponga)
#while  primeras50.append(raw_input("Lord: ")) != "exit":
	primeras50.append(raw_input("Lord "))

for contador in primeras50:
	i += 1
	count = primeras50.count(primeras50[i-1])
	#print "el dato ",primeras50[i-1],"se repite ",count, "veces "
	BuscarMayor.append(count)
	#if max(BuscarMayor) == max(BuscarMayor):
	#datosRespuesta.append())
		#print (BuscarMayor)
posicion = BuscarMayor.index(max(BuscarMayor)) #posicion del dato mas repetido
datosRespuesta.append(primeras50[posicion])
print "aprendio a decir -->",datosRespuesta[0]
