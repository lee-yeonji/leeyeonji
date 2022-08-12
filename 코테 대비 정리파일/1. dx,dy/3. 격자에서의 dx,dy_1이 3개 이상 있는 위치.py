'''
격자에서의 dx, dy 테크닉은 (x행, y열)이라 생각하고 진행하는 것이 좋음
격자의 범위가 벗어나는 지를 판단해주는 in_range()함수를 만들어 사용하면
더 간결한 코드를 구현할 수 있음
'''

# 변수 선언 및 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n) # list comprehension 
]

x, y = 0, 0
# dxs, dys 정의
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 인접한 위치가 격자 안에 들어오는 지를 판단
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀져 있는 함수
def adj_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt

# 각 칸 중 상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수 탐색
ans = 0
for i in range(n):
    for j in range(n):
        if adj_cnt(i, j) >= 3:
            ans += 1
print(ans)