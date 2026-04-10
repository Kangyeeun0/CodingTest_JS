def solution(numbers):
    answer = []
    
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            # 가장 오른쪽 0의 위치 찾기
            bit = (num ^ (num + 1)) + 1 >> 2
            answer.append(num + bit)
    
    return answer