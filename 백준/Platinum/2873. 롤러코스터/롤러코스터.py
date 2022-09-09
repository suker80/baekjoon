r, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]

# case 1 : 홀 홀 : 모든 값의 합

# case 2 : 홀 짝 : 모든 값의 합

# case 3 : 짝 홀 : 내려가면서 모든 값의 합

# case 4 : 짝 짝 : 마지막 점 위 혹은 왼쪽중 하나만 탐색가능
answer = ''


def move(key, r, c):
    global answer
    if key == 'R':
        answer += key
        return r, c + 1
    if key == 'D':
        answer += key
        return r + 1, c
    if key == 'L':
        answer += key
        return r, c - 1
    if key == 'U':
        answer += key
        return r - 1, c


if r % 2 == 1 and c % 2 == 1:
    for i in range(r):
        if i % 2 == 0:
            answer += 'R' * (c - 1)
        else:
            answer += 'L' * (c - 1)
        if i < r - 1:
            answer += 'D'

elif r % 2 == 1 and c % 2 == 0:
    for i in range(r):
        if i % 2 == 0:
            answer += 'R' * (c - 1)
        else:
            answer += 'L' * (c - 1)
        if i < r - 1:
            answer += 'D'

elif r % 2 == 0 and c % 2 == 1:
    for i in range(c):
        if i % 2 == 0:
            answer += 'D' * (r - 1)
        else:
            answer += 'U' * (r - 1)
        if i < c - 1:
            answer += 'R'


else:
    min_index = []
    min_val = float('inf')

    for i in range(r):
        for j in range(c):
            if (i + j) % 2 == 0: continue
            if min_val > graph[i][j]:
                min_index = [i, j]
                min_val = graph[i][j]
    i = 0
    flag = False

    answer += ("R" * (c - 1) + "D" + "L" * (c - 1)+ 'D') * ((min_index[0]) // 2)

    y = (min_index[0] // 2) * 2
    x = 0

    y_bound = y + 1
    x_bound = c - 1
    while y != y_bound or x != x_bound:
        if min_index != [y + 1, x] and y < y_bound:
            y += 1
            answer += 'D'
        elif min_index != [y - 1, x] and y == y_bound:
            y -= 1
            answer += 'U'
        if x != x_bound:
            x += 1
            answer += 'R'

    answer += ('D' + 'L' * (c - 1) + 'D' + 'R' * (c - 1)) * ((r - min_index[0] - 1) // 2)
print(answer)
