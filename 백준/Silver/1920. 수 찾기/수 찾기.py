n = int(input())
nums = list(map(int,input().split()))

m = int(input())
search_nums = list(map(int,input().split()))

nums = sorted(nums)
def binary_search(arr,value):
    left,right = 0,len(arr) - 1
    while right>=left:
        mid = (left+ right) //2
        if value == arr[mid] :
            print(1)
            return
        elif arr[mid] < value:
            left = mid+1
        elif arr[mid]>value:
            right = mid - 1
    print(0)

for i in search_nums:
    binary_search(nums,i)