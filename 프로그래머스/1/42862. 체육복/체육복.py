def solution(n, lost, reserve):
    same = set(lost) & set(reserve)

    lost = sorted(set(lost) - same)
    reserve = sorted(set(reserve) - same)

    answer = n - len(lost)

    for student in lost:
        if student - 1 in reserve:
            reserve.remove(student - 1)
            answer += 1

        elif student + 1 in reserve:
            reserve.remove(student + 1)
            answer += 1

    return answer