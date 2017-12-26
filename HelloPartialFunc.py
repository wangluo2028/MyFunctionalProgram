number = int('123456')
print(number)

number = int('1111', base=2)
print(number)


import functools
int2 = functools.partial(int, base = 2)
print(int2('1100'))

max2 = functools.partial(max, 10)
maxnumber = max2(5, 3, 2)
print(maxnumber)