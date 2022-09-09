n, m = map(int, input().split())

start = list(map(int, input().split()))
monster = list(map(int, input().split()))

if start[1] == 0:

    if monster[0] == 0 and monster[1] > start[0]:
        print("YES!")
    elif monster[0] == n and monster[0] % 2:
        print("YES!")
    else:
        print("NO...")

else:
    if monster[0] == 0 and monster[1] < start[0]:
        print("YES!")
    elif monster[0] == n and monster[0] % 2 == 0:
        print("YES!")
    else:print("NO...")
