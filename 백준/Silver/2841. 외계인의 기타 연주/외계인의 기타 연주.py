n, max_p = map(int,input().split())
line_stack = [[] for i in range(7)]
finger_count = 0

for _ in range(n):
    nth_line, p = map(int, input().split())

    while line_stack[nth_line] and line_stack[nth_line][-1] > p:
        line_stack[nth_line].pop()
        finger_count +=1
    if p not in line_stack[nth_line]:
        line_stack[nth_line].append(p)
        finger_count += 1
print(finger_count)
