X = [int(_) for _ in input()]
count = 0
while(len(X)>1):
    X = [int(_) for _ in str(sum(X))]
    count += 1
print(count)
if sum(X)%3 == 0:
    print("YES")
else:
    print("NO")