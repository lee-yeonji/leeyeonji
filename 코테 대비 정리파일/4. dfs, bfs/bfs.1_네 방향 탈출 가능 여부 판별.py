from collections import deque

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
q = deque()
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

# bfs 탐색
def bfs():

    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

    while q:
        # 현재 방문한 위치 가져오기
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            # 각 위치로 이동할 수 있는지 여부 확인 후 dfs 탐색
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

q.append((0, 0))
visited[0][0] = True

bfs()
print(int(visited[n-1][m-1]))