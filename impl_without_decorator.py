def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
    return wrapper

def func2():
    print("I am func2")
    
def func3():
    print("I am func3")

x = func(func2)
y = func(func3)
print(x)
x()
y()
