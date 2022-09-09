import sys
read = sys.stdin.readline

N = int(read())
D = [[1,1,1] for _ in range(N+1)]


for i in range(2, N+1):
    D[i][0] = (D[i-1][1]+ D[i-1][2]) % 9901
    D[i][1] = (D[i-1][0]+ D[i-1][2]) % 9901
    D[i][2] = (D[i-1][0]+ D[i-1][1]+ D[i-1][2]) % 9901
    
print(sum(D[N]) % 9901 )