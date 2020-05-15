// 배운 점
(1) 변수를 int로 바꿔서 저장하려면, temp = (int)temp 
    이런 식으로 저장하면 된다. 

// math를 import하면 Math.floor()를 쓸 수 있다. 
import math

def solution(x):
    answer = True
    
    // temp에 x값을 저장한다 
    temp = x
    
    // sum에 0을 저장한다 
    sum = 0
    
    while 1:
        // temp가 1보다 작으면 
        // while문을 break한다. 
        // 여기서 1보다 작다는 것은 0임을 의미한다. 
        if temp < 1:
            break
        
        // num에 temp를 10으로 나눈 나머지 값을 저장한다
        num = temp % 10
        // sum에 num을 더한다
        sum += num
        // temp를 10으로 나눈다
        temp /= 10
        // temp를 int로 바꿔서 저장한다 
        temp = int(temp)
    
    // x가 sum으로 나눠지면
    // answer에 True를 저장한다.  
    if x % sum == 0:
        answer = True
    // x가 sum으로 나눠지지 않으면
    // answer에 False를 저장한다. 
    else:
        answer = False
    
    // answer를 리턴한다 
    return answer
