def solution(arr):
    answer = 0
    
    # 두 수 최대 공약수 찾기
    def lcm(a,b) :
        tmp = 0
        while b != 0 :
            tmp = a
            a = b
            b = tmp % a
            
        return a
    
    if len(arr) <= 1 :
        return arr[0]
    cmp = arr[0] * arr[1] // lcm(arr[1], arr[0])
    for i in range(2, len(arr)) :
        cmp = cmp * arr[i] // lcm(max(cmp,arr[i]), min(cmp, arr[i]))
    
    
    return cmp