n = int(input())
boxes = list(map(int,input().split()))

dp = [boxes[0]]

def lowerBound(lst, key):
    start ,end = 0,len(lst) -1
    while start < end:
        mid = (start + end) // 2
        if lst[mid] == key:
            end = mid
        elif key < lst[mid]:
            end = mid
        elif lst[mid] < key:
            start = mid + 1
    return end


for i in range(1,n):
    if dp[-1]<boxes[i]:
        dp.append(boxes[i])
    elif dp[-1] > boxes[i]:
        idx = lowerBound(dp,boxes[i])
        dp[idx] = boxes[i]
    



print(len(dp))