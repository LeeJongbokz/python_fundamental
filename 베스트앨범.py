def solution(genres, plays):
    answer = []
 
    a = {}
 
    for i in range(0, len(genres)):
        if genres[i] not in a:
            a[genres[i]] = plays[i]
        else:
            a[genres[i]] += plays[i]
 
    a_reverse = sorted(a, key=a.get, reverse=True)
 
    for key in a_reverse:
        temp = []
 
        for i in range(0, len(genres)):
            if key == genres[i]:
                temp.append((plays[i], i))
 
        temp_reverse = sorted(temp, key=lambda x:x[0], reverse=True)
 
        if len(temp_reverse) >= 2:
            for i in range(0,2):
                answer.append(temp_reverse[i][1])
        else:
            answer.append(temp_reverse[0][1])
 
    return answer
