t= int(input())
from math import sqrt
for i in range(t):
    x_1,y_1,r_1, x_2,y_2,r_2 = map(int,input().split())
    
    dist = sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    
    if x_1 == x_2 and y_1 == y_2 and r_1 == r_2:
        print(-1)
    elif x_1 == x_2 and y_1 == y_2 and r_1 != r_2:
        print(0)
    elif r_1 + r_2 == dist or r_1 == r_2 + dist or r_2 == r_1 + dist:
        print(1)
    elif r_1 + r_2 < dist or r_1 > r_2+ dist or r_2> r_1 + dist:
        print(0)
    elif r_1 + r_2 > dist:
        print(2)
