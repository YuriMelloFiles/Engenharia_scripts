#Operações com números complexos

import cmath

''' CONVERTENDO DE POLAR PARA RETANGULAR'''

m=float(input("Insira o valor do módulo do número:  "))
n=float(input("Insira o valor da fase do número:  "))
fase=(n*cmath.pi)/180
number=cmath.rect(m,fase)
print("\n")
print("O resultado em forma polar é:  ",number)
print("Da forma arredondada:",complex(round(number.real),round(number.imag)))
