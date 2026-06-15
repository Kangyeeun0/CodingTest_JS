def solution(array, commands):
    answer = []
    
    for c in commands :
        i, j, k = c
        cut_array = sorted(array[i-1:j])
        # print(cut_array)
        answer.append(cut_array[k-1])
        
    return answer