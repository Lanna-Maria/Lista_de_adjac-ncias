# Importa as bibliotecas necessárias
import networkx as nx  # Para manipulação e análise de grafos
import matplotlib.pyplot as plt  # Para visualização do grafo
import argparse  # Para manipulação de argumentos da linha de comando

# Função para ler o grafo de um arquivo
def ler_grafo(inst):
    with open(inst, 'r') as arquivo:  # Abre o arquivo especificado
        n = int(arquivo.readline().strip())  # Lê a primeira linha e obtém o número de vértices (n)
        grafo = {i: [] for i in range(1, n + 1)}  # Cria um dicionário onde as chaves são os vértices e os valores são listas vazias para armazenar as arestas

        # Lê as linhas subsequentes do arquivo
        for linha in arquivo:
            linha = linha.strip()  # Remove espaços em branco desnecessários
            if linha:  # Se a linha não estiver vazia
                x, y, z = map(int, linha.split())  # Lê os valores das arestas (x, y) e peso (z)
                grafo[x].append((y, z))  # Adiciona a aresta (x, y) com peso z ao vértice x
                grafo[y].append((x, z))  # Adiciona a aresta (y, x) com peso z ao vértice y (grafo não direcionado)
    return grafo  # Retorna o grafo lido

# Função para exibir o grafo de forma textual
def exibir_grafo(grafo):
    for vertice, arestas in grafo.items():  # Para cada vértice e suas arestas
        print(f"{vertice}: {arestas}")  # Exibe o vértice e suas arestas associadas

# Função para visualizar o grafo graficamente
def visualizar_grafo(grafo):
    G = nx.Graph()  # Cria um grafo vazio utilizando a biblioteca NetworkX
    for vertice, adjacentes in grafo.items():  # Para cada vértice e seus vértices adjacentes
        for destino, peso in adjacentes:  # Para cada destino e peso associado à aresta
            G.add_edge(vertice, destino, weight=peso)  # Adiciona a aresta ao grafo NetworkX com o peso

    pos = nx.spring_layout(G)  # Define o layout para a posição dos vértices (distribuição "spring")
    labels = nx.get_edge_attributes(G, 'weight')  # Obtém os pesos das arestas

    # Configura a visualização com matplotlib
    plt.figure(figsize=(8, 6))  # Define o tamanho da figura
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')  # Desenha o grafo
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)  # Desenha os rótulos das arestas com os pesos
    plt.title("Visualização do Grafo", fontsize=16)  # Título da visualização
    plt.show()  # Exibe o grafo

# Função principal que gerencia os argumentos da linha de comando
def main():
    # Define os argumentos que serão passados via linha de comando
    parser = argparse.ArgumentParser(description="Manipulação de grafos")
    parser.add_argument("comando", choices=["read", "show", "visualize"], help="Comando a ser executado")
    parser.add_argument("arquivo", help="Nome da inst do grafo")  # Argumento que recebe o nome do arquivo
    args = parser.parse_args()  # Faz o parsing dos argumentos

    # Carrega o grafo uma única vez a partir do arquivo
    grafo = ler_grafo(args.arquivo)

    # Executa o comando conforme o argumento passado
    if args.comando == "read":  # Se o comando for 'read'
        print(f"'{args.arquivo}' carregada com sucesso!")  # Informa que o grafo foi carregado

    elif args.comando == "show":  # Se o comando for 'show'
        exibir_grafo(grafo)  # Exibe o grafo de forma textual

    elif args.comando == "visualize":  # Se o comando for 'visualize'
        visualizar_grafo(grafo)  # Exibe o grafo graficamente

# Este bloco garante que o código seja executado somente se for chamado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal
