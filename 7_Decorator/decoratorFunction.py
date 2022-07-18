def decorator_func(func):
    def wrapper_func():
        print("wrapper function worked")
        return func()
    print("Decorator function worked")
    return wrapper_func

def show():
    print("Show method worked")

decorator_show = decorator_func(show)
decorator_show()