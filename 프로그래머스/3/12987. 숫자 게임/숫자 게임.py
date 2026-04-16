def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    leng = len(A)
    a_idx = 0
    b_idx = 0
    
    while a_idx < leng and b_idx < leng  :
        if A[a_idx] < B[b_idx] :
            answer+=1
            a_idx +=1
            b_idx +=1
        else :
            b_idx += 1
    
    
    return answer