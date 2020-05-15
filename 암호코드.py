s = input()

// arr = [int(x) for x in list(s)]로
// 입력 받은 문자열로 숫자 배열을 만들 수 있음
arr = [int(x) for x in list(s)]

// 변수 arr_length에 arr의 길이를 반환함
arr_length = len(arr)

// dp=[0]*(arr_length+1)로
// arr_length+1의 길이로 dp를 0으로 초기화할 수 있음 
dp = [0]*(arr_length+1)

dp[0] = 1

for i in range(1, arr_length+1):
    
    if 1<=arr[i-1] and arr[i-1]<=9:
        dp[i] += dp[i-1]
        
    if i == 1:
        continue
        
    value = arr[i-2]*10+arr[i-1]
    
    if 10<=value and value<=26:
        dp[i] += dp[i-2]
    
    dp[i] %= 1000000
    
print(dp[arr_length]%1000000)
    
