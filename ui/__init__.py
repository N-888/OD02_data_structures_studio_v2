# Подключаем главное окно приложения из файла app.py.
from .app import DataStructuresApp

# Указываем, что удобно импортировать из пакета ui.
__all__ = ["DataStructuresApp"]