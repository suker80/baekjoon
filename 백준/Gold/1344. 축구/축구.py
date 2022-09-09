a, b = [int(input()) for i in range(2)]
from math import factorial, pow

prime = [2, 3, 5, 7, 11, 13, 17]
p_a = p_b = 0
a, b = a / 100, b / 100


def comb(r):
    return factorial(18) / (factorial(18 - r) * factorial(r))


for i in range(len(prime)):
    p = prime[i]
    p_a += comb(p) * pow(a, p) * pow(1 - a, 18 - p)
    p_b += comb(p) * pow(b, p) * pow(1 - b, 18 - p)
print(p_a + p_b - (p_a * p_b))
