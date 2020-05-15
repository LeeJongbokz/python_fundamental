def solution(num):
    answer = 0
    
    // cnt = 0 에서 시작한다 
    cnt = 0 
    
    while 1:
        // num이 1이 되거나, cnt가 501이면
        // while문을 탈출한다 
        if num == 1 or cnt == 501:
            break
        
        // num이 짝수이면 2로 나눠준다
        if num % 2 == 0:
            num /= 2
        // num이 홀수이면 3을 곱하고 1을 더해준다.
        else:
            num = 3*num+1
            
        // cnt를 1 더해준다
        cnt += 1
    
    // cnt가 501이면 answer에 -1을 저장한다
    if cnt == 501:
        answer = -1
    // cnt가 501이 아니면 answer에 cnt를 저장한다 
    else:
        answer = cnt
    
    // answer를 리턴한다 
    return answer
