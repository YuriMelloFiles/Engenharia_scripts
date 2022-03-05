#Operações com números complexos

import cmath
''' CALCULANDO A DIVISÃO ENTRE 2 COMPLEXOS RETANGULARES'''

m=float(input("Insira o valor real do primeiro número:  "))
n=float(input("Insira o valor imaginário do primeiro número:  "))
a=float(input("Insira o valor real do segundo número:  "))
b=float(input("Insira o valor imaginário do segundo número:  "))
x=complex(m,n)
y=complex(a,b)
divisao = x/y
print("\n")
print("O resultado da divisão em forma retangular é: ",divisao)
