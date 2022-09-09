from collections import deque

command = []


def check():
    global error
    if abs(stack[-1]) > 10 ** 9:
        error = True
        return False
    return True


while True:

    s = input().split()


    if s[0] == 'QUIT':
        break

    if s[0] == 'END':
        n = int(input())

        run = []
        for i in range(n):
            run.append(int(input()))
        for r in run:
            stack = [r]
            stack_len = 1
            error = False
            for c in command:
                if c[0] == 'NUM':
                    stack.append(int(c[1]))
                    stack_len += 1
                    continue
                if c[0] == 'DUP':
                    if not stack:
                        error = True
                    else:
                        stack.append(stack[-1])
                        stack_len += 1
                    continue

                if c[0] == 'INV':
                    if not stack:
                        error = True
                    else:
                        stack[-1] = -stack[-1]
                    continue

                if c[0] == 'POP':
                    if not stack:
                        error = True
                    else:
                        stack.pop()
                        stack_len -= 1
                    continue

                if c[0] == 'SWP':
                    if stack_len > 1:
                        stack[-1], stack[-2] = stack[-2], stack[-1]
                    else:
                        error = True
                    continue

                if c[0] == 'ADD':
                    if stack_len > 1:
                        first = stack.pop()
                        stack[-1] = stack[-1] + first
                        stack_len -= 1
                        check()

                    else:
                        error = True
                    continue

                if c[0] == 'SUB':
                    if stack_len > 1:
                        first = stack.pop()
                        stack_len -= 1
                        stack[-1] = stack[-1] - first
                        check()


                    else:
                        error = True
                    continue

                if c[0] == 'MUL':
                    if stack_len > 1:
                        first = stack.pop()
                        stack_len -= 1
                        stack[-1] = stack[-1] * first
                        check()

                    else:
                        error = True
                    continue
                if c[0] == 'DIV':
                    if stack_len > 1:
                        first = stack.pop()
                        stack_len -= 1
                        if not first:
                            error = True
                            continue
                        sign = 0
                        if first < 0:
                            sign += 1
                        if stack[-1] < 0:
                            sign += 1
                        if sign == 1:
                            stack[-1] = -(abs(stack[-1]) // abs(first))
                        else:
                            stack[-1] = abs(stack[-1]) // abs(first)
                        check()


                    else:
                        error = True
                    continue
                if c[0] == 'MOD':
                    if stack_len > 1:
                        first = stack.pop()
                        stack_len -= 1

                        if not first:
                            error = True
                            continue
                        if stack[-1] < 0:
                            stack[-1] = -(abs(stack[-1]) % abs(first))
                        else:
                            stack[-1] = abs(stack[-1]) % abs(first)
                        check()
                    else:
                        error = True

            if not error and stack_len == 1:
                print(stack[-1])
            else:
                print('ERROR')
        print()
        input()
        command =[]
    count = 1
    command.append(s)
