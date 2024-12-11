import networkx as nx  # Importa a biblioteca NetworkX, usada para manipulação e visualização de grafos
import matplotlib.pyplot as plt  # Importa o Matplotlib para visualização gráfica do grafo

def ler_grafo(nome_arquivo):
    """Carrega o grafo a partir de um arquivo no formato especificado."""
    with open(nome_arquivo, 'r') as arquivo:  # Abre o arquivo no modo leitura
        n = int(arquivo.readline().strip())  # Lê a primeira linha que contém o número de vértices e converte para inteiro
        grafo = {i: [] for i in range(1, n + 1)}  # Cria a estrutura de dados (inicialmente vazias).onde as chaves são os vértices e os valores são listas de arestas, (1, n + 1) cria uma sequencia de 1 ate infinito.

        # Lê as arestas e seus pesos
        for linha in arquivo:  # Itera pelas linhas restantes do arquivo
            x, y, z = linha.split()  # Divide a linha em três partes: dois vértices e o peso da aresta
            x, y = int(x), int(y)  # Converte os vértices para inteiros
            z = int(z)  # Converte o peso da aresta para um inteiro
            
            # Adiciona as arestas no grafo
            grafo[x].append((y, z))  # Adiciona uma aresta de x para y com peso z
            grafo[y].append((x, z))  # Como o grafo é não direcionado, também adiciona a aresta de y para x com o mesmo peso

    return grafo  # Retorna o grafo como um dicionário

def exibir_grafo(grafo, representacao='adjacente'):
    """Exibe o grafo na forma de lista de adjacência ou lista de arestas."""
    if representacao == 'adjacente':  # Se a representação for adjacente
        for vertice, arestas in grafo.items():  # Itera sobre os vértices e suas arestas
            print(f"{vertice}: {arestas}")  # Exibe o vértice e suas arestas
    elif representacao == 'arestas':  # Se a representação for arestas
        arestas = set()  # Cria um conjunto para armazenar as arestas e evitar duplicatas
        for vertice, adjacentes in grafo.items():  # Itera sobre os vértices e suas listas de adjacência
            for destino, peso in adjacentes:  # Itera sobre os destinos e pesos das arestas
                if (destino, vertice, peso) not in arestas:  # Se a aresta reversa não estiver no conjunto
                    arestas.add((vertice, destino, peso))  # Adiciona a aresta ao conjunto
        for aresta in arestas:  # Itera sobre as arestas únicas
            print(f"Aresta: {aresta[0]} -> {aresta[1]} com peso {aresta[2]}")  # Exibe a aresta e seu peso
    else:  # Caso a representação não seja reconhecida
        print("Representação não reconhecida!")  # Exibe uma mensagem de erro

def visualizar_grafo(grafo):
    """Visualiza o grafo usando NetworkX e Matplotlib."""
    G = nx.Graph()  # Cria um objeto grafo vazio usando NetworkX

    # Adiciona as arestas ao grafo do NetworkX
    for vertice, adjacentes in grafo.items():  # Itera sobre os vértices e suas adjacências
        for destino, peso in adjacentes:  # Itera sobre os destinos e pesos das arestas
            G.add_edge(vertice, destino, weight=peso)  # Adiciona as arestas ao grafo do NetworkX, com o peso associado

    # Configurações para exibir os pesos das arestas
    pos = nx.spring_layout(G)  # Gera uma disposição das posições dos vértices usando o layout de mola
    labels = nx.get_edge_attributes(G, 'weight')  # Obtém os pesos das arestas do grafo

    plt.figure(figsize=(8, 6))  # Cria uma figura com o tamanho especificado
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')  # Desenha o grafo com a posição e estilos definidos
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)  # Desenha os rótulos das arestas com os pesos
    plt.title("Visualização do Grafo", fontsize=16)  # Define o título da visualização
    plt.show()  # Exibe o gráfico

# Exemplo de uso:
grafo = ler_grafo("arquivo.g")  # Carrega o grafo a partir do arquivo especificado

# Exibe o grafo em forma de lista de adjacência
exibir_grafo(grafo, "adjacente")  # Exibe o grafo como uma lista de adjacência
print()  # Quebra de linha

# Exibe o grafo em forma de lista de arestas
exibir_grafo(grafo, "arestas")  # Exibe o grafo como uma lista de arestas
print()  # Quebra de linha

# Visualiza o grafo com NetworkX
visualizar_grafo(grafo)  # Visualiza o grafo usando a função de visualização do NetworkX
