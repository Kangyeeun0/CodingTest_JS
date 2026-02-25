def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    arr=[A[i]*B[i] for i in range(len(A))]
    answer=sum(arr)
    
    

    return answer