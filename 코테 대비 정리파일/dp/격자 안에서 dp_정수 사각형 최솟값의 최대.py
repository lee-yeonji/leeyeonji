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

    # 최좌측 열의 초기값 설정 
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], num[i][0])

    # 최상단 행의 초기값 설정 
    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], num[0][j])

init()

# 거쳐간 위치에 적여져 있는 숫자들 중 최솟값을 최대로 하는 값 탐색
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(dp[i-1][j], num[i][j]), min(dp[i][j-1], num[i][j]))

print(dp[n-1][n-1])