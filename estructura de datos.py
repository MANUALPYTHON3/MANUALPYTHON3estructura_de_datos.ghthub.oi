#aplicando las estructuras de repetición con las estructuras de datos

#listas
lista = [1, 2, 3]

for elemento in lista:
    print(elemento)
#tuplas

tupla = (1, 2, 3)

for elemento in tupla:
    print(elemento)
#diccionario

diccionario = {"nombre": "Juan", "edad": 30}

for clave, valor in diccionario.items():
    print(clave, valor)


#while
#listas
lista = [1, 2, 3]

i = 0
while i < len(lista):
    print(lista[i])
    i += 1

#tuplas
tupla = (1, 2, 3)

i = 0
while i < len(tupla):
    print(tupla[i])
    i += 1

#diccionario

diccionario = {"nombre": "Juan", "edad": 30}

i = 0
while i < len(diccionario):
    clave, valor = diccionario.items()[i]
    print(clave, valor)
    i += 1
