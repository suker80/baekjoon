n,k= map(int,input().split())

point = [False] * 100001

from collections import deque

queue = deque([[n,[n]]])
point[n] = 1
if k< n:
    print(n-k )
    print(*list(range(n,k-1,-1)))

else:
    while queue:
        current,route = queue.popleft()
        n_pos = [current *2 ,current -1 , current +1]
        if current == k:
            print(point[k] - 1)
            print(*route)
            break

        for i in n_pos:
            if 0<=i<=100000 and point[i] == False:
                point[i] = point[current]+ 1
                queue.append([i,route+[i]])