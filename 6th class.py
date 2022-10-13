#Bloque A:

#1 Leer, crear, modificar archivos
archivo = open('../quijote.txt') #Dentro del argumento debo poner la ruta completa del archivo
                              #Si el archivo esta en el mismo directorio que mi proyecto solo debo usar el nombre.
                              #Por defecto es 'r' de read

archivo = open('../quijote.txt', 'w') #Escribir el archivo desde cero
#Tambien sirve para crear un archivo con tal nombre.

archivo = open('../quijote.txt', 'a') #Escribe un texto nuevo al final del ya existente.

#Siempre despues de crear, leer o modifificar un archivo se debe cerrar:
archivo.close()

#2 Recorrer el archivo
archivo = open('../quijote.txt')

for linea in archivo:
    print(linea)

archivo.close()

for linea in archivo:
    linea = linea.strip()   #Quita los saltos de linea
    print(linea)

archivo.close()

for linea in archivo:
    linea = linea.strip().upper()   #Imprime cada linea con letras en mayuscula
    print(linea)

archivo.close()

#3 Crear archivo y escribir cada linea que lo compone:
archivo = open('quijote_nuevo.txt', 'w')
archivo.write('En un lugar de la mancha\n')
archivo.write('de cuyo nombre no quiero acordarme\n')
archivo.write('no ha mucho tiempo que vivia un hidalgo\n')
archivo.close()

#4 Trabajo en clases 1 (Contar cantidad de letras, palabras y lineas que hay en el archivo):
archivo = open('../quijote.txt')
lineas = 0
palabras = 0
letras = 0

for linea in archivo:
    lineas += 1     #Añade uno por cada fila que itera.
    letras += len(linea.strip().replace(' ', '')) #Suma el numero de letras por linea omitiendo los espacios.
    #palabras = linea.strip().split()    #Convierte cada linea a un string conteniendo todas las palabras.
    #palabras = len(linea.strip().split()) #Calcula la cantidad de elementos en la lista.
    palabras += len(linea.strip().split()) #Suma el numero de palabras por linea.

archivo.close()

print('La cantidad de letras en el archivo es: ',letras)
print('La cantidad de lineas en el archivo es: ', lineas)
print('La cantidad de palabras en el archivo es: ', palabras)



#2 Escribir en archivo nuevo reportes.text la ciudad y sus temperaturas minima y maxima como un solo string.
temp = {
	'Vina del mar': (9, 26),
	'Valparaiso': (10, 24),
	'Quilpue': (7, 30),
	'Quintero': (4, 22)
}
archivo = open('reportes.txt', 'w')

for ciudad, temperaturas in archivo.items():
    #print(ciudad, ': max ', temperaturas[1], ', min ', temperaturas[0]) #Para imprimir en pantalla como se escribirá en el archivo
    linea = ciudad + ': max ' + str(temperaturas[1]) + 'min ' + str(temperaturas[0] + '\n')
    archivo.write(ciudad, ': max ', temperaturas[1], ', min ', temperaturas[0], '\n') #Forma 1
    #archivo.write(f'{ciudad}: max  {temperaturas[1]}, min {temperaturas[0]} \n') #Forma 2

archivo.close()