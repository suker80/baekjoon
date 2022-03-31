import time

a = list(range(1, int(1e+7)))
b = list(range(int(1e+7), 1,-1))
start = time.time()
a, b = b, a
print(time.time() - start)
print(a[:10])
print(b[:10])