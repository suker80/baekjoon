def solution(numbers):
    
    number_set = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            number_set.add(numbers[i] + numbers[j])
    answer= sorted(list(number_set))
    return answer