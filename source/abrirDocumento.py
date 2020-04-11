# Programa para crear una lista de palabras desconocidas

### TO-DO
# Abrir documento palabras comunes
# Comparar

# Lista palabras comunes
comunes = []

listaFinal = []
#Leer un documento en todas las lineas
with open("source\prueba.txt", "r", encoding="utf-8") as f:
    # Lista de palabras extraidas del documento
    lista0 = [linea.strip() for linea in f]
    for line in f:
        lista0.append(line.split())
f.close()
with open("source\palabrasComunes.txt", "r", encoding="utf-8") as f2:
    # Lista de palabras extraidas del documento
    lista3 = [linea.strip() for linea in f2]
    for line in f2:
        print(line)
        lista3.append(line.split())
f2.close()
print("Palabras comunes: ", lista3)
# Lista con otras listas por linea de palabras en el documento
lista1 = []

# Imprime el numero por indices de la lista 
for i in range(len(lista0)):
    lista1.append(lista0[i].split())

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
        # Esta salida hay que agregarla a la lista final
        # Crear un bucle de comprobacion
        # Si la palabra esta en la lista "comunes", entonces ignorar, sino añadir a la lista final
        # print(lista1[lts][ent])
        if lista1[lts][ent].lower().strip(",") in lista3:
            print("Palabra repetida" + " " + lista1[lts][ent].lower())
        else:
            listaFinal.append(lista1[lts][ent])
        
print(listaFinal)