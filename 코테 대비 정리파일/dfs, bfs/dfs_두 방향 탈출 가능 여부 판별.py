# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 주어진 x, y가 격자 범위 안에 들어갈 지를 알아보기
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 주어진 위치로 이동 가능 여부 확인
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

# dfs 탐색
def dfs(x, y):

    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        # 각 위치로 이동할 수 있는지 여부 확인 후 dfs 탐색
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            dfs(new_x, new_y)

visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])