import networkx as nx
import matplotlib.pyplot as plt

# Станції метро в м. Дніпро
stations = [
    "Покровська",
    "Проспект Свободи",
    "Заводська",
    "Металургів",
    "Метробудівників",
    "Вокзальна"
]

# Зв'язки між станціями 
edges = [
    ("Покровська", "Проспект Свободи"),
    ("Проспект Свободи", "Заводська"),
    ("Заводська", "Металургів"),
    ("Металургів", "Метробудівників"),
    ("Метробудівників", "Вокзальна"),
]

# Створення графа
metro_graph = nx.Graph()

# Додавання станцій та зв'язків
metro_graph.add_nodes_from(stations)
metro_graph.add_edges_from(edges)

# Відображення графа
pos = nx.spring_layout(metro_graph)
nx.draw(metro_graph, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='lightblue', font_size=8, edge_color='gray')
plt.title("Граф метрополітену м. Дніпро")
plt.show()
