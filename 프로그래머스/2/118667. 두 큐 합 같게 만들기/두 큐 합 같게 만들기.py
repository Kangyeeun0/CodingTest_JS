from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_1 = sum(q1)
    sum_2 = sum(q2)
    total = (sum_1 + sum_2) / 2
    i=0
    k = 4 * len(q1)
    while i < k :
        if sum_1 == sum_2 :
            return i
        elif sum_1 > sum_2 :
            q= q1.popleft()
            q2.append(q)
            sum_1 -= q
            sum_2 += q
        elif sum_1 < sum_2 :
            q = q2.popleft()
            q1.append(q)
            sum_1+=q
            sum_2 -=q
        i+=1

    

    
    
    return -1