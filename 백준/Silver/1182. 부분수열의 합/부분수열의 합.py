import bisect
n,s = map(int,input().split())
from collections import defaultdict

arr = list(map(int,input().split()))

left_part = defaultdict(int)
right_part = defaultdict(int)

mid = len(arr)//2

left_arr = arr[:mid]
right_arr = arr[mid:]
answer = 0
def part_sum(i,arr,temp_sum,dic,mode):

    if  i and mode:
        dic[temp_sum] += 1
    if i >= len(arr) :
        return
    part_sum(i+1,arr,temp_sum + arr[i],dic,1)
    part_sum(i + 1, arr, temp_sum ,dic,0)

part_sum(0,left_arr,0,left_part,1)
part_sum(0,right_arr,0,right_part,0)

for l in left_part:
    if right_part[s-l]:
        answer += left_part[l] *right_part[s-l]
answer += left_part[s]
answer += right_part[s]



print(answer)