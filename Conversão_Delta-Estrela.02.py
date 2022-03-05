#Conversão de estrela para delta

R1=float(input("Insira o valor de R1:"))
R2=float(input("Insira o valor de R2:"))
R3=float(input("Insira o valor de R3:"))

RA=((R1*R2)+(R2*R3)+(R3*R1))/R1
RB=((R1*R2)+(R2*R3)+(R3*R1))/R2
RC=((R1*R2)+(R2*R3)+(R3*R1))/R3

print("RA é:",round(RA,1),"Ω")
print("RB é:",round(RB,1),"Ω")
print("RC é:",round(RC,1),"Ω")
