lenguajes=['python','kotlin','java','javascript']
print(lenguajes)

#los arrays(list) comienzan en la posicion 0
print(lenguajes[0])

#0 ordenar los elementos 
lenguajes.sort()
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo) 

#modificando valores de un arreglo (se le cambia su valor por otro)
lenguajes[2] = 'php'
print(lenguajes)

#agregar elementos a un arreglo(list)
lenguajes.append('ruby')
print(lenguajes)

#eliminar de un arreglo (listas)
del lenguajes[1]
print(lenguajes)

#eliminar con pop una posicion en especifico 
lenguajes.pop(0)
print(lenguajes)


#se elimina un arreglo (lista) 
lenguajes.pop() # se eliminara el ultimo de la lista
print(lenguajes)

#eliminar por nombre 
lenguajes.remove('php')
print(lenguajes)




#eliminar c

