#cálculo de conversão de delta para estela

RA=float(input("Insira o valor de RA:"))
RB=float(input("Insira o valor de RB:"))
RC=float(input("Insira o valor de RC:"))

R1=(RB*RC)/(RA+RB+RC)
R2=(RA*RC)/(RA+RB+RC)
R3=(RB*RA)/(RA+RB+RC)

print("R1 é:",round(R1,1),"Ω")
print("R2 é:",round(R2,1),"Ω")
print("R3 é:",round(R3,1),"Ω")
