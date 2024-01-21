import matplotlib.pyplot as plt
import networkx as nx


# Функція для виведення шляху та його довжини
def print_path(path):
    print("Шлях:", path)
    print("Довжина шляху:", len(path) - 1)


# Станції метро в м. Дніпро
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

# Зв'язки між станціями
edges = [
    ("Покровська", "Заводська"),
    ("Заводська", "Металургів"),
    ("Металургів", "Вокзальна"),
    ("Вокзальна", "Театральна"),
    ("Театральна", "Центральна"),
    ("Центральна", "Музейна"),
    ("Спортивна", "Пушкінська"),
    ("Пушкінська", "Центральна"),
    ("Центральна", "Індустріальна"),
    ("Індустріальна", "Харківська"),
    ("Пушкінська", "Вокзальна"),
    ("Вокзальна", "Мостова"),
    ("Мостова", "Індустріальна"),
]

# Створення графа
metro_graph = nx.Graph()

# Додавання станцій та зв'язків
metro_graph.add_nodes_from(stations)
metro_graph.add_edges_from(edges)

# Визначення шляхів за допомогою DFS
dfs_path = nx.dfs_edges(metro_graph, source="Покровська")
dfs_path = list(dfs_path)
print("Шляхи, знайдені за допомогою DFS:")
for edge in dfs_path:
    print(edge)
print()

# Визначення шляхів за допомогою BFS
bfs_path = nx.bfs_edges(metro_graph, source="Покровська")
bfs_path = list(bfs_path)
print("Шляхи, знайдені за допомогою BFS:")
for edge in bfs_path:
    print(edge)
print()

# Порівняння результатів
print("Різниця у шляхах:")
print(" - між DFS і BFS:", set(dfs_path) - set(bfs_path))
print(" - між BFS і DFS:", set(bfs_path) - set(dfs_path))
