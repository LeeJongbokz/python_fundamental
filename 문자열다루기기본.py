// 배운 점
(1) 어떤 문자열이 숫자로만 구성되어 있는지는 s.isdigit()와 같이 파악할 수 있음


// 배운 점
(1) isdigit()은 문자열의 모든 문자가 숫자일 때는 true를,
    아닐 때는 false를 반환함 

def solution(s):
   
    return s.isdigit() and (len(s) == 4 or len(s) == 6)
