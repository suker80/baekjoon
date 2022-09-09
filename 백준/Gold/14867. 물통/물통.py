
import sys
cap_a ,cap_b,a_target,b_target = map(int,input().split())
visit = [[0] * (cap_a+1) for _ in range(cap_b+1)]
from collections import deque
queue = deque([[0,0,0]])

visit[0][0] = 1

answer= 0

cap = [cap_a,cap_b]
def fill(i):

    if i == 0 :
        return [cap_a,bottle[1]]
    else:
        return [bottle[0],cap_b]

def empty(i):
    if i == 0 :
        return [0,bottle[1]]
    else:
        return [bottle[0],0]

def move(i):
    f = i
    to = (i+1) % 2

    if f == 0 :
        can_fill = cap[to] - bottle[to]

        if bottle[f] <= can_fill:
            return [0,sum(bottle)]

        else:
            return [bottle[f]-can_fill,bottle[to]+can_fill]
    else:
        can_fill = cap[to] - bottle[to]

        if bottle[f] <= can_fill:
            return [sum(bottle),0]

        else:
            return [bottle[to]+can_fill,bottle[f]-can_fill]

func = [fill,move,empty]
while queue:
    a,b, count  = queue.popleft()
    bottle = [a,b]
    if bottle[0] == a_target and bottle[1] == b_target:
        print(count)
        sys.exit()
    for i in range(2):
        for f in func:
            next_a,next_b = f(i)

            if visit[next_b][next_a] == 0:
                queue.append([next_a,next_b,count+1])
                visit[next_b][next_a] = 1

print(-1)
