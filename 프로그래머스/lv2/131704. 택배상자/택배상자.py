def solution(order):
    stack = []
    idx = 0
    answer = 0
    
    for i in range(len(order)):
        if i +1 == order[answer]:
            answer +=1
        else:
            stack.append(i+1)
        while stack and order[answer] == stack[-1]:
            stack.pop()
            answer +=1
        
        
    return answer