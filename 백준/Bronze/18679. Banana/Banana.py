n = int(input())

dic = {}
for i in range(n):
    a,b = input().split(' = ')


    dic[a] = b

t = int(input())

for _ in range(t):
    k = int(input())

    string = input().split()

    answer = ''

    for i in range(k):
        answer += dic[string[i]]
        answer +=' '
    print(answer)
