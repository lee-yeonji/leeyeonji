n = int(input())
num = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def init():
    # 시작점 
    dp[0][0] = num[0][0]

    # 좌좌측 열의 초기값 설정 
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + num[i][0]

    # 최상단 행의 초기값 설정 
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + num[0][j]

init()

# 탐색하는 위치의 위에 값과 우측 값 중 큰 값에 해당 위치의 숫자를 더함
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1] + num[i][j], dp[i-1][j] + num[i][j])

print(dp[n-1][n-1])