n = int(input())
mod = 1_000_000_007
String = input()

wh_comb = [0, 0, 0]  ## has E  0, 1 2 more than
w_count = 0
for char in String:

    if char == 'W':
        w_count += 1
    elif char == 'H':
        wh_comb[0] += w_count
    elif char == 'E':
        wh_comb[2] += (wh_comb[2] + wh_comb[1])
        wh_comb[2] %= mod
        wh_comb[1] += wh_comb[0] % mod
        wh_comb[1] %= mod

print(wh_comb[-1])
