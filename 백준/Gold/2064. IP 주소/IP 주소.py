n = int(input())
ip_list = [list(map(int, input().split('.'))) for _ in range(n)]

for i in range(len(ip_list)):
    a, b, c, d = ip_list[i]
    ip_list[i] = ('00000000' + bin(a)[2:])[-8:] + ('00000000' + bin(b)[2:])[-8:] + ('00000000' + bin(c)[2:])[-8:] + (
                                                                                                                                '00000000' + bin(
                                                                                                                            d)[
                                                                                                                                             2:])[
                                                                                                                    -8:]

mask = ''
for i in range(32):
    bit = ip_list[0][i]
    for j in range(n):
        if bit != ip_list[j][i]:
            mask += '0'
            break
    else:
        mask += '1'
        continue
    mask += '0' * 32
    mask = mask[:32]
    break
mask_arr = []
for i in range(4):
    mask_arr.append(int('0b' + mask[i * 8:(i + 1) * 8], 2))

answer = ''
for i in range(32):
    if mask[i] == '1':
        answer += ip_list[0][i]
    else:
        answer += '0'

answer_arr = []
for i in range(4):
    answer_arr.append(int('0b' + answer[i * 8:(i + 1) * 8], 2))
print('.'.join(map(str, answer_arr)))
print('.'.join(map(str, mask_arr)))
