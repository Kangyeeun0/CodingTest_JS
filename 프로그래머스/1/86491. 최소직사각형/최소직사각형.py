def solution(sizes):
    answer = 0
    col = []
    row = []
    
    for i in range(len(sizes)) :
        sizes[i].sort(reverse=False)
        col.append(sizes[i][0])
        row.append(sizes[i][1])
    
    answer = max(col) * max(row)
    
    return answer