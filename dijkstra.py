import networkx as nx


def dijkstra(graph, start):
    # Ініціалізація відстаней
    distance = {node: float("infinity") for node in graph.nodes}
    distance[start] = 0

    # Множина відвіданих вершин
    visited = set()

    while len(visited) < len(graph.nodes):
        # Вибір вершини з найменшою відстанню
        current_node = min(
            (node for node in graph.nodes if node not in visited),
            key=lambda x: distance[x],
        )
        visited.add(current_node)

        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph[current_node].items():
            new_distance = distance[current_node] + weight["weight"]
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

    return distance


# Граф метрополітену
stations = [
    "Покровська",
    "Заводська",
    "Металургів",
    "Вокзальна",
    "Театральна",
    "Центральна",
    "Музейна",
    "Спортивна",
    "Пушкінська",
    "Індустріальна",
    "Харківська",
    "Мостова",
]

edges_with_weights = [
    ("Покровська", "Заводська", 3),
    ("Заводська", "Металургів", 2),
    ("Металургів", "Вокзальна", 4),
    ("Вокзальна", "Театральна", 1),
    ("Театральна", "Центральна", 2),
    ("Центральна", "Музейна", 3),
    ("Спортивна", "Пушкінська", 2),
    ("Пушкінська", "Центральна", 1),
    ("Центральна", "Індустріальна", 3),
    ("Індустріальна", "Харківська", 2),
    ("Пушкінська", "Вокзальна", 1),
    ("Вокзальна", "Мостова", 3),
    ("Мостова", "Індустріальна", 3),
]

metro_graph = nx.Graph()
metro_graph.add_nodes_from(stations)
metro_graph.add_weighted_edges_from(edges_with_weights)

# Виклик алгоритму Дейкстри
start_station = "Покровська"
shortest_distances = dijkstra(metro_graph, start_station)

# Виведення результатів
print(f"Найкоротші відстані від станції {start_station}:")
for station, distance in shortest_distances.items():
    print(f"{station}: {distance}")
