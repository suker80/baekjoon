n, m, l, k = map(int, input().split())

star = [list(map(int, input().split())) for _ in range(k)]

answer = 0


for i in range(k):
    for j in range(k):
        cnt = 0
        x = star[i][0]
        y = star[j][1]

        for idx in range(k):
            star_x, star_y = star[idx]

            if x <= star_x and star_x <= x + l and y <= star_y and star_y <= y + l:
                cnt += 1
        answer = max(answer, cnt)

print(k - answer)
