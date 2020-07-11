import numpy as np
import matplotlib.pyplot as plt

N = 500
circle = [[],[]]
dist_x = []
dist_y = []

while len(dist_x) <= N:
    # Gera uma distribuição normal entre [-1,1]
    x,y = np.random.rand(2)*2 -1
    
    #verifica se o ponto esta num circulo unitário de raio 1
    if x**2+y**2 <=1:
        circle[0].append(x)
        circle[1].append(y)
        dist_x.append(x)
        dist_y.append(y*0.2) #quanto mais comprimido mais redundante, uma reta seria a mais redundante de todos
        
#matriz de rotação         
rot = [[np.cos(np.pi/6), np.sin(np.pi/6)], [np.sin(np.pi/6), np.cos(np.pi/6)]]   

#faz a rotação
result = np.dot(rot, [dist_x,dist_y])
#print(len(result))

fig, ax = plt.subplots(1, 3, figsize=(3*8, 8), sharey = True, sharex = True)

fig.suptitle("Distribuições uniformes")
ax[0].set_title("Distribuição em um circulo unitário")
ax[1].set_title("Distribuição alongada")
ax[2].set_title("Distribuição alongada rotacionada")
# ax[0].set_xlim(-1.1,1.1)
# ax[0].set_ylim(-1.1,1.1)


ax[0].scatter(circle[0],circle[1])
ax[1].scatter(dist_x, dist_y)
ax[2].scatter(result[0], result[1])
plt.savefig("images/uniform_dist.png")
plt.show()
