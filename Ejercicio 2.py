#Ejercicio 2:
pacientes = open('pacientes.csv', 'r')
jovenes = open('jovenes.txt', 'w')
mayores = open('mayores.txt', 'w')

for linea in pacientes:
    new_line = linea.strip().split(';')
    if int(new_line[2]) < 30:
        jovenes.write(f'{new_line[1]} {new_line[0]}\n')
    elif int(new_line[2]) > 60:
        mayores.write(f'{new_line[1]} {new_line[0]}\n')

pacientes.close()
jovenes.close()
mayores.close()