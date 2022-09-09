# n = int(input())
# from collections import defaultdict
#
# graph = [list(map(int, input().split())) for _ in range(n)]
#
# dp = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
#
#
# lu_dic = []
# rd_dic = []
# ld_dic = []
# ru_dic = []
#
# for i in range(n + 1):
#     lu_temp = []
#     ld_temp = []
#     ru_temp = []
#     rd_temp = []
#
#     for j in range(n + 1):
#         lu_temp.append(defaultdict(int))
#         ld_temp.append(defaultdict(int))
#         ru_temp.append(defaultdict(int))
#         rd_temp.append(defaultdict(int))
#
#     lu_dic.append(lu_temp)
#     ld_dic.append(ld_temp)
#     ru_dic.append(ru_temp)
#     rd_dic.append(rd_temp)
#
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         for l in range(i, n + 1):
#             for k in range(j, n + 1):
#                 dp[i][j][l][k] = dp[i][j][l - 1][k] + dp[i][j][l][k - 1] - dp[i][j][l - 1][k - 1] + graph[l - 1][k - 1]
#                 lu_dic[l][k][dp[i][j][l][k]] += 1
# del dp
# rd = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
#
# for i in range(n - 1, -1, -1):
#     for j in range(n - 1, -1, -1):
#         for l in range(i, -1, -1):
#             for k in range(j, -1, -1):
#                 rd[i][j][l][k] = rd[i][j][l + 1][k] + rd[i][j][l][k + 1] - rd[i][j][l + 1][k + 1] + graph[l][k]
#                 rd_dic[l][k][rd[i][j][l][k]] += 1
# del rd
# ru = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(n - 1, -1, -1):
#         for l in range(i, n + 1):
#             for k in range(j, -1, -1):
#                 ru[i][j][l][k] = ru[i][j][l-1][k] + ru[i][j][l][k+1] - ru[i][j][l-1][k+1] + graph[l-1][k]
#                 ru_dic[l][k][ru[i][j][l][k]] += 1
# del ru
# ld = [[[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
#
# for i in range(n-1,-1,-1):
#     for j in range(1,n+1):
#         for l in range(i,-1,-1):
#             for k in range(j,n+1):
#                 ld[i][j][l][k] = ld[i][j][l+1][k] + ld[i][j][l][k-1] - ld[i][j][l+1][k-1] + graph[l][k-1]
#                 ld_dic[l][k][ld[i][j][l][k]] += 1
# del ld
#
# answer = 0
# for i in range(1,n):
#     for j in range(1,n):
#
#         for key, value in lu_dic[i][j].items():
#             answer += rd_dic[i][j][key] * value
#
#         for key,value in ru_dic[i][j].items():
#             answer += ld_dic[i][j][key] * value
#
# print(answer)
#
#
#


n = int(input())
from collections import defaultdict

graph = [list(map(int, input().split())) for _ in range(n)]


def leftUp(y, x):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    dic = defaultdict(int)


    for i in range(y,0,-1):
        for j in range(x,0,-1):
            
            dp[i][j] = dp[i][j+1] + dp[i+1][j] - dp[i+1][j+1] + graph[i-1][j-1]
            
            dic[dp[i][j]] += 1
    return dic

def rightDown(y,x):
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    dic = defaultdict(int)


    for i in range(y+1,n+1):
        for j in range(x+1,n+1):

            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]
            dic[dp[i][j]] += 1
    return dic

def rightUp(y,x):

    dp = [[0] * (n+1) for _ in range(n+1)]

    dic = defaultdict(int)

    for i in range(y-1,-1,-1):
        for j in range(x,n):

            dp[i][j] = dp[i][j-1] + dp[i+1][j] -dp[i+1][j-1] + graph[i][j]

            dic[dp[i][j]] += 1
    return dic

def leftDown(y,x):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    dic = defaultdict(int)

    for i in range(y,n):
        for j in range(x-1,-1,-1):
            dp[i][j] = dp[i-1][j] + dp[i][j+1] - dp[i-1][j+1] + graph[i][j]
            dic[dp[i][j]] += 1
    return dic

answer = 0
for i in range(1,n):
    for j in range(1,n):
        lu_dic = leftUp(i,j)
        rd_dic = rightDown(i, j)
        ru_dic = rightUp(i,j)
        ld_dic = leftDown(i,j)
        for key,value in lu_dic.items():
            answer += rd_dic[key] * value

        for key,value in ru_dic.items():
            answer += ld_dic[key] * value
print(answer)

