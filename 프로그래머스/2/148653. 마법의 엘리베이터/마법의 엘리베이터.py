def solution(storey):
    arr = []
    total =0
    i=0
    
    while storey > 0 :
        a = storey%10
        arr.append(a)
        storey //=10
    
    while i < len(arr):
        if arr[i] > 5 or (arr[i] == 5 and i+1 < len(arr) and arr[i+1] >= 5):
            total +=(10-arr[i])
            if i <len(arr)-1 :
                arr[i+1]+=1
            else :
                arr.append(1)
        else :
            total +=arr[i]
        i+=1
        print(arr)
    return total
        
            
    
    return total