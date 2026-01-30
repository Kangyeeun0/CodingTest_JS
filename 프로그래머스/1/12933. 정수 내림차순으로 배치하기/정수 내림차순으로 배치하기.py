def solution(n):
    answer = 0
    
    arr=list(str(n))
    arr.sort(reverse=True)
    answer= ''.join(arr)
    return int(answer)