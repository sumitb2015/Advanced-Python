
import time

def timer(func):
    """
    This function can be used as a decorator to time the execution of a function.

    :param func: The function to be timed
    :type func: function
    :return: The function wrapped with the timer
    :rtype: function
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time-start_time} seconds")
        return result
    return wrapper

@timer
def test2():
    """
    This function is an example of a function that is being timed using the timer decorator.
    """
    for _ in range(10000000):
        pass
test2()

@timer
def test3():
    """
    This function is an example of a function that is being timed using the timer decorator.
    """
    time.sleep(10)
test3()