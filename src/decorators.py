from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable[[Any], Any]:
    """
    Декоратор для логирования вызова функций.

    Args:filename (str): Имя файла для записи лога. Если не указан, то логи будут выводиться в консоль.
    Returns: Callable: Декорируемая функция.
    """

    def decorator(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Получаем текущее время
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:

                # Вызываем функцию
                result = func(*args, **kwargs)

                # Записываем в лог try вызов функции
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{current_time} {func.__name__} ok\n")
                else:
                    print(f"{current_time} {func.__name__} ok")

                return result, f"{current_time} {func.__name__} ok"
            except Exception as e:
                # Записываем в лог информацию об ошибке
                if filename:
                    with open(filename, "a") as f:
                        f.write(f"{current_time} {func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{current_time} {func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    return f"{current_time} {func.__name__} error: {e}. Inputs: {args}, {kwargs}"

        return wrapper

    return decorator
