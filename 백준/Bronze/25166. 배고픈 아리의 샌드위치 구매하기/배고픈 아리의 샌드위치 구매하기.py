import sys

sand, koogie = map(int, input().split())
from itertools import combinations


def solve():
    coin = [1, 2, 4, 8, 16, 32, 64, 128, 256,512]
    koogie_coin = [coin[i] for i in range(len(coin)) if koogie & 1 << i]

    if sand >= 1024:
        for i in range(len(koogie_coin)):
            for c in combinations(koogie_coin, i + 1):
                if sum(c) + 1023 == sand:
                    print("Thanks")
                    sys.exit()


    else:
        for i in range(len(coin)):
            for c in combinations(coin, i + 1):
                if sum(c) == sand:
                    print("No thanks")
                    sys.exit()
    print("Impossible")
solve()