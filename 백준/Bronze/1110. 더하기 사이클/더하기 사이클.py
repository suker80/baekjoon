start_num =input()

if int(start_num) < 10:
    num = '0' + start_num
    cnt = 0
    new_num = str(int(num[0]) + int(num[1]))[-1]
    num = num[1] + new_num
    cnt +=1
    
else :
    num = start_num
    cnt = 0
    new_num = str(int(num[0]) + int(num[1]))[-1]
    num = num[1] + new_num
    cnt +=1

while int(start_num) is not int(num):
    new_num = str(int(num[0]) + int(num[1]))[-1]
    num = num[1] + new_num
    cnt +=1
print(cnt)