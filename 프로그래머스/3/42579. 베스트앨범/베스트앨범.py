def solution(genres, plays):
    answer = []
    dic = dict()
    genre_total = dict()
    
    for i in range(len(plays)):
        if genres[i] not in dic:
            dic[genres[i]] = []
            genre_total[genres[i]] = 0
        dic[genres[i]].append([plays[i], i])
        genre_total[genres[i]] += plays[i]
    
    # 수정 1: items()로 (장르, 총재생수) 튜플 정렬
    genre_sort = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    for genre, _ in genre_sort:  # (장르, 총재생수) 튜플
        songs = sorted(dic[genre], key=lambda x: (-x[0], x[1]))
        
        # 수정 2: 최대 2곡까지만
        for i in range(min(2, len(songs))):
            answer.append(songs[i][1])
    
    return answer