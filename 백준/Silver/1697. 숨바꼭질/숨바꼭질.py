n, k = map(int, input().split())

from collections import deque
from collections import defaultdict


def default_visit():
    return False
def default_time():
    return 0

time_dic = defaultdict(default_time, n=0)
visited =  defaultdict(default_visit, n=True)

queue = deque([n])

while queue:

    current_pos = queue.popleft()

    next_pos = [current_pos - 1, current_pos + 1, current_pos * 2]
    if current_pos == k:
        print(time_dic[current_pos])
        break

    for n in next_pos:
        if 0 <= n <= 100000 and visited[n] is False:
            queue.append(n)
            visited[n] = True
            time_dic[n] = time_dic[current_pos] + 1