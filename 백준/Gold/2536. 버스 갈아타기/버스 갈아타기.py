from collections import deque

n, m = map(int, input().split())

k = int(input())

visit = [False] * (k + 1)
horizon_bus = []
vertical_bus = []
bus = [[0]]
isHorizon = [False] * (k + 1)
for _ in range(k):
    b, x1, y1, x2, y2 = list(map(int, input().split()))
    if x1 > x2:
        x2, x1 = x1, x2
    if y1 > y2:
        y2, y1 = y1, y2

    if x1 - x2:
        vertical_bus.append([b, y1, x1, x2])
    else:
        horizon_bus.append([b, x1, y1, y2])
        isHorizon[b] = True
    bus.append([b, x1, y1, x2, y2])
bus.sort(key=lambda x: x[0])
dest = list(map(int, input().split()))
start = dest[:2]
end = dest[2:]

queue = deque()
answer = 0
for index, y, x1, x2 in vertical_bus:
    if start[1] == y and (x1 <= start[0] <= x2):
        queue.append([1, index, start[0], start[1]])
        visit[index] = True
for index, x, y1, y2 in horizon_bus:
    if start[0] == x and (y1 <= start[1] <= y2):
        queue.append([1, index, start[0], start[1]])
        visit[index] = True


def solve():
    while queue:
        count, thisBus, thisX, thisY = queue.popleft()
        thisBusData = bus[thisBus]
        if isHorizon[thisBus]:
            if thisX == end[0] and thisBusData[2] <= end[1] <= thisBusData[4]:
                return count
        else:
            if thisY == end[1] and thisBusData[1] <= end[0] <= thisBusData[3]:
                return count

        for nextBus, nextY, nextX1, nextX2 in vertical_bus:
            if visit[nextBus]:
                continue
            if isHorizon[thisBus]:
                if (nextX1 <= thisX <= nextX2) and (thisBusData[2] <= nextY <= thisBusData[4]):
                    queue.append([count + 1, nextBus, thisX, nextY])
                    visit[nextBus] = True
            else:
                if thisY == nextY and ((thisBusData[3] <= nextX1) != (thisBusData[1] <= nextX2)):
                    queue.append([count + 1, nextBus, nextX1, thisY])
                    visit[nextBus] = True

        for nextBus, nextX, nextY1, nextY2 in horizon_bus:
            if visit[nextBus]:
                continue
            if not isHorizon[thisBus]:
                if (nextY1 <= thisY <= nextY2) and (thisBusData[1] <= nextX <= thisBusData[3]):
                    queue.append([count + 1, nextBus, nextX, thisY])
                    visit[nextBus] = True

            else:
                if thisX == nextX and ((thisBusData[4] <= nextY1) != (thisBusData[2] <= nextY2)):
                    queue.append([count + 1, nextBus, thisX, nextY1])
                    visit[nextBus] = True


print(solve())
