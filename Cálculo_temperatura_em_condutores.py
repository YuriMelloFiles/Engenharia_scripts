# temperatura de um condutor

a=float(input("Insira o valor da temperatura do ambiente em graus(c°):  "))
b=float(input("Insira o valor da temperatura de isolação máxima do condutor em graus(c°):  "))
c=float(input("Insira o valor da corrente de cada condutor em Ampere (A):  "))
d=float(input("Insira o valor da corrente máxima do condutor em Ampere (A):  "))

Temp=(a+((b-a)*(c/d)**2))

print(" A temperatura no condutor será de : ",round(Temp,2),"°")
