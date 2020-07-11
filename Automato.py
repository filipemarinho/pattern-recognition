
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
plt.rcParams['figure.figsize'] = [9.5, 6]

#Função para o plot dos automatos 
def plot(L, gerador = "A"):
    fig, [axs1,axs2,axs3] = plt.subplots(3, 1, figsize=(9.5*3,6))
    
    Title = "Visualização da Sequência Gerada pelo automato "
    
    fig.suptitle(Title+str(gerador))
    
    axs1.set_title("Colormap")
    heat_map = sb.heatmap([[int(i) for i in L]], ax = axs1, cmap = 'viridis', xticklabels=False, yticklabels=False, cbar=False)
#     axs1.set_title("Histogram")
#     axs1.hist(L, density=True, facecolor='g', alpha=0.75)
    
    axs2.set_title("Stem Plot")    
    (markers, stemlines, baseline) = axs2.stem( np.arange(0,len(L)), L, use_line_collection=True, markerfmt = "k.")#,linefmt='gray', basefmt = 'gray')
    
    plt.setp(stemlines, linestyle="-", color="black", linewidth=0.5)
    plt.setp(baseline, linestyle=" ")#, color="black", linewidth=0.3, alpha = 0.1 )
    axs2.set_xlim(0,len(L))
    
    axs3.set_title("Bar Plot")
    axs3.step(np.arange(0,len(L)),L, where = 'post', color = 'black', linewidth = 0.9)
    axs3.set_xlim(0,len(L))
#     if max(L)>1:
#         plt.grid()
    plt.show()
    

#Gerador de automatos probabilisticos
def NextStep(last, matriz):
    i = 0
    p = matriz[last][0]
    r = np.random.random(1)[0]
#     print(last)
#     print(i)
    while r>p:
        
        i = i+1
        p =p+ matriz[last][i]
#         print(i)
#     print()
    return i



a