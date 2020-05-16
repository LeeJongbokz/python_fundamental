// 이 문제의 핵심은
// (1) 정렬 함수인 sorted()를 제대로 활용하는 것과
// (2) 예외 케이스(장르의 노래가 1가지인 경우)를 잘 구별해내는 것 
// (3) 딕셔너리와 배열을 잘 사용하는 것 임 

def solution(genres, plays):
    answer = []
 
    // 딕셔너리 a를 선언함
    a = {}
 
    // 가장 많이 재생된 genres를 고르기 위해
    // 딕셔너리 a에 genres마다 노래의 수를 더해줌 
    for i in range(0, len(genres)):
        if genres[i] not in a:
            a[genres[i]] = plays[i]
        else:
            a[genres[i]] += plays[i]
 
    // a를 value를 기준으로 내림차순으로 정렬함
    // key=a.get을 하면, a.get은 value이기 때문에
    // value를 기준으로 정렬을 할 수 있음
    // 딕셔너리의 value를 기준으로 적용하고 싶을 때는
    // 반드시 a.get을 사용해야 함 
    a_reverse = sorted(a, key=a.get, reverse=True)
 
    // a_reverse에 있는 key(장르)를 기준으로
    // a_reverse는 딕셔너리이므로, 바로 key를 인자로 적용할 수 있음 
    for key in a_reverse:
        temp = []
 
        // 전체 장르 중에서 해당 key(장르)에 해당하는 것만 골라서
        for i in range(0, len(genres)):
            if key == genres[i]:
                // temp 배열에 추가해줌
                // 이 때, 아래와 같이 2차원 배열을 만들 수 있음 
                // 이 때, 반드시 plays[i]를 추가해야 함 
                temp.append((plays[i], i))
        
        // temp_reverse는 temp 배열을 key=lambda x:x[0]을 기준으로
        // 내림차순으로 정렬한 것임 
        temp_reverse = sorted(temp, key=lambda x:x[0], reverse=True)
 
        // 만약 temp_reverse의 길이가 2와 같거나 더 크다면 
        if len(temp_reverse) >= 2:
            // 해당하는 위치의 원소 2개를 answer에 넣어줌
            for i in range(0,2):
                answer.append(temp_reverse[i][1])
                
        // 만약 1개라면 1개만 넣어줌         
        else:
            answer.append(temp_reverse[0][1])
 
    return answer
