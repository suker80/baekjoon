n = int(input())
people = 0
office = []
for i in range(n):
    d, p = map(int, input().split())
    people += p
    office.append([d, p])

office.sort(key=lambda x: x[0])

temp = 0
for d, p in office:
    temp += p

    if temp > people // 2:
        print(d)
        break
