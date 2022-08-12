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
    dp[0][n-1] = num[0][n-1]

    # 최우측 열의 초기값 설정 
    for i in range(1, n):
        dp[i][n - 1] = dp[i - 1][n - 1] + num[i][n - 1]

    # 최상단 행의 초기값 설정 
    for j in range(n-2, -1, -1):
        dp[0][j] = dp[0][j + 1] + num[0][j]

init()

# 탐색하는 위치의 위에 값과 우측 값 중 작은 값에 해당 위치의 숫자를 더함
for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i][j+1] + num[i][j], dp[i-1][j] + num[i][j])

print(dp[n-1][0])