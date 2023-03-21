from typing import Union

import networkx as nx
from matplotlib.pyplot import plot as plt


def build_pairs(seq: tuple) -> list:
    i = 0
    buffer = []
    while i < len(seq):
        buffer.append((i, i + 1))
        if i + 2 < len(seq):
            buffer.append((i, i + 2))

        i += 1

    return buffer


def generate_graph(stairway_: tuple) -> nx.DiGraph:
    nodes_pairs = build_pairs(stairway_)
    prices_dict = {step: cost for step, cost in zip(range(1, len(stairway_) + 1), stairway_)}
    structure = [nodes_pair + tuple([prices_dict[nodes_pair[1]]]) for nodes_pair in nodes_pairs]

    graph = nx.DiGraph()
    graph.add_nodes_from(list(range(len(stairway) + 1)))
    graph.add_weighted_edges_from(structure)
    # nx.draw_spring(graph, with_labels=True, node_color='red')
    # plt.show()
    return graph


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    # TODO c помощью функции из модуля networkx найти стоимость кратчайшего пути до последней лестницы
    visited_nodes = {node: False for node in graph.nodes}
    total_costs = {node: float('inf') for node in graph.nodes}
    current_node = 0
    total_costs[current_node] = 0

    for _ in range(len(graph)):
        not_visited_total_costs = {node: cost for node, cost in total_costs.items() if not visited_nodes[node]}
        min_value = float('inf')

        for key, value in not_visited_total_costs.items():
            if value < min_value:
                min_value = value
                current_node = key

        visited_nodes[current_node] = True

        for neighbour_node in graph[current_node]:
            weight = graph[current_node][neighbour_node]['weight']
            total_costs[neighbour_node] = min(total_costs[neighbour_node], total_costs[current_node] + weight)

    return list(total_costs.values())[-1]


def stairway_path_v2(graph: nx.DiGraph):
    start = list(graph.nodes)[0]
    finish = list(graph.nodes)[-1]
    path = nx.dijkstra_path(graph, start, finish)
    cost = nx.dijkstra_path_length(graph, start, finish)
    return path, cost


if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = generate_graph(stairway)  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72

    print(stairway_path_v2(stairway_graph))  # 72
