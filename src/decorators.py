from functools import wraps


def log(filename=None):
    """Декоратор для логирования начала и конца выполнения функции, а также результатов или ошибок."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            function_name = func.__name__
            try:
                result = func(*args, **kwargs)
                log_message = f"{function_name} ok: {result}"
            except Exception as e:
                log_message = f"{function_name} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                raise  # пробрасываем исключение дальше
            finally:
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)
            return result

        return wrapper

    return decorator
