#Operações com números complexos

import cmath
''' CONVERTENDO DE RETANGULAR PARA POLAR '''


m=float(input("Insira o valor real do número:  "))
n=float(input("Insira o valor imaginário do número:  "))
x=complex(m,n)
print("\n")
print("O resultado em forma polar é:      ",round(abs(x),3),"∟",round((cmath.phase(x)*180/cmath.pi),3),"°")
