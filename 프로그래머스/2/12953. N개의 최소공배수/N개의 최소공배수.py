def solution(arr):
    answer = 0
    n = len(arr)
    
    def gcd(a,b) :
        if a>=b :
            big = a
            small = b
        else :
            big = b
            small = a
        while small != 0 :
            tmp = big
            big = small
            small = tmp % small        
        return big

    mcdValue = 0
    
    for i in range(n-1) :
        if mcdValue == 0 :
            gcdValue = gcd(arr[i+1],arr[i])
            mcdValue = arr[i+1] * arr[i] // gcdValue
        else :
            gcdValue = gcd(mcdValue, arr[i+1])
            mcdValue = arr[i+1] * mcdValue // gcdValue
    
    answer = mcdValue
        
    
    return answer