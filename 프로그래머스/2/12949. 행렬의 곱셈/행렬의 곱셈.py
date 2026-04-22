def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)) :
        arr = []
        for j in range(len(arr2[0])) :
            summ = 0
            for k in range(len(arr2)) :
                summ+=arr1[i][k] * arr2[k][j]
            arr.append(summ)
        answer.append(arr)
        
    return answer