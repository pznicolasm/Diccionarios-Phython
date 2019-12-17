def busquedaBinaria (lista, valor):
    if len(lista) == 0:
        return False
    else:
        medio = len(lista) // 2
        if lista[medio] == valor:
            return True
        else:
            if valor < lista[medio]:
                return busquedaBinaria(lista[:medio], valor)
            else:
                return  busquedaBinaria(lista[medio:], valor)

listaprueba = [1,2,3,6,8,9,7,15,22,63,77,89,99]

print(busquedaBinaria(listaprueba, 99))
