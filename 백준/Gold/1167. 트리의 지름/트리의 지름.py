import sys
 
V=int(sys.stdin.readline())
 
matrix=[[] for _ in range(V+1)]
#입력받는 부분
for _ in range(V):
    path=list(map(int,sys.stdin.readline().split()))
    #1+2i
    path_len=len(path)
    for i in range(1,path_len//2):
        matrix[path[0]].append([path[2*i-1],path[2*i]])
 
 
#첫번째 DFS결과
result1=[0 for _ in range(V+1)]
 
def DFS(start,matrix,result):
    for e,d in matrix[start]:
        if result[e]==0:
            result[e]=result[start]+d
            DFS(e,matrix,result)
 
DFS(1,matrix,result1)#아무노드에서 시작해준다.
result1[1]=0#루트노드가 정해져 있지않아 양방향으로 입력을 받기때문에 해당
 
 
tmpmax=0#최대값 구하기
index=0#최장경로 노드
 
for i in range(len(result1)):
    if tmpmax<result1[i]:
        tmpmax=result1[i]
        index=i
 
#최장경로 노드에서 다시 DFS를 통해 트리지름구하기
result2=[0 for _ in range(V+1)]
DFS(index,matrix,result2)
result2[index]=0
print(max(result2))
 
