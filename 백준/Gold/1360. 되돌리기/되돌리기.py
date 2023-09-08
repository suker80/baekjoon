n = int(input())
log = [[0, '', '']]
for i in range(n):
    command = input().split()


    if command[0] == 'type':
        c, t = command[1], int(command[2])
        last_t, prev_string, cur_string = log[-1]
        log.append([t, cur_string, cur_string + c])
    else:
        cur_string = log[-1][2]
        c, t = int(command[1]), int(command[2])
        for last_t, prev_string, _ in log:
            if last_t >= t - c:
                log.append([t, cur_string, prev_string])
                break
print(log[-1][2])
