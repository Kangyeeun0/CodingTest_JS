def solution(m, musicinfos):
    answer = []
    songs = []
    titles=[]
    
    def change_code(melody) :
        melody = melody.replace("C#", 'c')
        melody = melody.replace("D#", 'd')
        melody = melody.replace("F#", 'f')
        melody = melody.replace("G#", 'g')
        melody = melody.replace("A#", 'a')
        return melody
              
        
    for i in range(len(musicinfos)) :
        start, end, title, song = musicinfos[i].split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        playtime = (end_h * 60 + end_m) - (start_h * 60 + start_m)
        song = change_code(song)
        l = (playtime // len(song)) + 1
        song = song * l
        songs.append([song[0:playtime],playtime])
        titles.append(title)
        
    change_m = change_code(m)
    # print(songs, change_m)
    for j in range(len(songs)) :
        melody, playtime = songs[j]
        if change_m in melody :
            answer.append([titles[j], playtime])
        
    if answer :
        answer.sort(key= lambda x : x[1], reverse = True)
        print(answer)
        return answer[0][0]
    return "(None)"