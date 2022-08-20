import numpy as np
import matplotlib.pyplot as plt
import math

#============= Ganho ===================
w = np.linspace(-2,2,1000)
R = 1000
C = 0.001
ganho1 = abs(1/(R*C*w * 1j + 1))
R = 1000
C = 0.01
ganho2 = abs(1/(R*C*w * 1j + 1))
R = 500
C = 0.001
ganho3 = abs(1/(R*C*w * 1j + 1))
R = 500
C = 0.01
ganho4 = abs(1/(R*C*w * 1j + 1))

plt.figure(figsize=(8,8))
plt.title(r"g($\omega$) para Diferentes Valores de R e C", fontsize=20)
plt.plot(w, ganho3, label=r'g($\omega$) para R=500 $\Omega$ e C=0.001 F', color='r')
plt.plot(w, ganho1, label=r'g($\omega$) para R=1000 $\Omega$ e C=0.001 F', color='b')
plt.plot(w, ganho4, label=r'g($\omega$) para R=500 $\Omega$ e C=0.01 F', color='y')
plt.plot(w, ganho2, label=r'g($\omega$) para R=1000 $\Omega$ e C=0.01 F', color='g')
plt.legend(loc="lower center", fontsize="xx-large")
plt.ylabel("Ganho")
plt.xlabel(r"$\omega$ [rad/s]")
plt.show()

#============= Diagrama de Bode =======
w = np.logspace(-3,2, 1000)

R = 1000
C = 0.001
ganho1 = abs(1/(R*C*w * 1j + 1))
R = 1000
C = 0.01
ganho2 = abs(1/(R*C*w * 1j + 1))
R = 500
C = 0.001
ganho3 = abs(1/(R*C*w * 1j + 1))
R = 500
C = 0.01
ganho4 = abs(1/(R*C*w * 1j + 1))

A1 = 20*np.log10(ganho1)
A2 = 20*np.log10(ganho2)
A3 = 20*np.log10(ganho3)
A4 = 20*np.log10(ganho4)

plt.figure(figsize=(14,8))
plt.title(r"Magnitude de g($\omega$) para Diferentes Valores de R e C", fontsize=20)
plt.plot(w, A3, label=r'magnitude para R=500 $\Omega$ e C=0.001 F', color='r')
plt.plot(w, A1, label=r'magnitude para R=1000 $\Omega$ e C=0.001 F', color='b')
plt.plot(w, A4, label=r'magnitude para R=500 $\Omega$ e C=0.01 F', color='y')
plt.plot(w, A2, label=r'magnitude para R=1000 $\Omega$ e C=0.01 F', color='g')
plt.legend(loc="lower left", fontsize="xx-large")
plt.xscale("log")
plt.ylabel("Magnitude (dB)")
plt.xlabel(r"$\omega$ [rad/s]")
plt.show()

#============= Onda Quadrada============
t = np.linspace(0,0.02,1000)
x = np.zeros_like(t)
T = 1/(40*np.pi)
w = (2*np.pi)/T
x += 0.5
y = x
R = 100
C = 0.00005
plt.figure(figsize=(10,5))

for m in range(1, 120): # Numero de componentes
    s = (2/T * 1/(w*m) * (1 - np.e**(-1j*w*m*T/2))) * (np.e**(1j*(m*w*t - np.pi/2)))                       # Componente da Onda Quadrada
    ganho = 1/(R*C*w*m*1j + 1)
    y = y + np.real(((1/(m*np.pi) * (1 - np.e**(-1j*m*np.pi))) * (np.e**(1j*(m*w*t - np.pi/2))))*ganho)    # Componente da Onda do Capacitor
    x = x + np.real(s)

plt.title(r"Vc(t) para R=100 $\Omega$ e C=0.00005 F", fontsize=20)
plt.plot(t, y, label="VC", color = "b")
plt.plot(t,x, label='V in', color='k')
plt.ylabel("Tensão [V]")
plt.xlabel("Tempo [s]")
plt.legend(loc="lower right", fontsize="xx-large")
plt.show()