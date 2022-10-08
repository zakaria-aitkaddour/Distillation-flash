import math
Z1=0.1
Z2=0.2
Z3=0.3
Z4=0.4
k1=4.2
k2=1.75
k3=0.74
k4=0.34
ksi=0.12
eps=0.0001
F=100
Tf=200
Pf=100
F=100
ksi=0.12
eps=0.0001
def RR(Z1,Z2,Z3,Z4,k1,k2,k3,k4):
    Result = (((Z1*(1-k1))/(1+ksi*(k1-1)))+((Z2*(1-k2))/(1+ksi*(k2-1)))+((Z3*(1-k3))/(1+ksi*(k3-1)))+((Z4*(1-k4))/(1+ksi*(k4-1))))
    return Result
def RRD(Z1,Z2,Z3,Z4,k1,k2,k3,k4):
    Resultd=(Z1*(1-k1)**2)/((1+ksi*(k1-1)**2))+((Z2*(1-k2)**2)/((1+ksi*(k2-1))**2))+((Z3*(1-k3)**2)/((1+ksi*(k3-1))**2))+((Z4*(1-k4)**2)/((1+ksi*(k4-1))**2))
    return Resultd
fobj=RR(Z1,Z2,Z3,Z4,k1,k2,k3,k4)
while abs(fobj) >= eps:
    ksi1=ksi-(fobj/RRD(Z1,Z2,Z3,Z4,k1,k2,k3,k4))
    print(abs(fobj), ksi)
    ksi=ksi1
    eps=eps+0.0001

V=F*ksi
L = F - V
x1 = Z1 / (1 + ksi * (k1 - 1))
x2 = Z2 / (1 + ksi * (k2 - 1))
x3 = Z3 / (1 + ksi * (k3 - 1))
x4 = Z4 / (1 + ksi * (k4 - 1))
y1 = x1 * k1
y2 = x2 * k2
y3 = x3 * k3
y4 = x4 * k4
print("V est de ", V)
print("L est de ", L)
print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)
print("x4 =", x4)
print("y1 =", y1)
print("y2 = ", y2)
print("y3 =", y3)
print("y4 =", y4)

    


