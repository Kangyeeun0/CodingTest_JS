
def solution(cards):
    answer = 0
    card_cnt = []
    boxes = {}
    
    for i in range(1, len(cards)+1) :
        boxes[i] = cards[i-1]
        
    # print(boxes)
    
    one_set_cnt = 0
    
    k = 1
    # print(boxes[k])
    
    while boxes :
        if k in boxes:
            next_box = boxes[k]
            one_set_cnt +=1
            del boxes[k]
            k = next_box
                    
        else :
            card_cnt.append(one_set_cnt)
            one_set_cnt = 0
            next_box = next(iter(boxes))
            k = next_box
        
    
    
    if one_set_cnt > 0 :
        card_cnt.append(one_set_cnt)
    
    if len(card_cnt) <= 1 :
        return 0
    else :
        card_cnt.sort(reverse=True)
        return card_cnt[0] * card_cnt[1]
        
    
    return answer