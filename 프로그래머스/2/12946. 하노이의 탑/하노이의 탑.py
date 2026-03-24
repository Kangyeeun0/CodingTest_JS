def solution(n):
    answer = []
    
    def hanoi(n, start, end, mid) :
        if n == 1 :
            answer.append([start, end])
            return
        else :
            #1. n-1개를 1->2로 이동
            hanoi(n-1, start, mid, end)
            
            #2. 가장 큰 원판을 1->3로 이동
            answer.append([start, end])
            
            #3. n-1개를 2->3로 이동
            hanoi(n-1, mid, end, start)
            
    hanoi(n, 1, 3, 2)
    return answer