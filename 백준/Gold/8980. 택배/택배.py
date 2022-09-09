n,c = map(int,input().split())

m = int(input())

data = [[] for _ in range(n+1)]
for _ in range(m):

    a,b,box = map(int,input().split())
    data[a].append([b,box])

for i in range(1,n+1):
    data[i].sort(key = lambda x: (x[0],-x[1]))
truck = 0
current = 0
lift = [0] * (n+1)
total = 0
    # can_lift = data[truck]
    # current -= lift[]
    # global current
    # for dest , baggage  in can_lift:
    #
    #     if current + baggage <= c:
    #         current += baggage
    #         lift[dest] += baggage
    #     else:
    #         baggage = c - current
    #         current += baggage
    #         lift[dest] += baggage
    #         return

for i in range(1,n+1):
    truck = i
    can_lift = data[truck]
    current -= lift[i]
    total += lift[i]
    for dest , baggage  in can_lift:

        if current + baggage <= c:
            current += baggage
            lift[dest] += baggage
        else:
            baggage = c - current
            current += baggage
            lift[dest] += baggage
            break
print(total)