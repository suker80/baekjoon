m = int(input())
strings = []
for i in range(m):
    s= input()
    strings.append(s)
for string in strings:
    count = 0 
    current = 0
    for s in (string):
        

        if s.lower() == 'o':
            current +=1
        if s.lower() == 'x':
            current = 0
        count += current
    print(count)