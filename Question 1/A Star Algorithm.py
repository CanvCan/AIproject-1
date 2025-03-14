import heapq
import networkx as nx
import matplotlib.pyplot as plt


def path_to_graph(path):
    graph = nx.Graph()

    # Noktaları ekleyin
    for i, node in enumerate(path):
        graph.add_node(i, pos=node)

    # Kenarları ekleyin
    for i in range(len(path) - 1):
        graph.add_edge(i, i + 1)

    return graph


def plot_graph(graph):
    pos = nx.get_node_attributes(graph, 'pos')

    plt.figure(figsize=(5, 5))
    nx.draw(graph, pos, with_labels=True, node_size=700, node_color='lightblue', font_size=10, font_weight='bold',
            edge_color='gray', width=2)
    plt.title("Shortest Path")
    plt.show()


class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(start, end, grid):
    open_list = []
    closed_list = []

    heapq.heappush(open_list, (0, start))

    while open_list:
        current_node = heapq.heappop(open_list)[1]
        closed_list.append(current_node)

        if current_node == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (
                    len(grid[len(grid) - 1]) - 1) or node_position[1] < 0:
                continue

            if grid[node_position[0]][node_position[1]] == '#':
                continue

            new_node = Node(node_position, current_node)

            children.append(new_node)

        for child in children:
            if child in closed_list:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end.position[0]) ** 2) + ((child.position[1] - end.position[1]) ** 2)
            child.f = child.g + child.h

            for open_node in open_list:
                if child == open_node[1] and child.g > open_node[1].g:
                    break
            else:
                heapq.heappush(open_list, (child.f, child))

    return None


def print_path(path):
    for position in path:
        print(position)


def main():
    grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '#', '.'],
        ['.', '.', '.', '.', '.', '.']
    ]

    start = Node((0, 0))
    end = Node((4, 5))

    path = astar(start, end, grid)
    plot_graph(path_to_graph(path))


if __name__ == "__main__":
    main()
