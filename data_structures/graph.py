# Подключаем очередь, чтобы использовать ее в обходе BFS.
from .queue_list import QueueList


# Создаем класс Graph для графа.
class Graph:
    # Создаем метод запуска графа.
    def __init__(self, directed: bool = True) -> None:
        # Сохраняем режим графа.
        self.directed = directed
        # Создаем словарь смежности.
        self.adjacency: dict[str, list[str]] = {}

    # Создаем метод добавления отдельной вершины.
    def add_vertex(self, vertex: str) -> None:
        # Если вершины еще нет, создаем для нее пустой список соседей.
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    # Создаем метод добавления ребра.
    def add_edge(self, start: str, end: str) -> None:
        # Убеждаемся, что стартовая вершина существует.
        self.add_vertex(start)

        # Убеждаемся, что конечная вершина существует.
        self.add_vertex(end)

        # Если связи еще нет, добавляем ее.
        if end not in self.adjacency[start]:
            self.adjacency[start].append(end)

        # Если граф ненаправленный, добавляем обратную связь.
        if not self.directed and start not in self.adjacency[end]:
            self.adjacency[end].append(start)

    # Создаем метод получения соседей вершины.
    def get_neighbors(self, vertex: str) -> list[str]:
        # Возвращаем копию списка соседей.
        return self.adjacency.get(vertex, []).copy()

    # Создаем метод обхода графа в ширину.
    def bfs(self, start: str) -> list[str]:
        # Проверяем, что стартовая вершина есть в графе.
        if start not in self.adjacency:
            raise KeyError("Стартовая вершина отсутствует в графе.")

        # Создаем список порядка обхода.
        visited_order: list[str] = []

        # Создаем множество уже замеченных вершин.
        seen = {start}

        # Создаем очередь для BFS.
        queue = QueueList()

        # Кладем стартовую вершину в очередь.
        queue.enqueue(start)

        # Пока очередь не пустая, продолжаем обход.
        while not queue.is_empty():
            # Берем вершину из начала очереди.
            current_vertex = queue.dequeue()

            # Добавляем ее в итоговый порядок.
            visited_order.append(current_vertex)

            # Идем по соседям текущей вершины.
            for neighbor in self.adjacency[current_vertex]:
                # Если сосед еще не посещался, запоминаем его.
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.enqueue(neighbor)

        # Возвращаем итог обхода.
        return visited_order

    # Создаем метод получения строк для красивого вывода.
    def display_lines(self) -> list[str]:
        # Если граф пустой, возвращаем одну строку.
        if not self.adjacency:
            return ["Граф пока пустой."]

        # Создаем список строк результата.
        lines: list[str] = []

        # Идем по всем вершинам и их соседям.
        for vertex, neighbors in self.adjacency.items():
            # Если соседи есть, соединяем их стрелками.
            if neighbors:
                neighbor_text = " -> ".join(neighbors)
            # Если соседей нет, показываем это явно.
            else:
                neighbor_text = "нет связей"

            # Добавляем строку вершины.
            lines.append(f"{vertex} -> {neighbor_text}")

        # Возвращаем готовые строки.
        return lines

    # Создаем метод очистки графа.
    def clear(self) -> None:
        # Полностью очищаем словарь смежности.
        self.adjacency.clear()

    # Создаем красивое строковое представление графа.
    def __str__(self) -> str:
        # Возвращаем основную информацию о графе.
        return f"Graph(directed={self.directed}, adjacency={self.adjacency})"