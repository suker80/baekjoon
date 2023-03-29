def solution(scores):
    answer = 1

    target = scores[0]
    target_score = sum(scores[0])
    scores.sort(key=lambda x: (-x[0], x[1]))

    temp = 0
    for score in scores:
        if target[0] < score[0] and target[1] < score[1]:
            return -1
        if temp <= score[1]:
            if target_score < score[0] + score[1]:
                answer += 1
            temp = score[1]
    return answer