n = int(input())
strings = []
for i in range(n):
    string = input()
    strings.append(string)
for string in strings:
    vps = 0
    for s in string:
        if s == '(' :
            vps +=1
        else :
            vps -=1 
        if vps<0:
            print('NO')
            break
    else:
        if vps == 0:
            print('YES')
        else:
            print('NO')