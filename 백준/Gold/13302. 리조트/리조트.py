n, m = map(int, input().split())
can_go = [True] * (n + 1)
if m:
    cant_go = list(map(int, input().split()))
    for days in cant_go:
        can_go[days] = False

dp = [[float('inf')] * 101 for _ in range(101)]


def solve(day, coupon):
    if day > n:
        return 0
    if not can_go[day]:
        dp[day][coupon] = solve(day + 1, coupon)

    m1 = solve(day + 5, coupon + 2) + 37000
    m2 = solve(day + 3, coupon + 1) + 25000
    m3 = solve(day + 1, coupon) + 10000
    dp[day][coupon] = min(m1,
                          m2,
                          m3,
                          dp[day][coupon])

    if coupon >= 3:
        dp[day][coupon] = min(dp[day][coupon], solve(day + 1, coupon - 3))
    return dp[day][coupon]


print(solve(1, 0))
