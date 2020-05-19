import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
    
#Função para o plot dos automatos 
def plot(L, gerador = "A"):
    fig, [axs1,axs2,axs3] = plt.subplots(3, 1, figsize=(10,6), dpi = 100, constrained_layout=True)
    Title = "Visualização da Sequência Gerada pelo automato "

    fig.suptitle(Title+gerador)

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

def freq(automato, symbol):
    automato = np.array(automato)
    counter = 0
    for i in automato: 
        if i==symbol: 
            counter +=1
    return counter/automato.size

def plot_density(frequencies, automato="A"):
    fig = plt.gcf()
    fig.suptitle("Densidade de f para o automato "+str(automato))
    colors = ["dodgerblue","orange","deeppink"]
    i=0
    for f in frequencies:
        sb.distplot(f, color = colors[i],  hist = False, kde = True)
        i+=1

    plt.xlim(0,1)
    plt.xlabel("Frequência de \"1\"")
    plt.ylabel("Densidade de ocorrência")