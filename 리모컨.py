// 배운 점
(1) 리스트의 여러 가지 원소를 input().split()으로 입력 받을 수 있음
   -> 이 때, 입력되는 입력값은 문자로 입력됨 
   -> 만약 int로 여러 개의 원소를 입력 받고 싶다면 어떻게 해야 하는가?
   -> list(map(int, input().split())) 으로 입력 받으면 된다. 
   -> 왜 이렇게 입력 받아야 하는가?
   -> map은 list의 요소를 지정된 함수로 처리해주는 함수임
      따라서 map(int, input().split()) 이라고 하면, 
      int라는 요소로 input().split()을 처리하는 것임 (4/9) 
(2) 숫자인 변수 c를 str(c)로 바꿈으로써 문자열로 변환할 수 있음 


// 배운 점
(1) 문자로 한 개의 값을 입력 받고 싶으면, input() 
(2) 숫자로 한 개의 값을 입력 받고 싶으면, int(input())
(3) 문자로 여러 개의 값을 입력 받고 싶으면, input.split()
(4) 숫자로 여러 개의 값을 입력 받고 싶으면, list(map(int, input().split()) (5/15) 

(5) if str_c in malf: 
    와 같이 특정 문자가 문자열 안에 있는지 검사할 수 있다  
(6) abs()로 절대값을 구할 수 있음
(7) len()으로 문자열의 길이를 구할 수 있음 
(8) 이 문제에서 핵심은 모든 가능한 케이스에 대해서 최소 이동횟수(abs(i-N)+len(val))를 구한 다음에
    100으로부터 이동횟수 abs(100-N)와 비교해준다는 것임 (5/15) 

// N과 M을 입력 받는다
// N과 M을 입력 받을 때는, int(input())을 사용한다
N = int(input())
M = int(input())

// M이 1이상일 때는, malf배열에 값을 입력한다.
// 이 때 input().split()을 사용해서 입력한다. 
if M > 0:
    malf = input().split()
else:
    malf = []
    
// channel이라는 이름의 배열을 선언한다 
channel = []

// range 0부터 1000001의 범위에 대해서 
for c in range(0, 1000000+1):

    // isAble = True라는 변수를 선언한다 
    isAble = True

    // 만약 c를 string으로 변환한 값(str(c))의 각각의 원소에 대해서
    // 그 원소가 malf에 있는지 검사함
    // 예를 들어 c가 5050이고, malf=[1,3,5]라면
    // str(c) "5050"으로 바꾸고 나서
    // 5가 malf에 있는지 검사하고, 0이 malf에 있는지 검사하고 이런 식으로 검사함 
    // 이렇게 하는 이유는 malf가 문자로 구성된 배열이므로
    // c도 문자로 바꿔서 검사를 해줘야하는 것임 
    for str_c in str(c):
        if str_c in malf:
            isAble = False
            break
            
    // 만약 isAble이라면 channel에 c를 추가함 
    if isAble:
        channel.append(c)
     
// val이라는 변수를 선언해줌
// 이 변수의 목적은 string값을 담기 위함임 
val = ''

// minNum을 99999999로 설정함
minNum = 99999999
    
// channel에 있는 i값에 대하여
for i in channel:
    // 만약 abs(i-N)이 minNum보다 작다면
    if abs(i-N) < minNum:
        // minNum을 abs(i-N)으로 대체함
        minNum = abs(i-N)
        // val은 str(i)로 대체함
        // 이것을 하는 이유는 뒤에서 len(val)을 검사하기 위함임 
        val = str(i)

// 답인 answer는 1차적으로 len(val)과 abs(minNum)으로 구해줌
answer = len(val) + abs(minNum)

// 100으로부터의 거리가 가까울 수 있으므로
// 이를 다시 한 번 확인해서 업데이트 함 
answer = min(abs(100-N), answer)

print(answer)
