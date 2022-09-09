strings =[]
while 1:
    s = input().upper()
    if s == '*':
        break
    strings.append(s)

def surprising(s):
    for d in range(0,len(s) - 2):
        temp = []
        for i in range(len(s) - d-1):
            gv= s[i] + s[i+d+1]
            try:
                temp.index(gv)
                print(s,"is NOT surprising.")
                return 
            except:
                temp.append(gv)
    return print(s,"is surprising.")

for s in strings:
    surprising(s)