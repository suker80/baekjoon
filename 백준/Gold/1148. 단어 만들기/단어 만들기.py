import sys
from collections import Counter, defaultdict

input = sys.stdin.readline

words = []
while True:

    s = input().strip()
    if s == '-':
        break

    words.append(Counter(s))

while True:
    s = input().strip()
    if s == '#':
        break
    puzzle_counter= Counter(s)
    has_answer = False
    answer_dict = defaultdict(int)
    for key in puzzle_counter.keys():
        answer_dict[key] = 0
    for word in words:
        # print(word)
        for key,value in word.items():
            if puzzle_counter[key] < value:
                break
        else:
            has_answer = True
            for key in word.keys():
                answer_dict[key] += 1


    min_val = min(answer_dict.values())
    max_val = max(answer_dict.values())
    min_str = ""
    max_str = ""
    for key, value in sorted(answer_dict.items()):
        if value == min_val:
            min_str += key

        if value == max_val:
            max_str += key

    print(min_str,min_val,max_str,max_val)

