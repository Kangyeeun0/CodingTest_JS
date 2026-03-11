def solution(n):
    answer = ''
    arr =[]
    
    while n > 3 :
        r = n%3
        if r == 0 :
            n = n//3 - 1
            arr.append(4)
        else :
            arr.append(r)
            n=n//3
    if n ==3 :
        arr.append(4)
    else :
        arr.append(n)    
    arr=arr[::-1]
    return "".join(map(str,arr))