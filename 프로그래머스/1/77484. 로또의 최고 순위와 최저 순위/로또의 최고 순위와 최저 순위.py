from collections import Counter
def solution(lottos, win_nums):
    answer = []
    correct_cnt = 0
    zero_cnt = 0
    rank_dic = dict()
    n=6
    for i in range(1, 7) :
        rank_dic[n] = i
        n-=1
    
    counter1 = Counter(lottos)
    counter2 = Counter(win_nums)
    correct_cnt = sum((counter1 & counter2).values())
    zero_cnt = counter1[0]
    
    
    max_cnt = correct_cnt + zero_cnt
    min_cnt = correct_cnt
    
    answer = [rank_dic[max_cnt] if max_cnt in rank_dic else 6, rank_dic[min_cnt] if min_cnt in rank_dic else 6]
    
    return answer