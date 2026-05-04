from collections import defaultdict

def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for result in results :
        a, b = result
        win[a].add(b)
        lose[b].add(a)
    
    for i in range(1, n+1) :
        for winner in lose[i] :
            win[winner].update(win[i])
        for loser in win[i] :
            lose[loser].update(lose[i])
            
    # print(win, lose)
    
    for i in range(1, n+1) :
        if len(win[i]) + len(lose[i]) == n - 1 :
            answer += 1
            
    return answer