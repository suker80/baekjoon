n, k = map(int, input().split())

length = 1
while k:
    length_sum = (10 ** length - 10 ** (length - 1)) * length
    if length_sum < k:
        k -= length_sum
        length += 1
    elif length_sum == k:
        print(9)
        break
    else:
        digit = k // length

        if k % length == 0:
            answer = 10 ** (length - 1) + digit - 1
            if answer > n:
                print(-1)
            else:
                print(str(answer)[-1])
        else:
            answer = 10 ** (length - 1) + digit
            if answer > n:
                print(-1)
            else:
                print(str(answer)[k % length - 1])
        break
