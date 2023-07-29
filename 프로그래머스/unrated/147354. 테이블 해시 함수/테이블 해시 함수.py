def bitwise(data,i):
    count = 0
    for num in data:
        count += num % i 
    return count
        
    
def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=  lambda x : (x[col-1],-x[0]))
    for i in range(row_begin-1,row_end):
        count = bitwise(data[i],i+1)
        answer ^=count
    
    return answer