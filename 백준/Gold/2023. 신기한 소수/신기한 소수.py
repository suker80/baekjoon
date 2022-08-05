def solution(N):
    answer = list()
    stack = list()
    stack.append(2)
    stack.append(3)
    stack.append(5)
    stack.append(7)
    while stack:
        num = stack.pop()
        if 10**(N-1)<=num<10**N:
            answer.append(num)
            continue
        for i in range(10):
            newnum = num*10+i
            check=True
            for j in range(2,newnum//2):
                if newnum%j ==0:
                    check=False
                    break
            if check==True:
                stack.append(newnum)
    return sorted(answer)


   
    return answer
def main():
    N=int(input())
    answer = solution(N)
    for i in answer:
        print(i)

main()