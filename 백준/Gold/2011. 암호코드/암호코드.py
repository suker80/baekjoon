num = input()
arr = list(map(int, num))
mod = 1000000
int_num = int(num)
dp = [0] * len(arr)
if 1 <= int_num <= 9:
    print(1)
    exit(0)
if (len(arr) == 1 and arr[0] == 0) or (len(arr) == 2 and int_num > 20 and int_num % 10 == 0) or arr[0] == 0:
    print(0)
    exit(0)
if len(arr) >= 2 and (arr[0] == 1 or arr[0] == 2):
    dp[1] = 1
    dp[0] = 1
    if arr[0] == 2 and 1 <= arr[1] <= 6:
        dp[1] += 1
    elif arr[0] == 1 and arr[1] != 0:
        dp[1] += 1
else:
    dp[0] = 1
    dp[1] = 1
if arr[1] == 0 and not (arr[1 - 1] == 1 or arr[1 - 1] == 2):
    print(0)
    exit(0) 
for i in range(2, len(arr)):
    if arr[i] == 0 and not (arr[i - 1] == 1 or arr[i - 1] == 2):
        print(0)
        exit(0)
    if arr[i - 1] == 1:
        dp[i] += dp[i - 2]
    elif arr[i - 1] == 2 and 0 <= arr[i] <= 6:
        dp[i] += dp[i - 2]

    if arr[i]:
        dp[i] += dp[i - 1]
    dp[i] %= mod

print(dp[-1])
