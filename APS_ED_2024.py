import random  # Biblioteca usada para gerar números aleatórios
from datetime import datetime, timedelta  # Importa classes para manipulação de datas e tempos
import time  # Usada para medir o tempo de execução de funções
import matplotlib.pyplot as plt  # Biblioteca para criar gráficos
import numpy as np

# Função que gera 'n' datas aleatórias
def generate_random_dates(n):
    start_date = datetime(2000, 1, 1)  # Define uma data de início fixa
    random_dates = []  # Lista para armazenar as datas geradas
    for _ in range(n):
        random_number_of_days = random.randint(0, 10000)  # Gera um número aleatório de dias a partir da data de início
        random_number_of_seconds = random.randint(0, 86400)  # Gera um número aleatório de segundos em um dia
        random_date = start_date + timedelta(days=random_number_of_days, seconds=random_number_of_seconds)  # Calcula a data aleatória
        random_dates.append(random_date.strftime("%Y-%m-%d %H:%M:%S"))  # Formata a data e adiciona à lista
    return random_dates  # Retorna a lista de datas aleatórias

# Implementação do algoritmo Bubble Sort para ordenar as datas
def bubble_sort(datas):
    n = len(datas)  # Tamanho da lista de datas
    for i in range(n):
        for j in range(0, n-i-1):  # Itera pela lista comparando pares de elementos
            if datas[j] > datas[j+1]:  # Se a data atual for maior que a próxima, troca as posições
                datas[j], datas[j+1] = datas[j+1], datas[j]
    return datas  # Retorna a lista ordenada

# Implementação do algoritmo Merge Sort para ordenar as datas
def merge_sort(datas):
    if len(datas) > 1:  # Só realiza a ordenação se a lista tiver mais de 1 elemento
        mid = len(datas) // 2  # Encontra o meio da lista
        esquerda = datas[:mid]  # Divide a lista em duas metades
        direita = datas[mid:]

        merge_sort(esquerda)  # Recursivamente ordena a metade esquerda
        merge_sort(direita)  # Recursivamente ordena a metade direita

        # Mescla as duas metades
        i = j = k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                datas[k] = esquerda[i]  # Copia o menor valor para a lista ordenada
                i += 1
            else:
                datas[k] = direita[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes da metade esquerda (se houver)
        while i < len(esquerda):
            datas[k] = esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes da metade direita (se houver)
        while j < len(direita):
            datas[k] = direita[j]
            j += 1
            k += 1
    return datas  # Retorna a lista ordenada

# Implementação do algoritmo Quick Sort para ordenar as datas
def quick_sort(datas):
    if len(datas) <= 1:  # Caso base: lista com 0 ou 1 elemento já está ordenada
        return datas
    else:
        pivô = datas[len(datas) // 2]  # Escolhe um pivô (elemento central)
        menores = [x for x in datas if x < pivô]  # Lista com os elementos menores que o pivô
        iguais = [x for x in datas if x == pivô]  # Lista com os elementos iguais ao pivô
        maiores = [x for x in datas if x > pivô]  # Lista com os elementos maiores que o pivô
        return quick_sort(menores) + iguais + quick_sort(maiores)  # Recursivamente ordena e combina os resultados

# Função para medir o tempo de execução de um algoritmo de ordenação // PRECISA DE OUTRA FUNÇAO MAIS PRECISA, ALGUNS TEMPOS ESTAO DANDO 0
def medir_tempo(algoritmo, dados):
    temp = dados.copy()
    inicio = time.perf_counter() # Armazena o tempo inicial

    algoritmo(temp)

    fim = time.perf_counter() # Armazena o tempo final
    return timedelta(seconds = fim-inicio).total_seconds() # Devolve o tempo de execuçao do   

# Função para plotar os tempos de execução dos algoritmos em um gráfico
def plotar_tempos(tempos_bubble, tempos_merge, tempos_quick, tamanhos, caso):
    # Ajustando fatores para alinhar as curvas teóricas
    fator_bubble = max(tempos_bubble) / max([t**2 for t in tamanhos])
    fator_merge = max(tempos_merge) / max([t * np.log2(t) for t in tamanhos])
    fator_quick = max(tempos_quick) / max([t * np.log2(t) for t in tamanhos])

    # Curvas teóricas alinhadas às experimentais
    plt.plot(tamanhos, [fator_bubble * (t**2) for t in tamanhos], 
             label='Bubble Sort (Teórica)', linestyle='--', color='blue', zorder=1)
    plt.plot(tamanhos, [fator_merge * (t * np.log2(t)) for t in tamanhos], 
             label='Merge Sort (Teórica)', linestyle='--', color='green', zorder=1)
    plt.plot(tamanhos, [fator_quick * (t * np.log2(t)) for t in tamanhos], 
             label='Quick Sort (Teórica)', linestyle='--', color='red', zorder=1)

    # Curvas experimentais
    plt.plot(tamanhos, tempos_bubble, label='Bubble Sort (Experimental)', marker='o', color='blue', zorder=2)
    plt.plot(tamanhos, tempos_merge, label='Merge Sort (Experimental)', marker='o', color='green', zorder=2)
    plt.plot(tamanhos, tempos_quick, label='Quick Sort (Experimental)', marker='o', color='red', zorder=2)

    plt.yscale('log')  # Transformar a escala Y para logaritmo
    plt.xlabel('Número de datas')  # Legenda do eixo X
    plt.ylabel('Tempo de execução (log segundos)')  # Legenda do eixo Y
    plt.title(f'Comparação de Algoritmos de Ordenação ({caso})')  # Título do gráfico
    plt.legend()  # Exibe a legenda
    plt.grid(True)  # Adiciona uma grade ao gráfico
    plt.show()  # Exibe o gráfico





# Testando com diferentes tamanhos de listas
tamanhos = [] # Lista de tamanhos de entrada  //colocar um in range aqui, intervalos de 50
for x in range(100,1000,50):
    tamanhos.append(x)



# Melhor Caso (lista ordenada)
tempos_bubble_melhor = []
tempos_merge_melhor = []
tempos_quick_melhor = []

for tamanho in tamanhos:
    dados_ordenados = sorted(generate_random_dates(tamanho))  # Gera uma lista ordenada (melhor caso)
    
    tempos_bubble_melhor.append(medir_tempo(bubble_sort, dados_ordenados))
    tempos_merge_melhor.append(medir_tempo(merge_sort, dados_ordenados))
    tempos_quick_melhor.append(medir_tempo(quick_sort, dados_ordenados))

# Pior Caso (lista inversamente ordenada)
tempos_bubble_pior = []
tempos_merge_pior = []
tempos_quick_pior = []

for tamanho in tamanhos:
    dados_inversos = sorted(generate_random_dates(tamanho), reverse=True)  # Gera uma lista inversamente ordenada (pior caso)
    
    tempos_bubble_pior.append(medir_tempo(bubble_sort, dados_inversos))
    tempos_merge_pior.append(medir_tempo(merge_sort, dados_inversos))
    tempos_quick_pior.append(medir_tempo(quick_sort, dados_inversos))

# Plotando os resultados dos tempos de execução para o melhor caso
plotar_tempos(tempos_bubble_melhor, tempos_merge_melhor, tempos_quick_melhor, tamanhos, "Melhor Caso")

# Plotando os resultados dos tempos de execução para o pior caso
plotar_tempos(tempos_bubble_pior, tempos_merge_pior, tempos_quick_pior, tamanhos, "Pior Caso")
