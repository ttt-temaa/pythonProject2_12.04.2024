import logging
from typing import Any


def get_module_logger(name: Any) -> logging.Logger:
    """Возвращает логгер для данного модуля."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # Создаем handler для стандартного вывода
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # Создаем форматтера для вывода в консоль
    file = logging.FileHandler(f"{name}.log", "w", encoding="UTF=8")
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)s: %(levelname)s - %(message)s")
    console.setFormatter(formatter)
    file.setFormatter(formatter)
    # Добавляем handler в логгер
    logger.addHandler(console)
    logger.addHandler(file)
    return logger
