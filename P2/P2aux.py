import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd

#Função usada para gerar os automatos a partir da matriz de probabilidades, retorna proximo numero da sequencia

def NextStep(last, matriz):
    i = 0
    p = matriz[last][0]
    r = np.random.random(1)[0]
    
    while r>p:
        i = i+1
        p =p+ matriz[last][i]
    return i

#função que gera um automato de tamanho M 
def New_automato(matriz, M = 200):
    automato = [0]
    while len(automato) < M:
        automato.append(NextStep(automato[-1], matriz))
    return automato

#Metodos implementados:
def Entropy(prob):
    entropy = 0
    for p_i in prob:
        if p_i>0:
            entropy -= p_i*np.log2(p_i)
    return entropy

def Evenness(probabilities):
    E = Entropy(probabilities)
    return 2**E

def Relative_freq(automato):
    automato = np.array(automato)
    freqs = []
    for symbol in range(max(automato)+1):
        counter = 0
        for i in automato: 
            if i==symbol: 
                counter +=1
        freqs.append(counter/automato.size)
    return freqs

def Split(sequence, symbol):
    split = []
    for i in sequence:
        if int(i)==int(symbol):
            split.append(1)
        else:
            split.append(0)
    return split

def ScanBursts(sequence):
    M = len(sequence)
    bursts = []
    count = 0
    for i in sequence:
        if i==1:
            count += 1
        elif count !=0:
            bursts.append(count)
            count = 0
    return np.array(bursts)

def Intersymbol(sequence):
    M = len(sequence)
    distance = []
    
    count = 0
    for i in sequence:
        if i==0:
            count += 1
        elif count !=0:
            distance.append(count)
            count = 0
    return np.array(distance)

def PowerSpec(sequence):
    fft = np.fft.fft(sequence)
    spec =(np.abs(fft))**2
    return np.array(spec)

def Visibility(L): 
    M = np.zeros((len(L),len(L)))
    for j in range(1,len(L)):
        for i in range(0, j-1):
            flag = 1
            k = i + 1
            while (k <= j-1) and (flag == 1):
                aux = L[j] + (L[i]-L[j])*(j-k)/(j-i)
                if (L[k] >= aux):
                    flag = 0
                k += 1
            if (flag == 1):
                M[i][j] = 1
                M[j][i] = 1
    sb.set_style("white")
    fig, ax = plt.subplots(1, 1, figsize=(9.5,9.5))
    plt.title("Matriz de Adjacência")
    sb.heatmap(M, cmap = 'viridis', xticklabels=False, yticklabels=False, cbar=False, square = True, )
    return M

def Average_Degree(L,M):
    edges = 0
    for i in range(len(L)):
        for j in range(len(L)):
            if M[i][j] == 1:
                edges += 1
    average = edges/(len(L))
    standard_deviation = M.std()
    print("Grau:\nMédia: %.2f Desvio padrão: %.2f \n" %(average,standard_deviation))
    return average, standard_deviation

def Clustering_Coefficient(M):
    degree_node = [] 
    count = 0
    for i in range(len(M)):
        degree_node.append(sum(M[i]))
        count += 1
    coefficient = (sum(degree_node)*2)/(count*(count-1))
    print("Coeficiente de aglomeração: %.2f" %coefficient)
    return coefficient

def Splits_all(automato):
    n = max(automato)
    splits=[]
    fig, axs = plt.subplots(n+2, 1,figsize=(12,6), dpi = 100, constrained_layout=True)
    axs[0].set_title("Stem Plot do sinal Original")    
    (markers, stemlines, baseline) = axs[0].stem( np.arange(0,len(automato)), automato, use_line_collection=True, markerfmt = "k.")#,linefmt='gray', basefmt = 'gray')
    plt.setp(stemlines, linestyle="-", color="black", linewidth=0.5)
    plt.setp(baseline, linestyle=" ")#, color="black", linewidth=0.3, alpha = 0.1 )
    axs[0].set_xlim(0,len(automato))
    for i in range(n+1):
        S = Split(automato,i)
        splits.append(S)
        axs[i+1].set_title("Split Signal do sinal S= "+str(i))    
        (markers, stemlines, baseline) = axs[i+1].stem( np.arange(0,len(S)), S, use_line_collection=True, markerfmt = "k.")#,linefmt='gray', basefmt = 'gray')
        plt.setp(stemlines, linestyle="-", color="black", linewidth=0.5)
        plt.setp(baseline, linestyle=" ")#, color="black", linewidth=0.3, alpha = 0.1 
    plt.show()
    return np.array(splits)

def plot_power(values, name):
    fig, ax = plt.subplots(1, 1, figsize=(10,6))
    
    values = values[1:len(values)//2]
    maximum= max(values)
    index = (np.where(values==maximum)[0]) 
    (markers, stemlines, baseline) = ax.stem(np.linspace(0,1,len(values)), values, use_line_collection=True, label="Max = %.1f, f = %.2f, T = %.2f"%(maximum, index/100, 100/index) , markerfmt = "k.")
    plt.setp(stemlines, linestyle="-", color="black", linewidth=0.5)
    plt.setp(baseline, linestyle=" ")#, color="black", linewidth=0.3, alpha = 0.1 )    
    ax.set_title("Espectro de potência de "+ name)
    plt.xlabel("f")
    plt.ylabel("Amplitude")
    plt.legend()
    
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