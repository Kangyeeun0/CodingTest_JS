#heap은 오름차순 정렬과는 조금 다른 것
#부모노드 <= 자식노드만 만족하면 됨
#여기서 핵심은 heap의 가장 첫원소만 가장 최소값을 만족한다는 것.
#가장 최솟값을 사용할 거면 heap이 맞고, 정렬이 필요하다면 리스트 정렬을 사용해야 함
def solution(n, s):
    
    if n > s :
        return [-1]
    
    k = s // n
    r = s % n
    answer = [k] * n

    for i in range(r):
        answer[-1-i] += 1

    return answer