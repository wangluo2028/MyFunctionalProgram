MyList = list(map(lambda x : x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(MyList)

def build(x, y):
    return lambda: x*x + y*y

Mysquare = build(5, 5)
print(Mysquare())