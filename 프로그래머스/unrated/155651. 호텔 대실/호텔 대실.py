from typing import List, Union, Tuple


def solution(book_time: List[Tuple[str, str]]) -> None:
    answer = 0
    minute = [0] * 1500
    for start_time, end_time in book_time:
        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))

        start_total_minutes = start_hour * 60 + start_minute
        end_total_minutes = end_hour * 60 + end_minute
        minute[start_total_minutes] += 1
        minute[end_total_minutes + 10] -= 1

    for i in range(1, len(minute)):
        minute[i] += minute[i-1]
    
    return max(minute)
