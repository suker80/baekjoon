a,b = input().split()
try:
    a,b = int(a) , int(b)
    print(a-b)
except:
    print("NaN")