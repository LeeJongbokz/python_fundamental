배운 점
(1) string[i][1:] 와 같은 문법으로 1번 인덱스부터 끝까지 반환해낼 수 있다.
(2) strings[i] = strings[i][n] + string[i] 와 같은 문법으로 n번 index를 strings[i]에 추가할 수 있다. 

def solution(strings, n):
    answer = []
    
    // strings의 각각의 원소, strings[i]에 대하여
    // strings[i][n]을 strings[i]에 더해줌
    // 이렇게 하는 이유는 strings[i]를 strings[i][n]을 기준으로 정렬하기 위함임 
    for i in range(len(strings)):
        strings[i] = strings[i][n]+strings[i]
        
    // strings를 sort해줌
    strings.sort()
    
    // 결과적으로는 strings[i][0]은 필요가 없으므로
    // 결과에는 strings[i][1:]만 answer 배열에 더해줌 
    for i in range(len(strings)):
        answer.append(strings[i][1:])
    
    // answer 배열을 리턴함 
    return answer
