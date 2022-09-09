n = int(input())
from collections import defaultdict

arr = [input() for _ in range(n)]

alpha_dic = defaultdict(int)
non_zero = set()
word_set = set()

for word in arr:

    word_len = len(word)

    for idx, alpha in enumerate(word):
        word_set.add(alpha)
        if not idx:
            non_zero.add(alpha)
        alpha_dic[alpha] += 10 ** (word_len - idx - 1)

alpha_weight = {}

answer = 0
use = {}
sorted_dic = sorted(alpha_dic.items(), key=lambda item: item[1])
count = 9
for key, value in sorted_dic:
    if key not in non_zero and len(word_set) == 10 :
        use[key] = 0
        break
    else:
        continue
sorted_dic = sorted(sorted_dic, key=lambda item: item[1], reverse=True)

for key, value in sorted_dic:
    if use.get(key) is None:
        answer += value * count
        count -= 1
    else:
        continue

print(answer)
