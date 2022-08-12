n = int(input())

# 시간복잡도 줄이기 
max_n = 1000
mod = 10007
dp = [ 0 for _ in range(max_n + 1) ]

# 초기 조건 설정
dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = ( dp[i - 2] + dp[i - 1] ) % mod 

print(dp[n])