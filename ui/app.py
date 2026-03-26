# Подключаем Tkinter.
import tkinter as tk

# Подключаем ttk и готовые окна сообщений.
from tkinter import ttk, messagebox

# Подключаем Optional для метода, который может вернуть пустое значение.
from typing import Optional

# Подключаем структуры данных из нашего пакета.
from data_structures import BinarySearchTree, Graph, QueueList, Stack

# Подключаем цвета и функцию настройки стиля.
from .theme import BG, CARD, INPUT, TEXT, setup_style


# Создаем главное окно приложения.
class DataStructuresApp(tk.Tk):
    # Создаем метод запуска окна.
    def __init__(self) -> None:
        # Запускаем родительский класс Tk.
        super().__init__()

        # Задаем заголовок окна.
        self.title("Data Structures Studio 2.0")

        # Задаем стартовый размер окна.
        self.geometry("1200x760")

        # Указываем минимальный размер окна.
        self.minsize(1000, 680)

        # Красим фон окна.
        self.configure(bg=BG)

        # Применяем стили приложения.
        self.style = setup_style(self)

        # Создаем объект стека.
        self.stack = Stack()

        # Создаем объект очереди.
        self.queue = QueueList()

        # Создаем объект дерева.
        self.tree = BinarySearchTree()

        # Создаем объект графа в направленном режиме.
        self.graph = Graph(directed=True)

        # Строим весь интерфейс.
        self._build_layout()

        # Обновляем отображение стека.
        self._refresh_stack_view()

        # Обновляем отображение очереди.
        self._refresh_queue_view()

        # Обновляем отображение дерева.
        self._refresh_tree_view()

        # Обновляем отображение графа.
        self._refresh_graph_view()

    # Создаем метод построения общей структуры окна.
    def _build_layout(self) -> None:
        # Создаем главный контейнер.
        container = ttk.Frame(self, style="App.TFrame", padding=20)

        # Растягиваем контейнер на все окно.
        container.pack(fill="both", expand=True)

        # Создаем главный заголовок.
        ttk.Label(
            container,
            text="Data Structures Studio 2.0",
            style="Header.TLabel"
        ).pack(anchor="w")

        # Создаем подзаголовок.
        ttk.Label(
            container,
            text="Стильное окно для работы со стеком, очередью, деревом и графом на Tkinter.",
            style="SubHeader.TLabel"
        ).pack(anchor="w", pady=(4, 18))

        # Создаем блок вкладок.
        notebook = ttk.Notebook(container)

        # Растягиваем вкладки.
        notebook.pack(fill="both", expand=True)

        # Создаем вкладку стека.
        self.stack_tab = ttk.Frame(notebook, style="App.TFrame", padding=12)

        # Создаем вкладку очереди.
        self.queue_tab = ttk.Frame(notebook, style="App.TFrame", padding=12)

        # Создаем вкладку дерева.
        self.tree_tab = ttk.Frame(notebook, style="App.TFrame", padding=12)

        # Создаем вкладку графа.
        self.graph_tab = ttk.Frame(notebook, style="App.TFrame", padding=12)

        # Добавляем вкладку стека.
        notebook.add(self.stack_tab, text="📚 Стек")

        # Добавляем вкладку очереди.
        notebook.add(self.queue_tab, text="🧾 Очередь")

        # Добавляем вкладку дерева.
        notebook.add(self.tree_tab, text="🌳 Дерево")

        # Добавляем вкладку графа.
        notebook.add(self.graph_tab, text="🕸 Граф")

        # Строим содержимое вкладки стека.
        self._build_stack_tab()

        # Строим содержимое вкладки очереди.
        self._build_queue_tab()

        # Строим содержимое вкладки дерева.
        self._build_tree_tab()

        # Строим содержимое вкладки графа.
        self._build_graph_tab()

    # Создаем вспомогательный метод карточки.
    def _create_card(self, parent, title: str, subtitle: str = ""):
        # Создаем фрейм карточки.
        card = ttk.Frame(parent, style="Card.TFrame", padding=16)

        # Добавляем заголовок карточки.
        ttk.Label(card, text=title, style="CardTitle.TLabel").pack(anchor="w")

        # Если есть подзаголовок, выводим его.
        if subtitle:
            ttk.Label(card, text=subtitle, style="CardText.TLabel").pack(anchor="w", pady=(2, 12))
        else:
            ttk.Label(card, text="", style="CardText.TLabel").pack(anchor="w", pady=(0, 12))

        # Возвращаем карточку.
        return card

    # Создаем вспомогательный метод текстовой области.
    def _make_text_area(self, parent, height: int = 12) -> tk.Text:
        # Создаем многострочное текстовое поле.
        text = tk.Text(
            parent,
            height=height,
            bg=INPUT,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            bd=0,
            font=("Consolas", 10),
            padx=12,
            pady=12
        )

        # Запрещаем ручное редактирование.
        text.configure(state="disabled")

        # Возвращаем готовое поле.
        return text

    # Создаем вспомогательный метод записи текста в поле.
    def _set_text(self, widget: tk.Text, lines: list[str]) -> None:
        # Временно открываем поле для записи.
        widget.configure(state="normal")

        # Полностью очищаем текущее содержимое.
        widget.delete("1.0", tk.END)

        # Вставляем новые строки.
        widget.insert(tk.END, "\n".join(lines))

        # Снова запрещаем ручное редактирование.
        widget.configure(state="disabled")

    # Создаем вкладку стека.
    def _build_stack_tab(self) -> None:
        # Разрешаем первой колонке растягиваться.
        self.stack_tab.columnconfigure(0, weight=1)

        # Разрешаем второй колонке растягиваться.
        self.stack_tab.columnconfigure(1, weight=1)

        # Создаем левую карточку управления.
        input_card = self._create_card(
            self.stack_tab,
            "Управление стеком",
            "LIFO: последний пришёл — первый ушёл."
        )

        # Ставим карточку в сетку.
        input_card.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=(0, 8))

        # Создаем переменную для поля ввода.
        self.stack_value_var = tk.StringVar()

        # Создаем поле ввода.
        ttk.Entry(input_card, textvariable=self.stack_value_var).pack(fill="x")

        # Создаем блок кнопок.
        buttons = ttk.Frame(input_card, style="Card.TFrame")

        # Размещаем блок кнопок.
        buttons.pack(fill="x", pady=12)

        # Создаем кнопку добавления.
        ttk.Button(
            buttons,
            text="Добавить",
            style="Accent.TButton",
            command=self._stack_push
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку удаления верхнего элемента.
        ttk.Button(
            buttons,
            text="Удалить верхний",
            style="Soft.TButton",
            command=self._stack_pop
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку просмотра верхнего элемента.
        ttk.Button(
            buttons,
            text="Посмотреть верхний",
            style="Soft.TButton",
            command=self._stack_peek
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку очистки.
        ttk.Button(
            buttons,
            text="Очистить",
            style="Soft.TButton",
            command=self._stack_clear
        ).pack(side="left")

        # Создаем строку статуса.
        self.stack_status = ttk.Label(input_card, text="Готово к работе.", style="Info.TLabel")

        # Показываем строку статуса.
        self.stack_status.pack(anchor="w", pady=(8, 0))

        # Создаем правую карточку просмотра.
        view_card = self._create_card(
            self.stack_tab,
            "Содержимое стека",
            "Правый край списка — вершина стека."
        )

        # Ставим правую карточку в сетку.
        view_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=(0, 8))

        # Создаем текстовую область.
        self.stack_text = self._make_text_area(view_card, height=18)

        # Размещаем текстовую область.
        self.stack_text.pack(fill="both", expand=True)

    # Создаем действие добавления в стек.
    def _stack_push(self) -> None:
        # Получаем текст из поля и убираем лишние пробелы.
        value = self.stack_value_var.get().strip()

        # Если поле пустое, показываем предупреждение.
        if not value:
            messagebox.showwarning("Пустое поле", "Введите значение для добавления в стек.")
            return

        # Добавляем значение в стек.
        self.stack.push(value)

        # Очищаем поле ввода.
        self.stack_value_var.set("")

        # Обновляем статус.
        self.stack_status.configure(text=f"Добавлено в стек: {value}")

        # Обновляем вид.
        self._refresh_stack_view()

    # Создаем действие удаления из стека.
    def _stack_pop(self) -> None:
        # Пытаемся удалить элемент.
        try:
            # Забираем верхний элемент.
            removed = self.stack.pop()

            # Обновляем статус.
            self.stack_status.configure(text=f"Удалено из стека: {removed}")

            # Обновляем вид.
            self._refresh_stack_view()

        # Если стек пустой, показываем ошибку.
        except IndexError as error:
            messagebox.showerror("Ошибка", str(error))

    # Создаем действие просмотра верхнего элемента.
    def _stack_peek(self) -> None:
        # Пытаемся посмотреть верхний элемент.
        try:
            # Получаем значение вершины.
            top_value = self.stack.peek()

            # Обновляем статус.
            self.stack_status.configure(text=f"Верхний элемент: {top_value}")

        # Если стек пустой, показываем ошибку.
        except IndexError as error:
            messagebox.showerror("Ошибка", str(error))

    # Создаем действие очистки стека.
    def _stack_clear(self) -> None:
        # Очищаем стек.
        self.stack.clear()

        # Обновляем статус.
        self.stack_status.configure(text="Стек очищен.")

        # Обновляем вид.
        self._refresh_stack_view()

    # Создаем метод обновления вида стека.
    def _refresh_stack_view(self) -> None:
        # Формируем строки для вывода.
        lines = [
            "Элементы:",
            str(self.stack.to_list()),
            "",
            f"Размер: {self.stack.size()}",
            f"Пустой: {self.stack.is_empty()}"
        ]

        # Записываем строки в текстовую область.
        self._set_text(self.stack_text, lines)

    # Создаем вкладку очереди.
    def _build_queue_tab(self) -> None:
        # Разрешаем первой колонке растягиваться.
        self.queue_tab.columnconfigure(0, weight=1)

        # Разрешаем второй колонке растягиваться.
        self.queue_tab.columnconfigure(1, weight=1)

        # Создаем карточку управления.
        input_card = self._create_card(
            self.queue_tab,
            "Управление очередью",
            "FIFO: первый пришёл — первый ушёл."
        )

        # Размещаем карточку в сетке.
        input_card.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=(0, 8))

        # Создаем переменную для ввода.
        self.queue_value_var = tk.StringVar()

        # Создаем поле ввода.
        ttk.Entry(input_card, textvariable=self.queue_value_var).pack(fill="x")

        # Создаем блок кнопок.
        buttons = ttk.Frame(input_card, style="Card.TFrame")

        # Размещаем блок кнопок.
        buttons.pack(fill="x", pady=12)

        # Создаем кнопку добавления.
        ttk.Button(
            buttons,
            text="Добавить",
            style="Accent.TButton",
            command=self._queue_enqueue
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку удаления первого элемента.
        ttk.Button(
            buttons,
            text="Удалить первый",
            style="Soft.TButton",
            command=self._queue_dequeue
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку просмотра первого элемента.
        ttk.Button(
            buttons,
            text="Посмотреть первый",
            style="Soft.TButton",
            command=self._queue_peek
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку очистки.
        ttk.Button(
            buttons,
            text="Очистить",
            style="Soft.TButton",
            command=self._queue_clear
        ).pack(side="left")

        # Создаем строку статуса.
        self.queue_status = ttk.Label(input_card, text="Готово к работе.", style="Info.TLabel")

        # Показываем строку статуса.
        self.queue_status.pack(anchor="w", pady=(8, 0))

        # Создаем карточку просмотра.
        view_card = self._create_card(
            self.queue_tab,
            "Содержимое очереди",
            "Левый край списка — начало очереди."
        )

        # Размещаем карточку просмотра.
        view_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=(0, 8))

        # Создаем текстовую область очереди.
        self.queue_text = self._make_text_area(view_card, height=18)

        # Показываем текстовую область.
        self.queue_text.pack(fill="both", expand=True)

    # Создаем действие добавления в очередь.
    def _queue_enqueue(self) -> None:
        # Получаем введенное значение.
        value = self.queue_value_var.get().strip()

        # Если поле пустое, показываем предупреждение.
        if not value:
            messagebox.showwarning("Пустое поле", "Введите значение для добавления в очередь.")
            return

        # Добавляем значение в очередь.
        self.queue.enqueue(value)

        # Очищаем поле ввода.
        self.queue_value_var.set("")

        # Обновляем статус.
        self.queue_status.configure(text=f"Добавлено в очередь: {value}")

        # Обновляем вид.
        self._refresh_queue_view()

    # Создаем действие удаления из очереди.
    def _queue_dequeue(self) -> None:
        # Пытаемся удалить элемент.
        try:
            # Получаем первый элемент.
            removed = self.queue.dequeue()

            # Обновляем статус.
            self.queue_status.configure(text=f"Удалено из очереди: {removed}")

            # Обновляем вид.
            self._refresh_queue_view()

        # Если очередь пустая, показываем ошибку.
        except IndexError as error:
            messagebox.showerror("Ошибка", str(error))

    # Создаем действие просмотра первого элемента.
    def _queue_peek(self) -> None:
        # Пытаемся посмотреть первый элемент.
        try:
            # Получаем первый элемент.
            first_value = self.queue.peek()

            # Обновляем статус.
            self.queue_status.configure(text=f"Первый элемент: {first_value}")

        # Если очередь пустая, показываем ошибку.
        except IndexError as error:
            messagebox.showerror("Ошибка", str(error))

    # Создаем действие очистки очереди.
    def _queue_clear(self) -> None:
        # Очищаем очередь.
        self.queue.clear()

        # Обновляем статус.
        self.queue_status.configure(text="Очередь очищена.")

        # Обновляем вид.
        self._refresh_queue_view()

    # Создаем метод обновления вида очереди.
    def _refresh_queue_view(self) -> None:
        # Формируем строки для вывода.
        lines = [
            "Элементы:",
            str(self.queue.to_list()),
            "",
            f"Размер: {self.queue.size()}",
            f"Пустая: {self.queue.is_empty()}"
        ]

        # Записываем данные в текстовую область.
        self._set_text(self.queue_text, lines)

    # Создаем вкладку дерева.
    def _build_tree_tab(self) -> None:
        # Разрешаем первой колонке растягиваться.
        self.tree_tab.columnconfigure(0, weight=1)

        # Разрешаем второй колонке растягиваться.
        self.tree_tab.columnconfigure(1, weight=1)

        # Создаем левую карточку управления.
        left_card = self._create_card(
            self.tree_tab,
            "Управление деревом",
            "Бинарное дерево поиска работает с числами."
        )

        # Размещаем левую карточку.
        left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=(0, 8))

        # Создаем переменную ввода для дерева.
        self.tree_value_var = tk.StringVar()

        # Создаем поле ввода.
        ttk.Entry(left_card, textvariable=self.tree_value_var).pack(fill="x")

        # Создаем блок кнопок.
        buttons = ttk.Frame(left_card, style="Card.TFrame")

        # Размещаем блок кнопок.
        buttons.pack(fill="x", pady=12)

        # Создаем кнопку вставки числа.
        ttk.Button(
            buttons,
            text="Вставить",
            style="Accent.TButton",
            command=self._tree_insert
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку поиска числа.
        ttk.Button(
            buttons,
            text="Найти",
            style="Soft.TButton",
            command=self._tree_search
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку очистки дерева.
        ttk.Button(
            buttons,
            text="Очистить",
            style="Soft.TButton",
            command=self._tree_clear
        ).pack(side="left")

        # Создаем строку статуса дерева.
        self.tree_status = ttk.Label(left_card, text="Готово к работе.", style="Info.TLabel")

        # Показываем строку статуса.
        self.tree_status.pack(anchor="w", pady=(8, 8))

        # Создаем область для обходов и высоты.
        self.tree_info = self._make_text_area(left_card, height=11)

        # Показываем область обходов и высоты.
        self.tree_info.pack(fill="both", expand=True)

        # Создаем правую карточку схемы дерева.
        right_card = self._create_card(
            self.tree_tab,
            "Визуальная схема дерева",
            "Схема обновляется после каждой операции."
        )

        # Размещаем правую карточку.
        right_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=(0, 8))

        # Создаем область показа дерева.
        self.tree_view = self._make_text_area(right_card, height=22)

        # Показываем область дерева.
        self.tree_view.pack(fill="both", expand=True)

    # Создаем метод получения числа из поля дерева.
    def _parse_tree_value(self) -> Optional[int]:
        # Получаем текст из поля.
        raw_value = self.tree_value_var.get().strip()

        # Если поле пустое, предупреждаем пользователя.
        if not raw_value:
            messagebox.showwarning("Пустое поле", "Введите целое число для дерева.")
            return None

        # Пытаемся превратить текст в число.
        try:
            return int(raw_value)

        # Если число введено неправильно, показываем ошибку.
        except ValueError:
            messagebox.showerror("Ошибка", "Для дерева нужно ввести целое число.")
            return None

    # Создаем действие вставки в дерево.
    def _tree_insert(self) -> None:
        # Получаем число из поля.
        value = self._parse_tree_value()

        # Если число не удалось получить, выходим.
        if value is None:
            return

        # Добавляем число в дерево.
        self.tree.insert(value)

        # Очищаем поле ввода.
        self.tree_value_var.set("")

        # Обновляем статус.
        self.tree_status.configure(text=f"В дерево добавлено число: {value}")

        # Обновляем вид.
        self._refresh_tree_view()

    # Создаем действие поиска в дереве.
    def _tree_search(self) -> None:
        # Получаем число из поля.
        value = self._parse_tree_value()

        # Если число не удалось получить, выходим.
        if value is None:
            return

        # Выполняем поиск.
        result = self.tree.contains(value)

        # Формируем понятный статус.
        if result:
            self.tree_status.configure(text=f"Поиск числа {value}: найдено")
        else:
            self.tree_status.configure(text=f"Поиск числа {value}: не найдено")

        # Обновляем вид дерева.
        self._refresh_tree_view()

    # Создаем действие очистки дерева.
    def _tree_clear(self) -> None:
        # Очищаем дерево.
        self.tree.clear()

        # Обновляем статус.
        self.tree_status.configure(text="Дерево очищено.")

        # Обновляем вид.
        self._refresh_tree_view()

    # Создаем метод обновления вида дерева.
    def _refresh_tree_view(self) -> None:
        # Готовим строки с обходами и высотой.
        info_lines = [
            f"Симметричный обход: {self.tree.inorder()}",
            f"Прямой обход: {self.tree.preorder()}",
            f"Обратный обход: {self.tree.postorder()}",
            f"Высота: {self.tree.height()}",
        ]

        # Пишем обходы и высоту в левую область.
        self._set_text(self.tree_info, info_lines)

        # Пишем красивую схему дерева в правую область.
        self._set_text(self.tree_view, self.tree.pretty_lines())

    # Создаем вкладку графа.
    def _build_graph_tab(self) -> None:
        # Разрешаем первой колонке растягиваться.
        self.graph_tab.columnconfigure(0, weight=1)

        # Разрешаем второй колонке растягиваться.
        self.graph_tab.columnconfigure(1, weight=1)

        # Создаем левую карточку управления графом.
        left_card = self._create_card(
            self.graph_tab,
            "Управление графом",
            "Можно строить направленный или ненаправленный граф."
        )

        # Размещаем левую карточку.
        left_card.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=(0, 8))

        # Создаем строку для выбора режима графа.
        mode_row = ttk.Frame(left_card, style="Card.TFrame")

        # Показываем эту строку.
        mode_row.pack(fill="x")

        # Создаем булеву переменную режима графа.
        self.graph_directed_var = tk.BooleanVar(value=True)

        # Создаем флажок направленного режима.
        ttk.Checkbutton(
            mode_row,
            text="Направленный граф",
            variable=self.graph_directed_var
        ).pack(side="left")

        # Создаем кнопку применения режима.
        ttk.Button(
            mode_row,
            text="Применить режим",
            style="Soft.TButton",
            command=self._apply_graph_mode
        ).pack(side="left", padx=(12, 0))

        # Создаем строку для двух полей ввода вершин.
        fields = ttk.Frame(left_card, style="Card.TFrame")

        # Показываем строку полей.
        fields.pack(fill="x", pady=12)

        # Создаем переменную стартовой вершины.
        self.graph_start_var = tk.StringVar()

        # Создаем переменную конечной вершины.
        self.graph_end_var = tk.StringVar()

        # Создаем поле первой вершины.
        ttk.Entry(fields, textvariable=self.graph_start_var).grid(row=0, column=0, sticky="ew", padx=(0, 8))

        # Создаем поле второй вершины.
        ttk.Entry(fields, textvariable=self.graph_end_var).grid(row=0, column=1, sticky="ew")

        # Разрешаем первой колонке растягиваться.
        fields.columnconfigure(0, weight=1)

        # Разрешаем второй колонке растягиваться.
        fields.columnconfigure(1, weight=1)

        # Создаем строку кнопок.
        buttons = ttk.Frame(left_card, style="Card.TFrame")

        # Показываем строку кнопок.
        buttons.pack(fill="x")

        # Создаем кнопку добавления ребра.
        ttk.Button(
            buttons,
            text="Добавить ребро",
            style="Accent.TButton",
            command=self._graph_add_edge
        ).pack(side="left", padx=(0, 8))

        # Создаем кнопку очистки графа.
        ttk.Button(
            buttons,
            text="Очистить граф",
            style="Soft.TButton",
            command=self._graph_clear
        ).pack(side="left")

        # Создаем строку для BFS.
        bfs_row = ttk.Frame(left_card, style="Card.TFrame")

        # Показываем строку BFS.
        bfs_row.pack(fill="x", pady=12)

        # Создаем переменную стартовой вершины BFS.
        self.graph_bfs_var = tk.StringVar()

        # Создаем поле для стартовой вершины BFS.
        ttk.Entry(bfs_row, textvariable=self.graph_bfs_var).pack(side="left", fill="x", expand=True, padx=(0, 8))

        # Создаем кнопку запуска BFS.
        ttk.Button(
            bfs_row,
            text="BFS",
            style="Soft.TButton",
            command=self._graph_bfs
        ).pack(side="left")

        # Создаем строку статуса графа.
        self.graph_status = ttk.Label(left_card, text="Готово к работе.", style="Info.TLabel")

        # Показываем строку статуса.
        self.graph_status.pack(anchor="w", pady=(8, 8))

        # Создаем область для результата BFS.
        self.graph_bfs_result = self._make_text_area(left_card, height=7)

        # Показываем область результата BFS.
        self.graph_bfs_result.pack(fill="both", expand=True)

        # Сразу пишем стартовый текст.
        self._set_text(self.graph_bfs_result, ["BFS пока не запускался."])

        # Создаем правую карточку списка смежности.
        right_card = self._create_card(
            self.graph_tab,
            "Список смежности",
            "Здесь показаны все связи между вершинами."
        )

        # Размещаем правую карточку.
        right_card.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=(0, 8))

        # Создаем область показа графа.
        self.graph_view = self._make_text_area(right_card, height=22)

        # Показываем область графа.
        self.graph_view.pack(fill="both", expand=True)

    # Создаем действие применения режима графа.
    def _apply_graph_mode(self) -> None:
        # Пересоздаем граф в выбранном режиме.
        self.graph = Graph(directed=self.graph_directed_var.get())

        # Определяем понятное название режима.
        if self.graph_directed_var.get():
            mode_name = "направленный"
        else:
            mode_name = "ненаправленный"

        # Обновляем статус.
        self.graph_status.configure(text=f"Выбран режим: {mode_name}. Граф начат заново.")

        # Обновляем вид графа.
        self._refresh_graph_view()

        # Сбрасываем текст BFS.
        self._set_text(self.graph_bfs_result, ["BFS пока не запускался."])

    # Создаем действие добавления ребра.
    def _graph_add_edge(self) -> None:
        # Получаем первую вершину.
        start = self.graph_start_var.get().strip()

        # Получаем вторую вершину.
        end = self.graph_end_var.get().strip()

        # Если хотя бы одно поле пустое, предупреждаем пользователя.
        if not start or not end:
            messagebox.showwarning("Пустое поле", "Введите обе вершины для создания ребра.")
            return

        # Добавляем ребро в граф.
        self.graph.add_edge(start, end)

        # Очищаем первое поле.
        self.graph_start_var.set("")

        # Очищаем второе поле.
        self.graph_end_var.set("")

        # Определяем стрелку для статуса.
        if self.graph.directed:
            arrow = "→"
        else:
            arrow = "↔"

        # Обновляем статус.
        self.graph_status.configure(text=f"Добавлена связь: {start} {arrow} {end}")

        # Обновляем вид графа.
        self._refresh_graph_view()

    # Создаем действие очистки графа.
    def _graph_clear(self) -> None:
        # Очищаем граф.
        self.graph.clear()

        # Обновляем статус.
        self.graph_status.configure(text="Граф очищен.")

        # Обновляем вид графа.
        self._refresh_graph_view()

        # Сбрасываем текст BFS.
        self._set_text(self.graph_bfs_result, ["BFS пока не запускался."])

    # Создаем действие обхода BFS.
    def _graph_bfs(self) -> None:
        # Получаем стартовую вершину.
        start = self.graph_bfs_var.get().strip()

        # Если поле пустое, предупреждаем пользователя.
        if not start:
            messagebox.showwarning("Пустое поле", "Введите стартовую вершину для BFS.")
            return

        # Пытаемся выполнить BFS.
        try:
            # Получаем порядок обхода.
            order = self.graph.bfs(start)

            # Обновляем статус.
            self.graph_status.configure(text=f"BFS успешно выполнен от вершины: {start}")

            # Показываем результат.
            self._set_text(self.graph_bfs_result, [f"Порядок обхода BFS: {order}"])

        # Если вершина не существует, показываем ошибку.
        except KeyError as error:
            messagebox.showerror("Ошибка", str(error))

    # Создаем метод обновления вида графа.
    def _refresh_graph_view(self) -> None:
        # Формируем название режима.
        if self.graph.directed:
            mode_name = "направленный"
        else:
            mode_name = "ненаправленный"

        # Формируем строки для вывода.
        lines = [f"Режим: {mode_name}", ""] + self.graph.display_lines()

        # Показываем эти строки в области графа.
        self._set_text(self.graph_view, lines)