import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int,input().split()) # 노드 수, 간선 수
parent = [0] * (N+1) # 부모 노드 저장할 공간
rank = [0] * (N+1) # 집합의 rank 저장할 공간
edges = [[] for i in range(M+1)] # 간선 정보 저장할 공간

for i in range(1, N+1):
    parent[i] = i # 부모 노드 자기 자신으로 설정

for i in range(1,M+1):
    a, b, c = map(int,input().split()) # 간선 정보 입력받기
    edges[i].extend([c, a, b]) # 비용, 시작 노드, 끝 노드

# union find algorithm
def find(a):
    if parent[a] == a: # 자기 자신이 부모 노드인 경우
        return a
    p = find(parent[a]) # 부모 노드 탐색
    parent[a] = p # 부모 노드 갱신
    return parent[a]

def union(a, b): # 두 분리 집합 병합
    a = parent[a] # 부모 노드 얻기
    b = parent[b] # 부모 노드 얻기
    if a == b: # 동일한 집합에 속함
        return
    if rank[a] > rank[b]: # 작은 집합을 큰 집합에 병합
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] += 1

# kruskal algorithm
def kruskal(edges):
    edges.sort() # 가중치 순으로 정렬
    cost = 0 # 비용
    MST = [] # 최소 신장 트리
    for edge in edges:
        if not edge: # 0 번 인덱스 edge 생략
            continue
        c, a, b = edge
        if find(a) != find(b): # 분리 집합이면 병합
            union(a, b)
            cost += c
            MST.append([a, b])
            if len(MST) == N-2: # 그래프를 두 개의 집합으로 분리하기 위해 중지 조건
                return cost
    return cost

print(kruskal(edges))