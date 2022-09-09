n = int(input())

p = [tuple(map(int,input().split())) for i in range(n) ]

result = []

for i in range(n):
    count = 1
    for j in range(n):
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            count +=1
    result.append(count)

print(*result, sep='\n')