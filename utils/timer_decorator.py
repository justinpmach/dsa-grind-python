import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {(time.time() - start):.4f} seconds")
        return result
    return wrapper
