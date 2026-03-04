def solution(citations):
    citations.sort(reverse=True)  # 내림차순 정렬
    h_index = 0
    
    for i, c in enumerate(citations):
        # i+1: 지금까지 확인한 논문 수
        if c >= i + 1:
            h_index = i + 1  # H-Index 후보 갱신
        else:
            break  # 조건 만족하지 않으면 더 이상 증가하지 않음
    
    return h_index