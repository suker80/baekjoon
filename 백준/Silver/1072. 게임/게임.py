import math
import random

x,y = [int(_) for _ in input().split(' ')]

rate= math.floor( 100 * y/x )
new_rate = rate
cnt = 0
first = 0
last = x
interval = (first +last)/2
while True:
    if rate< 99:
        new_rate = math.floor( 100 * (y+interval)  / (x+ interval))

        if new_rate > rate:
            temp_rate =  math.floor(100 * (y+interval -1 )  / (x+ interval -1))
            if temp_rate == rate and temp_rate != new_rate :
                print(int(interval))
                break;
            last = interval 
            interval = (first + last ) // 2
#             print("right rate : {} new_rate {} temp_rate {} interval {}".format(rate,new_rate,temp_rate,interval))

        else:

            temp_rate =  math.floor(100 * (y+interval +1 )  / (x+ interval +1))
            if temp_rate != rate and temp_rate != new_rate :
                print(int(interval + 1))
                break;
            first = interval
            interval = (first + last) //2
            
#             print("left rate : {} new_rate {} temp_rate {} interval {}".format(rate,new_rate,temp_rate,interval))
    else:
        print(-1)
        break