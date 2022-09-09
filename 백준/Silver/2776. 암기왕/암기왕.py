n = int(input())

for i in range(n):
    note_size1 = int(input())
    first_note = list(map(int,input().split()))

    note_size2 = int(input())
    second_note = list(map(int,input().split()))
    
    note = set(first_note)
    
    for num in second_note:
        
        if num in note:
            print(1)
        else:
            print(0)
    
    
    
    