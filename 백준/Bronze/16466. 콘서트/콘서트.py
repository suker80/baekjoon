n = int(input())
arr = list(map(int,input().split()))

arr.sort()

answer =1 
index = 0

while index< n and arr[index] == answer :
    index +=1 
    answer += 1 
print(answer)