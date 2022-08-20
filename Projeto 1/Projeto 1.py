import numpy as np
import matplotlib.pyplot as plt
import math
# EXEMPLO BASE (23 lados)
# [ [0, 0], [1, 2], [4, 4], [5, 5], [7, 6], [8, 7], [9, 9], [11, 10], [14, 13], [15, 14], [16, 15], [18, 17], [19, 18], [22, 19], [23, 20], [26, 18], [26, 15], [22, 14], [17, 11], [14, 7], [11, 5], [7, 3], [4, 2] ]
#========= CONSTANTES =============================
# Número de lados do polígono
N = int(input("Digite o numero de lados do poligono: "))
# Vértices do polígono
vertices = input("Insira os vértices do polígono ([ [x1, y1], [x2, y2], ..., [xn, yn] ]): ")
vertices = vertices[2 : len(vertices) - 2]                      # Remove os colchetes e os espacos do inicio e do final
vertices = list(vertices.split("], ["))                         # Cada dupla esta em uma posicao da lista
vertices[0] = vertices[0][1 : len(vertices[0])]                 # Remove o colchete restante da primeira dupla
vertices[-1] = vertices[-1][0 : len(vertices[-1]) - 1]          # Remove o colchete restante da ultima dupla
x = []
y = []
for i in range (len(vertices)):                                 # Separa as coordenadas em x e em y em vetores diferentes
    for j in range (len(vertices[i])):
        if vertices[i][j] == ",":
            break
    aux_x = vertices[i][0 : j]
    aux_y = vertices[i][j+1 : len(vertices[i])]
    x.append(int(aux_x))
    y.append(int(aux_y))
x.append(0)                                                     # Adiciona o ponto (0,0) no final para facilitar o cálculo da área
y.append(0)
# Componente x do campo vetorial
Fx = int(input("Digite o valor da componente em X do campo vetorial (constante): "))
# Componente y do campo vetorial
Fy = int(input("Digite o valor da componente em Y do campo vetorial (constante): "))
# Componente z do campo vetorial
Fz = int(input("Digite o valor da componente em Z do campo vetorial (constante): "))
# Campo vetorial
F = np.array([Fx, Fy, Fz])
#========= PRIMEIRO PLOT ==========================
x_,y_, z_ = np.meshgrid(np.linspace(min(x), max(x), 5), np.linspace(min(y), max(y), 5), np.linspace(-10, 10, 3))        # Para o campo vetorial

plt.figure(figsize=(6,6))
ax = plt.axes(projection='3d')                                              # Para deixar a figura em 3D
ax.quiver3D(x_, y_, z_, Fx, Fy, Fz, length=0.8,  color='lightcoral')        # Plot do campo vetorial
ax.plot(x, y, zs = 0, zdir = 'z', color='lime')                             # Plot do poligono em z = 0
plt.xlim(min(x) - 1, max(x) + 1)
plt.ylim(min(y) - 1, max(y) + 1)
plt.xlabel("x")
plt.ylabel("y")
ax.set_zlabel("z")
plt.show()
#========= SEGUNDO PLOT ============================
t = np.linspace(0, 10, 100)                 # Em segundos
omega = np.pi                               # Em radiano/s
Fnorma = np.sqrt(Fx**2 + Fy**2 + Fz**2)
theta_zero = math.acos(Fz/Fnorma)

area = 0
for i in range(0, N-1):
    area += (x[i]*y[i+1] - x[i+1]*y[i])

area += x[N-1]*y[0] - x[0]*y[N-1]
area = abs(area)/2                                  # Calculo da area como deduzido no texto

fluxo = area*np.cos(theta_zero + omega*t)*Fnorma    # Calculo do fluxo como deduzido no texto

plt.figure()
plt.plot(t, fluxo)
plt.xlabel("Tempo [s]")
plt.ylabel("Fluxo")
plt.show()