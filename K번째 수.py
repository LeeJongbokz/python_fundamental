배운 점
1) 파이썬은 배열을 배열이름 = [] 이런 식으로 선언한다
2) 문제를 몇 단계로 나눠서 접근할 수 있다.
   첫 번째는, 자르기
   두 번째는, 자른 값들을 배열에 담기
   세 번째는, 배열에서 특정 위치의 값을 추출하기
3) sort()메소드를 통해 배열에 담긴 값들을 정렬할 수 있다
4) 배열에 새로운 값을 추가할 때는 append()를 쓸 수 있다. 


def solution(array, commands):
    answer = []
    
    // commands 배열의 길이만큼 순회하면서
    for i in range(len(commands)):
    
        // 배열에서 자르기 시작하는 부분
        start = commands[i][0]
        // 배열에서 자르기를 마치는 부분
        end = commands[i][1]
        
        // 자른 배열값들을 추가할 배열 
        temp = []
        
        // array 배열에 대해서
        for j in range(len(array)):
            // start-1부터 end-1까지
            if start-1<= j and j <= end-1:
                // temp배열에 값을 더해준다
                // 이 때는, append를 사용해서 더해준다 
                temp.append(array[j])
        
        // temp.sort()를 사용하면 배열의 값들을 오름차순 정렬을 할 수 있다 
        temp.sort()
        // order는 정렬된 temp배열에서 내가 값을 뽑아야 하는 위치를 의미한다
        order = commands[i][2]
        // answer 배열에 해당하는 위치의 원소를 더해준다. 
        // 이 때도, 마찬가지로 append 배열을 사용한다. 
        answer.append(temp[order-1])
        
    // 결과인 answer 배열을 리턴한다    
    return answer
