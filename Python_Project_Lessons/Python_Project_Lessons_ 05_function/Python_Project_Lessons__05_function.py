# Функция def №1

def func (x, a):
    return x + a

print(func(23, 23))

# №2
def func (x):
    def add(a):
        return x + a
    return add

test = func(100)
print(test(200))

# Функция не чего не возвращает.
def func2():
    pass

# №3. c - по умолчанию значение. потом можно это значение не указывать
def func2(a, b, c = 3):
    res = a + b
    res *= c
    return res

print(func2(23, 43))

# через функцию передать кортедж
def func2(*args):
    return args

print(func2(23, 43, 4, 2))

# через функцию передать словаря
def func2(**args):
    return args

print(func2(a = 23, b = 43, c = 34))

# lambda - функция в одну строку с одной опирации

add = lambda x, y: x * y
print(add(3,4))
print((lambda x, y: x * y)(32,3))
