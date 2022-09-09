n = int(input())
m = int(input())
if m:
    button = list(map(int,input().split()))
else:
    button = []
start = 100

button_set = list(set(range(10)).difference(button))

l = len(str(n))

import itertools

min_button = abs(start-n)

for i in range(1,l+2):
    for p in itertools.product(button_set,repeat=i):
        p= map(str,p)
        
        b = int(''.join(p))
        
        
        min_button = min(min_button, abs(b-n) +i)

print(min_button)
        