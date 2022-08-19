from collections import deque
from copy import deepcopy

n, m, d = map(int, input().split())
from itertools import combinations

orig_graph = [list(map(int, input().split())) for _ in range(n)]

orig_enemies = deque()

for i in range(n):
    for j in range(m):
        if orig_graph[i][j] == 1:
            orig_enemies.append([i, j])
answer = 0


def check(enemy):
    y, x = enemy

    return 0 <= y < n and 0 <= x < m and graph[y][x] == 1


def find_enemy(archer):
    for dist in range(d):
        for r in range(dist):
            enemy_pos = [n - (r + 1), archer - (dist - r)]
            if check(enemy_pos):
                return enemy_pos

        enemy_pos = [n - (dist + 1), archer]
        if check(enemy_pos):
            return enemy_pos

        for r in range(dist - 1, -1, -1):
            enemy_pos = [n - (r + 1), archer + (dist - r)]
            if check(enemy_pos):
                return enemy_pos


answer = 0
for archers in combinations(range(m), 3):
    graph = deepcopy(orig_graph)
    enemies = deepcopy(orig_enemies)
    cnt = 0
    while enemies:
        catch = set()
        catch_enemies = []
        for archer in archers:
            catch_enemy = find_enemy(archer)
            if catch_enemy:
                catch_enemies.append(catch_enemy)
        for catch_enemy in catch_enemies:
            y, x = catch_enemy
            graph[y][x] = 0
            catch.add((y * m + x))
        temp_enemy = []
        for enemy in enemies:
            y, x = enemy
            graph[y][x] = 0
            if enemy not in catch_enemies and y + 1 < n:
                temp_enemy.append([y + 1, enemy[1]])
        for enemy in temp_enemy:
            y, x = enemy
            graph[y][x] = 1
        enemies = temp_enemy
        cnt += len(catch)
    answer = max(answer, cnt)
print(answer)
