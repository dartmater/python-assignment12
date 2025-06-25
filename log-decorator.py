import logging


logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(
            f"\nfunction: {func.__name__}"
            f"\npositional parameters: {args if args else 'none'}"
            f"\nkeyword parameters: {kwargs if kwargs else 'none'}"
            f"\nreturn: {result}\n"
        )
        return result
    return wrapper

# Function 1: No parameters
@logger_decorator
def say_hello():
    print("Hello, World!")

# Function 2: Positional arguments
@logger_decorator
def check_args(*args):
    return True

# Function 3: Keyword arguments
@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

# Mainline code
if __name__ == "__main__":
    say_hello()
    check_args(10, 20, 30)
    return_decorator(color="blue", size="large")
