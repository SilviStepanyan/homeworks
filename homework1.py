#1.3
def sum_of_two_max_numbers_squares(a, b, c):
    if a > c < b:
        return a ** 2 + b ** 2
    elif a > b < c:
        return a ** 2 + c ** 2
    elif b > a < c:
        return b ** 2 + c ** 2


#1.5
def sum_of_numbers_from_a_to_b(a, b):
    res = -a
    while a < b:
        res = res + a
        a += 1
    return res


#1.6
def sum_of_all_numbers_from_min_to_max(a, b):
    if a > b:
        res = -b
        while b < a:
            res = res + b
            b += 1
        return res
    elif a < b:
        res = -a
        while a < b:
            res = res + a
            a += 1
        return res


#1.7
def pow(a, b):
    res = 1
    count = 0
    if a != 0:
        if b > 0:
            while count < b:
                res = res * a
                count += 1
            return res
        elif b < 0:
            while count < -b:
                res = res * (1/a)
                count += 1
            return res
        else:
            return 1
    else:
        if b > 0:
            return 0
        else:
            return "undefined"


#1.8
def improve(n, m):
    return ((m / (n ** 2)) + (2 * n)) / 3

def abs(n):
    if n > 0:
        return n
    else:
        return -n

def guess_enough(value, target):
    if abs(value**2 - target) < 0.0001:
        return True
    else:
        return False

def cube(m):
    n = 1
    while not guess_enough(n, m):
        n = improve(n, m)
    return n

