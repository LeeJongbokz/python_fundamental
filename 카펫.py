
def solution(brown, red):
    answer = []
    
    // total이라는 변수에 brown과 red를 더해준다
    total = brown + red
    
    // m에 total 값을 담아준다 
    m = total
    
    while 1:
        
        // 만약 total이 m으로 나누어지면,
        // n에 total/m을 담는다 
        // total이 m으로 나누어진다는 의미는
        // m,n(=total/m)으로 직사각형 모양을 구성할 수 있다는 의미이다. 
        if total % m == 0:
            n = total / m
            
        // 만약 total이 m으로 나누어지지 않는다면 
        // m을 1만큼 값을 줄여준다 
        else:
            m -= 1
            continue
        
        // temp에 2*m+2*n-4를 담는다
        // temp는 전체 직사각형 테두리의 개수를 의미한다. 
        temp = 2*m+2*n-4
            
        // temp과 brown하고 일치하는지 확인한다
        // 일치한다는 것은 즉, 이 때의 m과 n이 답이라는 의미이다
        // 따라서 answer에 m과 n을 넣고 break한다. 
        if temp == brown:
            answer.append(m)
            answer.append(n)
            break
        
        // m을 1만큼 값을 줄여준다 
        m -= 1
    
    // 결과인 answer 배열을 리턴한다 
    return answer
