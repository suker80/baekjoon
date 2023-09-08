for _ in range(int(input())):
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.sort(key=lambda x: (x[0]))

    answer = []

    cafe = [[] for _ in range(100_001)]
    for x, y in arr:
        cafe[x].append(y)

    prev_y = 0
    cafe[0].append(0)
    for x in range(100_001):
        if cafe[x]:
            cafe[x].sort()
            if cafe[x][0] != prev_y:
                cafe[x].reverse()
            for y in cafe[x]:
                answer.append([x, y])
                prev_y = y
    lst = list(map(int, input().split()))
    m = lst[0]
    for k in lst[1:]:
        print(*answer[k])
