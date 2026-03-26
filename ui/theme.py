# Подключаем модуль ttk для настройки внешнего вида.
from tkinter import ttk


# Создаем основной темный цвет фона.
BG = "#0f172a"

# Создаем цвет поверхности карточек.
CARD = "#1f2937"

# Создаем цвет полей ввода и внутренних областей.
INPUT = "#0b1220"

# Создаем основной светлый цвет текста.
TEXT = "#e5e7eb"

# Создаем приглушенный цвет текста.
MUTED = "#94a3b8"

# Создаем яркий акцентный цвет.
ACCENT = "#38bdf8"


# Создаем функцию настройки общего внешнего вида приложения.
def setup_style(root) -> ttk.Style:
    # Создаем объект стиля.
    style = ttk.Style(root)

    # Выбираем тему clam, потому что она хорошо настраивается.
    style.theme_use("clam")

    # Красим фон главного окна.
    root.configure(bg=BG)

    # Настраиваем обычные фреймы приложения.
    style.configure("App.TFrame", background=BG)

    # Настраиваем карточки.
    style.configure("Card.TFrame", background=CARD, relief="flat")

    # Настраиваем главный заголовок.
    style.configure(
        "Header.TLabel",
        background=BG,
        foreground=TEXT,
        font=("Segoe UI", 22, "bold")
    )

    # Настраиваем подзаголовок.
    style.configure(
        "SubHeader.TLabel",
        background=BG,
        foreground=MUTED,
        font=("Segoe UI", 10)
    )

    # Настраиваем заголовок карточки.
    style.configure(
        "CardTitle.TLabel",
        background=CARD,
        foreground=TEXT,
        font=("Segoe UI", 14, "bold")
    )

    # Настраиваем дополнительный текст внутри карточек.
    style.configure(
        "CardText.TLabel",
        background=CARD,
        foreground=MUTED,
        font=("Segoe UI", 10)
    )

    # Настраиваем информативные надписи.
    style.configure(
        "Info.TLabel",
        background=CARD,
        foreground=TEXT,
        font=("Consolas", 10)
    )

    # Настраиваем акцентные кнопки.
    style.configure(
        "Accent.TButton",
        font=("Segoe UI", 10, "bold"),
        padding=8,
        background=ACCENT,
        foreground="#0f172a"
    )

    # Делаем поведение акцентной кнопки при наведении.
    style.map(
        "Accent.TButton",
        background=[("active", ACCENT), ("!disabled", ACCENT)],
        foreground=[("!disabled", "#0f172a")]
    )

    # Настраиваем мягкие кнопки.
    style.configure(
        "Soft.TButton",
        font=("Segoe UI", 10),
        padding=8,
        background="#273449",
        foreground=TEXT
    )

    # Делаем поведение мягкой кнопки при наведении.
    style.map(
        "Soft.TButton",
        background=[("active", "#334155"), ("!disabled", "#273449")],
        foreground=[("!disabled", TEXT)]
    )

    # Настраиваем сам блок вкладок.
    style.configure("TNotebook", background=BG, borderwidth=0)

    # Настраиваем отдельные вкладки.
    style.configure(
        "TNotebook.Tab",
        font=("Segoe UI", 10, "bold"),
        padding=(14, 10),
        background="#1e293b",
        foreground=TEXT
    )

    # Настраиваем выбранную вкладку.
    style.map(
        "TNotebook.Tab",
        background=[("selected", CARD)],
        foreground=[("selected", ACCENT)]
    )

    # Настраиваем поля ввода.
    style.configure(
        "TEntry",
        fieldbackground=INPUT,
        foreground=TEXT,
        padding=8
    )

    # Настраиваем флажки.
    style.configure(
        "TCheckbutton",
        background=CARD,
        foreground=TEXT
    )

    # Возвращаем готовый объект стиля.
    return style