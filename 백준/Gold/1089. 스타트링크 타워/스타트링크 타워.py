n = int(input())

nums = [input() for _ in range(5)]

num_string = [
    "####.##.##.####",
    "..#..#..#..#..#",
    "###..#####..###",
    "###..####..####",
    "#.##.####..#..#",
    "####..###..####",
    "####..####.####",
    "###..#..#..#..#",
    "####.#####.####",
    "####.####..####"
]
permutation_list = []
for i in range(n):
    temp = ''
    for j in range(5):
        temp += nums[j][i * 4: i * 4 + 3]

    temp_lst = []
    for j in range(10):
        for k in range(15):
            if temp[k] == '#' and temp[k] != num_string[j][k]:
                break
        else:
            temp_lst.append(j)
    permutation_list.append(temp_lst)

num_lst = []

num_sum = 0
lst = [0] * n
total_possible = 1
for i in range(n):
    num_possible = 1
    for j in range(n):
        if i != j:
            num_possible *= len(permutation_list[j])
    for j in permutation_list[i]:
        num_sum += num_possible * j * (10 ** (n - i - 1))

for i in range(n):
    total_possible *= len(permutation_list[i])

if total_possible:
    print('{0:5f}'.format(num_sum / total_possible))
else:
    print(-1)
