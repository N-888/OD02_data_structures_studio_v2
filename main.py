# Подключаем главное окно приложения.
from ui import DataStructuresApp


# Проверяем, что файл запускается напрямую.
if __name__ == "__main__":
    # Создаем объект приложения.
    app = DataStructuresApp()

    # Запускаем бесконечный цикл окна.
    app.mainloop()