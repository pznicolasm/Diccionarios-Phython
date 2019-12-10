def busquedaBinaria (lista, item):
    if len(lista) == 0:
        return False
    else:
        medio = len(lista) // 2
        if lista[medio] == item:
            return True
        else:
            if item < lista[medio]:
                return busquedaBinaria(lista[:medio], item)
            else:
                return  busquedaBinaria(lista[medio:], item)

listaprueba = [1,2,3,6,8,9,7,15,22,63,77,89,99]

item = 15

print(busquedaBinaria(listaprueba, 99))