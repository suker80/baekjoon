t = int(input())


def solve(i, score):
    global answer
    if i == 11:
        answer = max(answer, score)
        return

    for idx in range(11):
        if player[i][idx] and pick[idx] == -1:
            pick[idx] = i
            solve(i + 1, score + player[i][idx])
            pick[idx] = -1
for _ in range(t):
    player = [list(map(int, input().split())) for _ in range(11)]
    pick = [-1] * 11
    answer = 0
    solve(0,0)
    print(answer)