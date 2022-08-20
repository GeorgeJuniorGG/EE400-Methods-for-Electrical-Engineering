import numpy as np
import matplotlib.pyplot as plt
#=========Função original==================================
x0 = np.linspace(-2*np.pi, 0, 250)                      # Maneira que encontrei de plotar a funcao periodicamente
x1 = np.linspace(0, 2*np.pi, 250)
x2 = np.linspace(2*np.pi, 4*np.pi, 250)
x3 = np.linspace(4*np.pi, 6*np.pi, 250)

f = x1**2
plt.figure(figsize=(12,6))
plt.title('Função Periódica x(t)', fontsize=16) 
plt.plot(x0, f, color='b', label='Alvo')
plt.plot([0, 0], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x1, f, color='b')
plt.plot([2*np.pi, 2*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x2, f, color='b')
plt.plot([4*np.pi, 4*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x3, f, color='b')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.show()
#=========Série de Fourier=================================
x0 = np.linspace(-2*np.pi, 0, 250)
x1 = np.linspace(0, 2*np.pi, 250)
x2 = np.linspace(2*np.pi, 4*np.pi, 250)
x3 = np.linspace(4*np.pi, 6*np.pi, 250)

f = x1**2

t = np.linspace(-2*np.pi, 6*np.pi, 1000)
y = np.zeros_like(t)
y += (4*np.pi**2)/3                                     # Inicializa com a0
for m in range(1,150):                                  # Faz o somatorio da serie de Fourier de 1 ate 149
    s = (np.cos(2*np.pi*m)/(np.pi*m**3) * (4*np.pi*m) * np.cos(m*t) + np.cos(m*t + np.pi/2) * ((2 + np.cos(2*np.pi*m)*(4*np.pi**2*m**2-2))/(np.pi*m**3)))
    y = y + s

plt.figure(figsize=(12,6))
plt.title('Aproximação por Série de Fourier', fontsize=16) 
plt.plot(x0, f, color='b', label='Alvo')
plt.plot([0, 0], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x1, f, color='b')
plt.plot([2*np.pi, 2*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x2, f, color='b')
plt.plot([4*np.pi, 4*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x3, f, color='b')
plt.plot(t, y, color='k', label='Aproximação')
plt.plot(x0, abs(f-y[0:250]), color='y', label='Erro')
plt.plot(x1, abs(f-y[250:500]), color='y')
plt.plot(x2, abs(f-y[500:750]), color='y')
plt.plot(x3, abs(f-y[750:1000]), color='y')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.show()

#=========Série de Taylor==================================
x0 = np.linspace(-2*np.pi, 0, 250)
x1 = np.linspace(0, 2*np.pi, 250)
x2 = np.linspace(2*np.pi, 4*np.pi, 250)
x3 = np.linspace(4*np.pi, 6*np.pi, 250)

f = x1**2

t1 = np.linspace(-2*np.pi, 6*np.pi, 1000)
y1 = np.zeros_like(t1)

for m in range(2,3):                        # Calcula o unico coeficiente da serie de Taylor
    s1 = 1*t1**m
    y1 += s1

plt.figure(figsize=(12,6))
plt.title('Aproximação por Série de Taylor', fontsize=16) 
plt.plot(x0, f, color='b', label='Alvo')
plt.plot([0, 0], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x1, f, color='b')
plt.plot([2*np.pi, 2*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x2, f, color='b')
plt.plot([4*np.pi, 4*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x3, f, color='b')
plt.plot(t1, y1, color='k', label='Aproximação')
plt.plot(x0, abs(f-y1[0:250]), color='y', label='Erro')
plt.plot(x1, abs(f-y1[250:500]), color='y')
plt.plot(x2, abs(f-y1[500:750]), color='y')
plt.plot(x3, abs(f-y1[750:1000]), color='y')
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.show()

#=========Série de Taylor em cima da Série de Fourier======
x0 = np.linspace(-2*np.pi, 0, 250)
x1 = np.linspace(0, 2*np.pi, 250)
x2 = np.linspace(2*np.pi, 4*np.pi, 250)
x3 = np.linspace(4*np.pi, 6*np.pi, 250)

f = x1**2

t2 = np.linspace(-2*np.pi, 6*np.pi, 1000)
y2 = np.zeros_like(t2)
y2 += 4*np.pi**2/3                              # Inicializa com o a0 da serie de Fourier
t0 = 0                                          # Valor de t0 ao redor do qual se quer obter a aproximacao

for m in range(100):                            # Loop correspondente a serie de Taylor
    aux = 0                                     # Variavel que acumula os valores do somatorio da serie de Fourier, para cada iteracao da serie de Taylor
    for n in range(1, 15):                      # Loop correspondente a serie de Fourier
        A = np.cos(2*np.pi*n)/(np.pi*n**3) * (4*np.pi*n)
        B = (2 + np.cos(2*np.pi*n)*(4*np.pi**2*n**2-2))/(np.pi*n**3)
        if(m%4 == 0):
            aux = aux + 1/np.math.factorial(m) * (A*np.cos(n*(t0))*n**m - B*np.sin(n*(t0))*n**m) * (t2-t0)**m
        elif(m%4 == 1):
            aux = aux + 1/np.math.factorial(m) * (-A*np.sin(n*(t0))*n**m - B*np.cos(n*(t0))*n**m)* (t2-t0)**m
        elif(m%4 == 2):
            aux = aux + 1/np.math.factorial(m) * (-A*np.cos(n*(t0))*n**m + B*np.sin(n*(t0))*n**m) * (t2-t0)**m
        elif(m%4 == 3):
            aux = aux + 1/np.math.factorial(m) * (A*np.sin(n*(t0))*n**m + B*np.cos(n*(t0))*n**m) * (t2-t0)**m
    s2 = aux
    y2 = y2 + s2
    


plt.figure(figsize=(12,6))
plt.title('Aproximação por Série de Taylor em cima da Série de Fourier', fontsize=16) 
plt.plot(x0, f, color='b', label='Alvo')
plt.plot([0, 0], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x1, f, color='b')
plt.plot([2*np.pi, 2*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x2, f, color='b')
plt.plot([4*np.pi, 4*np.pi], [0, (2*np.pi)**2 + 5], '--', color='silver')
plt.plot(x3, f, color='b')
plt.plot(t2, y2, color='k', label='Aproximação')
plt.plot(x0, abs(f-y2[0:250]), color='y', label='Erro')
plt.plot(x1, abs(f-y2[250:500]), color='y')
plt.plot(x2, abs(f-y2[500:750]), color='y')
plt.plot(x3, abs(f-y2[750:1000]), color='y')
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(0, 20*np.pi**2)
plt.legend(loc='upper right')
plt.show()