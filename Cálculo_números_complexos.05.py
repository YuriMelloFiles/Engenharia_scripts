#Operações com números complexos

import cmath
''' CALCULANDO O PARALELO ENTRE 2 COMPLEXOS POLARES'''

m=float(input("Insira o valor do módulo do primeiro número:  "))
n=float(input("Insira o valor da fase do primeiro número:  "))
a=float(input("Insira o valor do módulo do segundo número:  "))
b=float(input("Insira o valor da fase do segundo número: "))

fase1=(n*cmath.pi)/180
fase2=(b*cmath.pi)/180
x=cmath.rect(m,fase1)
y=cmath.rect(a,fase2)
paralelo = (x*y)/(x+y)
print("\n")
print("O resultado em forma polar é:      ",round(abs(paralelo),3),"∟",
      round((cmath.phase(paralelo)*180/cmath.pi),3),"°")
