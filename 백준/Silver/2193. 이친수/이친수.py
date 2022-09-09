n = int(input())

a = [0,1,1,2,3]

for i in range(len(a),n+1):
    a.append(a[i-2] + a[i-1])

print(a[n])