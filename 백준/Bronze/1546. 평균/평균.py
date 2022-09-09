n = int(input())
values = [int(_) for _ in input().split() ]

m = max(values)
values = [v/m*100 for v in values]
print(sum(values)/ n)