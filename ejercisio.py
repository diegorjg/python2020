print('Elige tu propio camino')
inicio = input("Escribe empezar para iniciar el programa: ")
while (inicio == 'empezar'):
    print(""" ¿Que camino quieres elegir?
    escribe la opcion con numero
    1 - Quiero que me saludes
    2 - Deseo multiplicar ya que no se como hacerlo
    3 - quiero salir de este programa, ya que aprendi a multiplicar con el curso de Alvaro """)
    opcion = input()
    if opcion == '1':
        print("Te saludo")
    elif opcion == '2':
        numero1 = float(input('introduce el valor a multiplicar primero: '))
        numero2 = float(input('introduce el valor a multiplicar segundo: '))
        print('El resultado es: ', numero1*numero2)
    elif opcion == '3':
        print('Excelente decision que hayas tomado el curso de alvaro')
        break
    else:
        print('No se que elegiste, tuviste que haber puesto algun numero de las opciones, se nota que no tomaste el curso de alvaro')
        