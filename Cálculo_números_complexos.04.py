#Operações com números complexos

import cmath
''' CALCULANDO O PARALELO ENTRE 2 COMPLEXOS RETANGULARES'''

m=float(input("Insira o valor real do primeiro número:  "))
n=float(input("Insira o valor imaginário do primeiro número:  "))
a=float(input("Insira o valor real do segundo número:  "))
b=float(input("Insira o valor imaginário do segundo número:  "))
x=complex(m,n)
y=complex(a,b)
paralelo = (x*y)/(x+y)
print("\n")
print("O resultado do paralelo em forma retangular é: ",paralelo)
print("Da forma arredondada:",complex(round(paralelo.real),round(paralelo.imag)))
