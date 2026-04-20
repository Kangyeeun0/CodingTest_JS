def solution(sticker):
    answer = 0
    n = len(sticker)
    
    # 예외 처리
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker[0], sticker[1])
    
    # 경우 1: 첫 번째 스티커를 선택할 수 있는 경우 (마지막 제외)
    # 인덱스 0 ~ n-2까지 고려
    dp1 = [0] * (n - 1)
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    
    for i in range(2, n-1) :
        dp1[i] = max(dp1[i-1],dp1[i-2] + sticker[i])
        
    dp2 = [0] * (n-1)
    dp2[0] = sticker[1]
    dp2[1] = max(sticker[1], sticker[2])
    
    for i in range(2, n-1) :
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i+1])
   

    return max(dp1[-1], dp2[-1])