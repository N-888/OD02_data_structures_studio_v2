# Подключаем Optional для значений, которые могут быть пустыми.
from typing import Optional


# Создаем класс Node для одного узла дерева.
class Node:
    # Создаем метод запуска узла.
    def __init__(self, key: int) -> None:
        # Сохраняем значение узла.
        self.key = key
        # Создаем ссылку на левый дочерний узел.
        self.left: Optional["Node"] = None
        # Создаем ссылку на правый дочерний узел.
        self.right: Optional["Node"] = None


# Создаем класс BinarySearchTree для бинарного дерева поиска.
class BinarySearchTree:
    # Создаем метод запуска дерева.
    def __init__(self) -> None:
        # Пока дерево пустое, поэтому корень равен None.
        self.root: Optional[Node] = None

    # Создаем публичный метод вставки нового значения.
    def insert(self, key: int) -> None:
        # Перезаписываем корень после рекурсивной вставки.
        self.root = self._insert_recursive(self.root, key)

    # Создаем внутренний рекурсивный метод вставки.
    def _insert_recursive(self, node: Optional[Node], key: int) -> Node:
        # Если узла нет, создаем новый узел.
        if node is None:
            return Node(key)

        # Если новое значение меньше, идем влево.
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)

        # Если новое значение больше, идем вправо.
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)

        # Если значение уже есть, просто возвращаем текущий узел без дубля.
        return node

    # Создаем метод поиска значения в дереве.
    def contains(self, key: int) -> bool:
        # Запускаем рекурсивный поиск от корня.
        return self._contains_recursive(self.root, key)

    # Создаем внутренний рекурсивный метод поиска.
    def _contains_recursive(self, node: Optional[Node], key: int) -> bool:
        # Если узла нет, значит число не найдено.
        if node is None:
            return False

        # Если число совпало, значит найдено.
        if key == node.key:
            return True

        # Если искомое число меньше, ищем слева.
        if key < node.key:
            return self._contains_recursive(node.left, key)

        # Иначе ищем справа.
        return self._contains_recursive(node.right, key)

    # Создаем метод симметричного обхода.
    def inorder(self) -> list[int]:
        # Создаем пустой список для результата.
        values: list[int] = []
        # Запускаем рекурсивный обход.
        self._inorder_recursive(self.root, values)
        # Возвращаем результат.
        return values

    # Создаем внутренний метод симметричного обхода.
    def _inorder_recursive(self, node: Optional[Node], values: list[int]) -> None:
        # Если узла нет, выходим.
        if node is None:
            return
        # Сначала идем влево.
        self._inorder_recursive(node.left, values)
        # Потом добавляем текущий узел.
        values.append(node.key)
        # Потом идем вправо.
        self._inorder_recursive(node.right, values)

    # Создаем метод прямого обхода.
    def preorder(self) -> list[int]:
        # Создаем пустой список для результата.
        values: list[int] = []
        # Запускаем рекурсивный обход.
        self._preorder_recursive(self.root, values)
        # Возвращаем результат.
        return values

    # Создаем внутренний метод прямого обхода.
    def _preorder_recursive(self, node: Optional[Node], values: list[int]) -> None:
        # Если узла нет, выходим.
        if node is None:
            return
        # Сначала добавляем текущий узел.
        values.append(node.key)
        # Затем идем влево.
        self._preorder_recursive(node.left, values)
        # Затем идем вправо.
        self._preorder_recursive(node.right, values)

    # Создаем метод обратного обхода.
    def postorder(self) -> list[int]:
        # Создаем пустой список для результата.
        values: list[int] = []
        # Запускаем рекурсивный обход.
        self._postorder_recursive(self.root, values)
        # Возвращаем результат.
        return values

    # Создаем внутренний метод обратного обхода.
    def _postorder_recursive(self, node: Optional[Node], values: list[int]) -> None:
        # Если узла нет, выходим.
        if node is None:
            return
        # Сначала идем влево.
        self._postorder_recursive(node.left, values)
        # Потом идем вправо.
        self._postorder_recursive(node.right, values)
        # После детей добавляем текущий узел.
        values.append(node.key)

    # Создаем метод вычисления высоты дерева.
    def height(self) -> int:
        # Возвращаем высоту от корня.
        return self._height_recursive(self.root)

    # Создаем внутренний метод вычисления высоты.
    def _height_recursive(self, node: Optional[Node]) -> int:
        # Если узла нет, высота равна 0.
        if node is None:
            return 0
        # Вычисляем высоту левого поддерева.
        left_height = self._height_recursive(node.left)
        # Вычисляем высоту правого поддерева.
        right_height = self._height_recursive(node.right)
        # Возвращаем большую высоту плюс текущий уровень.
        return max(left_height, right_height) + 1

    # Создаем метод полной очистки дерева.
    def clear(self) -> None:
        # Просто делаем корень пустым.
        self.root = None

    # Создаем метод красивого текстового вида дерева.
    def pretty_lines(self) -> list[str]:
        # Если дерево пустое, возвращаем одну понятную строку.
        if self.root is None:
            return ["Дерево пустое."]

        # Создаем список строк.
        lines: list[str] = []

        # Собираем дерево в текстовый вид.
        self._build_pretty_lines(self.root, "", True, lines)

        # Возвращаем готовые строки.
        return lines

    # Создаем внутренний метод построения дерева по строкам.
    def _build_pretty_lines(
        self,
        node: Optional[Node],
        prefix: str,
        is_tail: bool,
        lines: list[str]
    ) -> None:
        # Если узла нет, выходим.
        if node is None:
            return

        # Выбираем вид ветки.
        branch = "└── " if is_tail else "├── "

        # Добавляем строку текущего узла.
        lines.append(f"{prefix}{branch}{node.key}")

        # Создаем список детей.
        children: list[Node] = []

        # Если есть левый ребенок, добавляем его.
        if node.left is not None:
            children.append(node.left)

        # Если есть правый ребенок, добавляем его.
        if node.right is not None:
            children.append(node.right)

        # Идем по всем детям.
        for index, child in enumerate(children):
            # Формируем новый префикс.
            next_prefix = prefix + ("    " if is_tail else "│   ")
            # Рекурсивно строим следующие строки.
            self._build_pretty_lines(child, next_prefix, index == len(children) - 1, lines)

    # Создаем красивое строковое представление дерева.
    def __str__(self) -> str:
        # Возвращаем дерево через симметричный обход.
        return f"BinarySearchTree({self.inorder()})"