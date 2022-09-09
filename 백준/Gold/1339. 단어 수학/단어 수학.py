n = int(input())

words = [list(map(str, input())) for _ in range(n)]

nums = list(range(10))
from collections import defaultdict
word_dic = defaultdict(int)

for word in words:
    for i,char in enumerate(word[::-1]):
        word_dic[char] += 10 ** i

word_num = {}
answer = 0
for key,value in sorted(word_dic.items(),key=lambda x:x[1],reverse=True):

    answer += value* nums.pop()
#
# def convert(word):
#     s = ''
#
#     for char in word:
#         s += word_num[char]
#     return int(s)
# answer = 0
# for word in words:
#     answer += convert(word)
# print(answer)
print(answer)