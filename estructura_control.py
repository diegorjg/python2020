# if
if True:
    print('Imprimo esto porque la evaluacion fue verdadera')
# tenemos que dejar el espacio para respetar la gerarquia 
Alvaro = 10
if Alvaro == 10:
    print('Alvaro Vale 10')
if Alvaro == 12:
    print('Alvaro Vale 12')

# if elfi else 


final = float(input('coloca la nota: '))

if final >= 11 :
    print("valor euivocado la nota va de 1 a 10")
   
elif final >= 9 :
    print('sos un genio')
elif final >= 7:
    print('Aprobaste!')
elif final == 6:
    print('Te falto poco!')
elif final <= 5:
    print('Tuviste que haber estudiando en el curso de Python de Alvaro!')
    
else:   
    print('No se donde estudias porque la nota que pusiste no la puedoi evaluar')