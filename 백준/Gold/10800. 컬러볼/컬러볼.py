import sys

# init()
n = int(input(''))
ball_list = []
for i in range(n):
    c, s = map(int, sys.stdin.readline().rstrip().split(' '))
    ball_list.append([i, s, c])

# size, color로 오름차순 정렬
ball_list.sort(key=lambda x:(x[1], x[2]))

color_list = [0] * 200001
player_list = [0] * n

sum_ = 0
i, j = 0, 0

# 누적 합
while i < n:

    a_ball = ball_list[i]
    b_ball = ball_list[j]

    # B >= A 일 때 종료
    while b_ball[1] < a_ball[1]:

        # 총 사이즈 누적
        sum_ += b_ball[1]
        # 컬러 별 사이즈 누적
        color_list[b_ball[2]] += b_ball[1]

        j += 1
        b_ball = ball_list[j]

    player_list[a_ball[0]] = sum_ - color_list[a_ball[2]]
    i += 1

result = []
for i in range(n):
    result.append(str(player_list[i]))
print('\n'.join(result))