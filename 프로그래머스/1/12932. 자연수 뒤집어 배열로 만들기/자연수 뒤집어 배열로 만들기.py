def solution(n):
    arr=list(str(n))
    answer=[]
    
    for i in range(len(arr)) :
       answer.append(int(arr[len(arr)-i-1]))
    
    
    return answer