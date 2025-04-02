# Faz a importação da biblioteca matplotlib e adiciona um alias (apelido) 
# Usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

# Definição dos grupos e valores
fabricante = ['toyota', 'ford', 'volkswagen', 'honda', 'bmw']
quantidade = [1050000, 900000, 950000, 870000, 500000]

# Configura um gráfico de barras, onde recebe os grupos, valores
# E opcionalmente ass cores]
plt.bar (fabricante, quantidade, color=['navy', 'red', 'silver', 'green', 'blue'])

# Define o título do gráfico
plt.title ('Produção de Automóveis por Fabricante')

# Define o título do eixo X
plt.xlabel ('Fabricante')

    # Define o título do eixo Y
plt.ylabel('Carros Produzidos')

# Cria o gráfico
plt.show()

# Salva dentro do arquivo de imagem
plt.savefig('chart.png')