n= int(input())
strings = []
for _ in range(n):
    strings.append(input())
count = 0

for string in strings:
    c = 1 
    for i in range(len(string) - 1 ):
        if string[i] != string[ i + 1 ]:
            c += 1
    if c == len(set(string)):
        count +=1
print(count)