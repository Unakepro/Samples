from threading import Thread


def simple_decorator(name, daemon):
    def actual_decorator(func):
        def wrapper():
            t = Thread(target=func, name=name, daemon=daemon)
            t.start()
        return wrapper

    return actual_decorator


@simple_decorator("Yop", False)
def say_hello():
    print("Hello")


say_hello()

