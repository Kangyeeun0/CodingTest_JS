def solution(arr) :
    answer = 0
    def mdf(a,b) :
        while b != 0 :
            temp = b
            b = a%b
            a = temp
        return a
    
    for i in range(len(arr)-1) :
        if i == 0 :
            mid = arr[i]*arr[i+1] // mdf(arr[i], arr[i+1])
            answer=mid
        else :
            mid = answer*arr[i+1] // mdf(answer,arr[i+1])
            answer=mid
    
    return answer