# Faz a importação da biblioteca matplotlib e adiciona um alias (apelido) 
# Usar linha de comando: python3 -m pip install matplotlib 
import matplotlib.pyplot as plt 

def exibirGrafico ():
    # Definição dos grupos e valores 
    grupos = ['A','B','C']
    valores = [23,38,12]

    # Configurar um gráfico de barras, onde recebe os grupos, valores 
    # E opcionalmente as cores 
    plt. bar (grupos, valores, color = ['red','blue','grey'])

    #  Define o título do gráfico 
    plt.title ('Gráfico de Barras Simples')

    # Define o título do eixo x 
    plt.xlabel ('Grupos')
