import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 도로 좌표 저장
R = [(0, 0)]
for i in range(1, N + 1):
    x, y = map(int, input().split())
    R.append((x, y))

# 연결 정보 저장
T = []
for _ in range(M):
    u, v, c = map(int, input().split())

    # 연결 좌표 저장
    # 상위 지점과 하위 지점을 따로 저장
    # 상위 지점의 경우 +, 하위 지점의 경우 - (하위 지점을 벗어날 경우 통행량을 빼줘야함으로)
    if R[u][1] > R[v][1]:
        T.append((R[u][1], c))
        T.append((R[v][1] - 1, -c))
    else:
        T.append((R[v][1], c))
        T.append((R[u][1] - 1, -c))

# 저장된 좌표를 가장 위 지점부터 차례대로 내려가면서 도로 통행량 저장
T.sort(key=lambda x: -x[0])
ans, tmp = 0, 0
for i in range(M * 2):
    tmp += T[i][1]
    if tmp > ans:
        ans = tmp
print(ans)