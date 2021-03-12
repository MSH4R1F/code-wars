from itertools import permutations
def next_bigger(n):
    max_num = int(''.join(sorted(list(str(n)))[::-1]))
    x = n
    while n < max_num:
        x += 1
        if sorted(list(str(x))) == sorted(list(str(n))):
            return x
    return -1
