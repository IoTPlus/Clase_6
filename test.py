# Bloque B
archivo = open('alumnos.txt')

#1 Para eliminar separadores de palabras contenidos en el archivo, tipicamente , ; | :
for linea in archivo:
    line = linea.strip().split(':') #Nuevamente split() genera una lista de elementos y debemos indicar tal separador ':'
    print(line)

archivo.close()

#2 Paso Inverso: Usar separadores para juntar elementos (palabras y numeros) contenidos en una lista
lista = ['Juan', 'Perez', '100']

';'.join(lista)

#3 Funcion map es usada para convertir todos los elementos de una lista a un tipo de variable en especifico
list(map(int, ['10', '20', '30']))
list(map(str, [10, 20, 30]))
list(map(float, ['10.23', '20.23413545', '30.98']))

#4 Ejemplo en clase 1
archivo = open('alumnos.csv', 'r')
prom = open('promedios.txt', 'w')

for linea in archivo:
    lin = linea.strip().split(';')
    nombres = lin[:2]
    notas = list(map(int, lin[2:]))
    promedio = round(sum(notas)/len(notas))
    print(promedio)
    print(f'El alumno {nombres[0]} {nombres[1]} tiene un promedio: {promedio}')
    prom.write(f'El alumno {nombres[0]} {nombres[1]} tiene un promedio: {promedio}\n')
    #prom.write(';'.join([str(promedio), nombres[1], nombres[0], \n]))

archivo.close()
prom.close()