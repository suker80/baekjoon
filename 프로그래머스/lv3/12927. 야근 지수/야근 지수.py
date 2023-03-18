from heapq import *


def solution(n, works):
    answer = 0
    heap = []
    for work in works:
        heappush(heap, -work)
    count = 0
    while heap and count < n:
        count += 1
        pop = heappop(heap) + 1
        if pop:
            heappush(heap, pop)
    for work in heap:
        answer += work ** 2
    return answer


