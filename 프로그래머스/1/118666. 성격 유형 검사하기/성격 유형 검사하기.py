def solution(survey, choices):
    answer = ''
    
    dic_rt = {"R":0, "T": 0}
    dic_cf = {"C":0, "F": 0}
    dic_jm = {"J":0, "M": 0}
    dic_an = {"A":0, "N": 0}
    
    
    for i in range(len(survey)) :
        if survey[i] in ["AN", "NA"] :
            if choices[i] >= 4 :
                dic_an[survey[i][1]] += choices[i] - 4
            else :
                dic_an[survey[i][0]] += 4 - choices[i] 
        elif survey[i] in ["CF", "FC"] :
            if choices[i] >= 4 :
                dic_cf[survey[i][1]] += choices[i] - 4
            else :
                dic_cf[survey[i][0]] += 4 - choices[i] 
        elif survey[i] in ["MJ", "JM"] :
            if choices[i] >= 4 :
                dic_jm[survey[i][1]] += choices[i] - 4
            else :
                dic_jm[survey[i][0]] += 4 - choices[i] 
        elif survey[i] in ["RT", "TR"] :
            if choices[i] >= 4 :
                dic_rt[survey[i][1]] += (choices[i] - 4)
            else :
                dic_rt[survey[i][0]] += (4 - choices[i]) 
    # print(dic_rt, dic_cf, dic_jm, dic_an)
    
    answer+=max(dic_rt, key = dic_rt.get)
    answer+=max(dic_cf, key = dic_cf.get)
    answer+=max(dic_jm, key = dic_jm.get)
    answer+=max(dic_an, key = dic_an.get)
    
        
    return answer