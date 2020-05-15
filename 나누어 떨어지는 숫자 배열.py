배운 점
1) 파이썬 배열의 sort는 배열 이름.sort()로 해준다
2) 파이썬 배열이 비어 있는지 확인하는 것은 if not 배열 이름: 으로 할 수 있다. 


def solution(arr, divisor):
    answer = []
    
    // arr 배열의 값들에 대해서
    // 그 배열의 값이 divisor로 나눠지면
    // 배열 answer에 추가해줌 
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            answer.append(arr[i])
    
    // 배열 answer를 오름차순으로 정렬함 
    answer.sort()
    
    // 배열 answer가 비어 있다면,
    // 배열 answer에 -1을 추가함 
    if not answer:
        answer.append(-1)
    
    // 결과인 answer를 리턴함 
    return answer
