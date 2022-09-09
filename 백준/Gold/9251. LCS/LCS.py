a = input()
b = input()

len_a = len(a)
len_b = len(b)

table = [[0] * (len_b+1) for _ in range(len_a+1)]
for i in range(1,len_a+1):
    for j in range(1,len_b+1):

        if a[i-1] == b[j-1]:
            table[i][j] = table[i-1][j-1]+1
        else:
            table[i][j] = max(table[i-1][j] , table[i][j-1])

print(table[-1][-1])
