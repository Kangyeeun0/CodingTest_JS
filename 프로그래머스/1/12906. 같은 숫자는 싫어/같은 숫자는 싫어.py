def solution(arr):
    answer = []
    answer.append(arr[0])
    k=0
    for i in range(1, len(arr)) :
        if answer[k] != arr[i] :
            answer.append(arr[i])
            k+=1
        
    return answer