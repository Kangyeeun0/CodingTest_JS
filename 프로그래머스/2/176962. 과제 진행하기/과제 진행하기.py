from collections import deque

def solution(plans):
    answer = []
    waiting_works = deque()

    # 시간 -> 분
    def change_time(t):
        h, m = map(int, t.split(":"))
        return h * 60 + m

    # 전처리
    for plan in plans:
        plan[1] = change_time(plan[1])
        plan[2] = int(plan[2])

    # 시작 시간순 정렬
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans) - 1):
        subject, start, play = plans[i]
        next_start = plans[i + 1][1]

        # 다음 과제 시작 전까지 남는 시간
        remain_time = next_start - start

        if play <= remain_time:
            answer.append(subject)
            remain_time -= play

            # 남는 시간 동안 대기 과제 수행
            while waiting_works and remain_time > 0:
                w_subject, w_play = waiting_works.pop()

                if w_play <= remain_time:
                    answer.append(w_subject)
                    remain_time -= w_play
                else:
                    waiting_works.append([w_subject, w_play - remain_time])
                    break

        else:
            # 끝내지 못하면 남은 시간 저장
            waiting_works.append([subject, play - remain_time])

    # 마지막 과제는 무조건 완료
    answer.append(plans[-1][0])

    # 대기 과제 역순(LIFO) 처리
    while waiting_works:
        answer.append(waiting_works.pop()[0])

    return answer