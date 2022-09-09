n = int(input())
scores = [] 
for i in range(n):
    score = list(map(int,input().split()))
    scores.append(score)

for score in scores:
    l = score[0]
    avg = sum(score[1:]) / l
    count = sum(list(map(lambda x: x>avg , score[1:])))
    per =count/l * 100
    print('%.3f'%per + '%')
    