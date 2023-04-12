from heapq import *


def solution(n, k, enemy):
    answer = 0
    heap = []

    for e in enemy:
        heappush(heap, -e)

        if n < e:
            while heap and k > 0 and n < e:
                n -= heappop(heap)
                k -= 1
            if n < e:
                break

        n -= e
        answer += 1

    return answer