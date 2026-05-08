import math
def solution(str1, str2):
    answer = 0
    first = ""
    second = ""
    arr1 = []
    arr2 = []
    sum_j = 0
    mul_j = 0
    
     # str1에서 연속된 영문자 2개 추출
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            arr1.append((str1[i] + str1[i+1]).lower())
    
    # str2에서 연속된 영문자 2개 추출
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            arr2.append((str2[i] + str2[i+1]).lower())
            
    for i in range(0, len(first)-1):
        cut = first[i:i+2]
        arr1.append(cut)

    for i in range(0, len(second)-1):  # 따로 반복
        cut2 = second[i:i+2]
        arr2.append(cut2)


    
    # print(arr1,arr2)

    # 교집합
    temp2 = arr2[:]  # 복사본 만들기
    for item in arr1:
        if item in temp2:
            mul_j += 1
            temp2.remove(item)  # 사용한 것 제거

    sum_j = len(arr1) + len(arr2) - mul_j
    
    if mul_j == 0 and sum_j == 0 :
        return 65536
    else :
        # print(mul_j, sum_j)
        answer = math.floor((mul_j / sum_j) * 65536)
        
        
            
    return answer