
// 파이썬 딕셔너리에 대한 선행 개념이 있어야 풀 수 있는 문제임


https://github.com/star1262/webPilot/blob/master/22%EC%A3%BC%EC%B0%A8/%ED%8C%8C%EC%9D%B4%EC%8D%AC/dictionary

- 딕셔너리는 key와 value를 한 쌍으로 갖는 자료형임
- 딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요소값을 구하지 않고,
  key를 통해 value를 얻음 
- 딕셔너리는 key와 value 쌍 여러 개가 {}로 둘러싸여 있음
- 딕셔너리는 key를 사용해서 value를 얻을 수 있음 
- 딕셔너리 이름이 a라면 a.keys()는 a의 key만 모아서 반환함
- key를 얻는 것과 마찬가지로 a.values() a의 value만 모아서 반환함


def solution(clothes):

    answer = 1
    
    // d = {}로 딕셔너리를 선언한다 
    d = {}
    
    // for val,key in clothes로
    // 의상의 이름을 val로 의상의 종류를 key로 지정한다 
    for val, key in clothes:
        
        // 만약 d.keys()에 key가 있다면
        // 해당하는 key에 val을 추가한다 
        if key in d.keys():
            d[key].append(val)
        // 만약 해당하는 key에 val이 없다면
        // key에 val을 추가한다 
        else:
            d[key]= [val]
    
    // for문으로 d.values()를 순회하면서
    // answer에 len(val)+1을 곱해준다 
    // 이렇게 하는 이유는 하나의 key에서 선택할 수 있는 가지수+선택하지 않는 경우
    // 이렇게를 전체 케이스에 곱해주는 것이다. 
    for val in d.values():
        answer *= (len(val)+1)
    
    // 적어도 하나의 의상은 선택해야 하므로 -1을 해준다 
    return answer-1
