answer = float('inf')


def solution(picks, minerals):
    n = len(minerals)

    def solve(current_idx, remain_picks, count):
        global answer
        if current_idx >= n or not sum(remain_picks):
            answer = min(answer, count)
        for i, v in enumerate(remain_picks):
            temp_count = count
            if not v:
                continue
            for j in range(5):
                next_idx = current_idx + j
                if next_idx < n:
                    if minerals[next_idx] == 'diamond':
                        temp_count += 5 ** i
                    elif minerals[next_idx] == 'iron':
                        temp_count += max(1, 5 ** (i - 1))
                    else:
                        temp_count += max(1, 5 ** (i - 2))
                else:
                    answer = min(answer, temp_count)
                    return
            else:
                temp_remain_picks = remain_picks[:]
                temp_remain_picks[i] -= 1
                solve(current_idx + 5, temp_remain_picks, temp_count)

    solve(0, picks, 0)
    return answer
