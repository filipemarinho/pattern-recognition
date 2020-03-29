from  numpy import arange
import matplotlib.pyplot as plt
import seaborn as sb


def plot(L):
    #Cria 3 plots de 10x10 na vertical
    fig, [axs1,axs2,axs3] = plt.subplots(3, 1, figsize=(30, 10))
    
    axs1.set_title("Colormap")
    heat_map = sb.heatmap([[int(i) for i in L]], ax = axs1, xticklabels=False, yticklabels=False, cbar=False)

#     Para fazer um histograma, bom para ver a frequencia relativa
#     axs1.set_title("Histogram")
#     axs1.hist(L, density=True, facecolor='g', alpha=0.75)
    
    axs2.set_title("Stem Plot")    
    axs2.stem(arange(0,len(L)), L, use_line_collection=True)
    axs2.set_xlim(0,len(L))
    
    axs3.set_title("Bar Plot")
    axs3.step(arange(0,len(L)),L)
    axs3.set_xlim(0,len(L))

    plt.grid()
    plt.show()

#Teste
#plot(["0", "1", "0","1","0"])

