
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

next = [0] * 100_0001
prev = [0] * 100_0001

for i in range(n - 1):
    next[arr[i]] = arr[i + 1]
    prev[arr[i + 1]] = arr[i]
next[arr[n - 1]] = arr[0]
prev[arr[0]] = arr[n - 1]
answer = []
for _ in range(m):
    command = input().split(' ')

    if command[0] == 'BN':
        i, j = map(int, command[1:])
        answer.append(next[i])
        between_station = next[i]
        next[i] = j
        next[j] = between_station
        prev[between_station] = j
        prev[j] = i
    elif command[0] == 'BP':
        i, j = map(int, command[1:])
        answer.append(prev[i])
        between_station = prev[i]
        next[j] = i
        next[between_station] = j
        prev[i] = j
        prev[j] = between_station
    elif command[0] == 'CN':
        i = int(command[1])
        answer.append(next[i])
        between_station = next[i]
        between_next = next[between_station]
        next[i] = between_next
        prev[between_next] = i
    elif command[0] == 'CP':
        i = int(command[1])
        answer.append(prev[i])
        between_station = prev[i]
        between_prev = prev[between_station]
        prev[i] = between_prev
        next[between_prev] = i
print('\n'.join(map(str, answer)))
