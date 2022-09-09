T = int(input())
from heapq import heappop,heappush
for _ in range(T):
    m =int(input())
    arr = []

    for i in range(m//10 + 1):
        a = list(map(int,input().split()))
        arr.extend(a)

    left = []
    right = []
    count = 1
    print(m//2 + 1 )
    for i in range(m):

        if i == 0:print(arr[i],end=' ');continue
        if i == 1:
            if arr[0] > arr[1] :
                heappush(right,arr[0])
                heappush(left,-arr[1])
                continue
            else:
                heappush(right,arr[1])
                heappush(left,-arr[0])
                continue

        x = arr[i]

        left_max = -heappop(left)
        right_min = heappop(right)

        if len(left) <= len(right):
            if x > right_min:
                heappush(left,-left_max)
                heappush(left,-right_min)
                heappush(right,x)
            else:
                heappush(left,-left_max)
                heappush(left,-x)
                heappush(right,right_min)
        else:
            if x > left_max:
                heappush(left,-left_max)
                heappush(right, x)
                heappush(right,right_min)
            else:
                heappush(left,-x)
                heappush(right,left_max)
                heappush(right,right_min)
        if i%2 == 0:
            print(-left[0],end=' ')
            count += 1
            if count % 10 == 0:
                print('')
    print('')



