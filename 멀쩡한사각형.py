
// 재귀함수로 GCD를 구해줌
// 유클리드 호제법에 기초하고 있음 
// 나머지가 0이 아니면 계속 재귀함수를 진입하고,
// 나머지가 0이 되면 그 때의 m값을 리턴함 
def recursive(n, m):

    r = n % m
    
    if r == 0:
        return m
    
    return recursive(m, r)
    


def solution(w,h):
    answer = 0
    
    // w와 h의 최대공약수를 구해줌
    // 최대공약수를 구하는 이유는 
    // 최대공약수로 w와 h를 나눠주기 위함임 
    GCD = recursive(w, h)
    
    // w와 h를 최대공약수로 나눠서 
    // smallW와 smallH를 구함 
    smallW = w / GCD
    smallH = h / GCD
    
    // unable이라는 변수를 다음과 같이 구해줌
    // unable이라는 변수는 smallW와 smallH를 활용해서 구할 수 있음 
    // 이렇게 구할 수 있는 이유는 여러 가지의 케이스를 통해서 규칙성을 발견할 수 있음 
    unable = (smallW-1) + (smallH-1) + 1 
    
    // unable에 GCD를 구해줌
    // 이를 통해 전체 직사각형에서의 unable을 구할 수 있음 
    unable = GCD*unable 
    
    // answer는 전체 개수에서 unable을 제거해줌 
    answer = w*h - unable 
    
    // 결과값인 answer를 리턴함 
    return answer
