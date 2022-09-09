import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0
store = [[0, i] for i in range(k)]
customer = []
for _ in range(n):
    i, v = map(int, input().split())
    store_time, store_id = heappop(store)
    heappush(store, [store_time + v, store_id])
    heappush(customer, [store_time + v, -store_id, i])

for i in range(n):
    cur_time,  _,c_id = heappop(customer)

    answer += c_id * (i + 1)
print(answer)
