import matplotlib.pyplot as plt
import networkx as nx

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

# Отримання основних характеристик графа
num_nodes = metro_graph.number_of_nodes()
num_edges = metro_graph.number_of_edges()
degree_sequence = [degree for node, degree in metro_graph.degree()]

# Вивід інформації
print("Кількість вершин (станцій):", num_nodes)
print("Кількість ребер (зв'язків):", num_edges)
print("Ступінь кожної вершини:", degree_sequence)

# Відображення графа
pos = nx.spring_layout(metro_graph, seed=42)
nx.draw(
    metro_graph,
    pos,
    with_labels=True,
    font_weight="bold",
    node_size=1000,
    node_color="lightblue",
    font_size=8,
    edge_color="gray",
)
plt.title("Граф метрополітену м. Дніпро")
plt.show()
