def twenty_twenty_four(x):
    
    return int(str(g(g(x))) + str((f(f(f(x))))) + str(f(x)))

def f(x):
    return x - 1

def g(x):
    return x * 2

def h(x, y):
    return int(str(x) + str(y))

print(twenty_twenty_four(5))