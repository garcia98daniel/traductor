
def traducir(palabras_a_traducir):
    diccionarioENG={'i':1 , 'run':2 , 'fast':3};
    diccionarioSPA={1:'yo' , 2:'correr' , 3:'rapido'};
    cadenaTraducida=""

    for x in palabras_a_traducir:
	     	print(diccionarioSPA[diccionarioENG[x]])
  

