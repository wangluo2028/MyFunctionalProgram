from functools import reduce

def f(x):
    return x*x

r=map(f, [1, 2,3, 4, 5, 6, 7, 8, 9])
print(list(r))

def addNumber(x, y):
    return x + y

print(reduce(addNumber, [1, 2, 3, 4, 5, 6]))



#print(reduce(combineNumber, [1, 2, 3, 4, 5]))

def str2int(s):
    def combineNumber(x, y):
        return x * 10 + y

    def char2Num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    return reduce(combineNumber, map(char2Num, s))



print(str2int('1234555555'))


def str2intverion2(s):
    def char2Num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    return reduce(lambda x, y : x*10+y, map(char2Num, s))

print(str2intverion2("1233212121"))

