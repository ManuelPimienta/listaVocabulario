
# Leer un documento en todas las lineas
with open("source\prueba.txt", "r") as f:
    lista0 = [linea.strip() for linea in f]
    for line in f:
        # print(line.split())
        lista0.append(line.split())
        # print(line)
print(lista0)

lista1 = []
# lista0 = ['Hola mundo', 'Iteracion diccionario palabras', "Fuerza perseverancia"]

# Imprime el numero por indices de la lista 
for i in range(len(lista0)):
    lista1.append(lista0[i].split())
# lista1.append(lista0[0].split())
# lista1.append(lista0[1].split())
# lista1.append(lista0[2].split())
print(lista1)
# Hay que iterar sobre dos indices, el de la lista y el de las listas dentro de la lista pricipal. ej, 
# lista1[0][1]
# Esto itera sobre la lesta dentro de la otra e imprime todas la palabras
# for i in range(len(lista1[0])):
#     print(lista1[0][i])
# Iterar en cada lista dentro de la lista mayor.
for elements in range(len(lista1)):
    lts = int(elements)
    for i in range(len(lista1[lts])):
        ent = int(i)
        print(lista1[lts][ent])