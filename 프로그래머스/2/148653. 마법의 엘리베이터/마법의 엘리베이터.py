from collections import deque
def solution(storey):
    answer = 0
    storey = str(storey)
    q = deque([int(storey[x]) for x in range(len(storey)-1, -1, -1)])
    print(q)
    
    while q :
        r = q.popleft()
        if r >= 10 :
            if not q :
                q.append(r//10)
            else :
                q[0]+=1
            r = r % 10
            
        if r == 5:
            if q and q[0] >= 5:
                answer += 5
                q[0] += 1
            else:
                answer += 5
        elif r < 5 :
            answer+=r
        else :
            answer += (10-r)
            if q :
                q[0]+=1
            else :
                q.append(1)
    # print(arr)
    

    
    return answer