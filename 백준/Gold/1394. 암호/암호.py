string = input()
password = input()
mod = 900528
n = len(string)
n_powers = [1] * len(password)
char_indices = {char: idx for idx, char in enumerate(string)}

# Precompute the powers of n modulo mod
answer = 1
for i in range(1, len(password)):
    n_powers[i] = (n_powers[i-1] * n) % mod
for i in range(1, len(password)):
    answer += n_powers[i]

# Use precomputed powers and indices
for i in range(len(password)):
    char = password[i]
    power_index = len(password) - 1 - i
    idx = char_indices[char]
    answer += (n_powers[power_index] * idx) % mod

print(answer % mod)
