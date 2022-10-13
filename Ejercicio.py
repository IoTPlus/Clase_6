#Ejercicio 1:
notas = open('notas.txt', 'r')
new_file = open('reporte.txt', 'w')

for linea in notas:
    new_line = linea.strip().split(':')
    nombre = new_line[0]
    grades = new_line[1:]
    int_grades = list(map(float, grades))
    average = sum(int_grades)/len(int_grades)
    if round(average, 2) < 4.0:
        new_file.write(f'{nombre} aprobado\n')
    else:
        new_file.write(f'{nombre} reprobado\n')

notas.close()
new_file.close()


