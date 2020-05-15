
// 배운 점
(1) 배열의 이름에 max만 씌움으로 인해서 그 배열의 최대값을 구할 수 있음
     ex) max(scores)
(2) 우선, max_score를 구한 후,
    answer 배열에 모든 가능한 max_score의 인덱스를 추가해주는 것이 핵심임(5/15) 
(3) modulo연산을 통해서 num1,num2,num3 배열을 반복적으로 사용할 수 있음(5/15) 


def solution(answers):
    answer = []
    
    // scores 배열을 선언함
    scores = [0, 0, 0]
    
    // num1, num2, num3 3개의 배열을 선언함
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    // for문을 len(answers)만큼 순회하면서
    for i in range(len(answers)):
    
        // answers[i]와 num1[i%5]가 일치하면
        // scores[0]에 1을 더해줌 
        if answers[i] == num1[i%5]:
            scores[0] += 1
        
        // answers[i]와 num2[i%8]가 일치하면
        // scores[1]에 1을 더해줌 
        if answers[i] == num2[i%8]:
            scores[1] += 1
            
        // answers[i]와 num3[i%10]이 일치하면
        // scores[2]에 1을 더해줌 
        if answers[i] == num3[i%10]:
            scores[2] += 1
    
    // max_score에 scores배열의 최대값을 저장함
    max_score = max(scores)
    
    // 가장 많이 맞힌 사람이 여러 명일수 있으므로
    // max_score에 해당하는 값을 모두 answer배열에 넣어줌
    for i in range(len(scores)):
        if scores[i] == max_score:
            answer.append(i+1)
           
    // answer 배열을 리턴함 
    return answer
