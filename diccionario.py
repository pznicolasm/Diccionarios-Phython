diccionario = {'nombre' : 'nicolas', 'DNI' : 33222666, 'carreras' : ['diseno', 'analisis'] }

#Imprime cada key y su correspondiente valor del diccionario
for key in diccionario:
    print (key, ":", diccionario[key])

diccionario_dict = dict(nombre = 'nicolas', DNI = 33222666, carreras = ['diseno', 'analisis'])

diccionario_zip = dict(zip('abcd',[1,2,3,4]))

items = diccionario.items()

keys = diccionario.keys()

diccionario_fromkeys = dict.fromkeys(['a','b','c','d'],1)

get = diccionario.get('nombre')

pop = diccionario.pop('nombre')

setdefault = diccionario.setdefault('ciudad', 'la plata')

print ("\n Diccionario", diccionario)
print ("\n Metodo DICT: ", diccionario_dict)
print ("\n Metodo ZIP: ", diccionario_zip)
print ("\n Metodo ITEMS:", items)
print ("\n Metodo KEYS: ",keys)
print ("\n Metodo CLEAR: Elimina todos los items del diccionario dejandolo vacio")
print ("\n Metodo COPY: REtorna una copia del diccionario original")
print ("\n Metodo FROMKEYS: ", diccionario_fromkeys)
print ("\n Metodo GET: ", get," devuelve el valor de key pasado por paramtro")
print ("\n Metodo POP: ", pop," devuelve la key pasada por parametro y a la vez la elimina")
print ("\n Metodo SETDEFAULT: ", diccionario, " Agrega un nuevo elemento al diccionario")
print ("\n Metodo UPDATE: recibe como parametro otro diccionario, si tiene keys iguales, actualiza el valor de la key repetida y si no, la agrega al diccionario", )