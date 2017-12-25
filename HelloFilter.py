def is_odd(n):
    return n%2==1

oddlist = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(oddlist)


def str_not_empty(s):
    return s and s.strip()

not_empty_string = list(filter(str_not_empty, ['A', '', 'B', 'C', None, '  ']))
print(not_empty_string)


test_string = "  abbcc     "
TripTestString = test_string.strip()
print(TripTestString)

if TripTestString:
    print('not empty string')
else:
    print('empty string')



def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break


