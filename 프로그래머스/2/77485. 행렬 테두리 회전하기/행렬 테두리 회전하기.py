def solution(rows, columns, queries):
    # 2차원 배열로 만들기
    answer = []
    k = 1
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(k)
            k += 1
        answer.append(row)
    
    result = []
    
    def turn_clock(x1, y1, x2, y2, query):
        xi = x1 
        yi = y1
        temp = query[x1][y1]  # 시작점 값 저장
        min_val = temp
        
        width = (x2-x1+1) * 2 + (y2-y1+1) * 2 - 4  # 테두리 칸 수
        
        for i in range(width):
            # 왼쪽 세로 (위→아래)
            if xi < x2 and yi == y1:
                next_val = query[xi+1][yi]
                query[xi][yi] = next_val
                min_val = min(min_val, next_val)
                xi += 1
            # 아래 가로 (왼쪽→오른쪽)
            elif xi == x2 and yi < y2:
                next_val = query[xi][yi+1]
                query[xi][yi] = next_val
                min_val = min(min_val, next_val)
                yi += 1
            # 오른쪽 세로 (아래→위)
            elif xi > x1 and yi == y2:
                next_val = query[xi-1][yi]
                query[xi][yi] = next_val
                min_val = min(min_val, next_val)
                xi -= 1
            # 위 가로 (오른쪽→왼쪽)
            elif xi == x1 and yi > y1:
                next_val = query[xi][yi-1]
                query[xi][yi] = next_val
                min_val = min(min_val, next_val)
                yi -= 1
        
        query[x1][y1+1] = temp  # 저장했던 값을 다음 위치에
        
        return min_val
    
    for query in queries:
        x1, y1, x2, y2 = query
        # 1-indexed를 0-indexed로 변환
        min_val = turn_clock(x1-1, y1-1, x2-1, y2-1, answer)
        result.append(min_val)
    
    return result