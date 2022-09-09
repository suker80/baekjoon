n, l = map(int, input().split())
import sys
input = sys.stdin.readline
graph = [list(map(int,input().split())) for _ in range(n)]

def check(arr):
    start = arr[0]
    count = 0
    for i in range(n):
        if abs(arr[i] - start) > 1:
            return False

        elif arr[i] - start == 1:
            if count - l >= 0:
                start = arr[i]
                count = 1
            else:
                return False
        elif start - arr[i] == 1:

            for k in range(l):
                if (i + k < n and arr[i] == arr[i + k]) == False:
                    return False
            start = arr[i]
            count = - l +1
        elif arr[i] == start:

            count += 1
            continue

    return True
answer = 0
for i in range(n):
    answer += check(graph[i])
    answer += check([graph[j][i] for j in range(n)])
print(answer)