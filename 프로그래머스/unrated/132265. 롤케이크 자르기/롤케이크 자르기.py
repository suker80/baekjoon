def solution(topping):
    answer = 0
    visit_a = [0] * 10001
    visit_b = [0] * 10001
    count_a ,count_b = 0,0
    for t in topping:
        if not visit_b[t]:
            count_b += 1
        visit_b[t] +=1
        
    for t in topping:
        visit_b[t] -= 1
        if not visit_b[t]:
            count_b -=1 
        if not visit_a[t]:
            count_a +=1
        visit_a[t] += 1
        if count_a == count_b:
            answer +=1
    return answer