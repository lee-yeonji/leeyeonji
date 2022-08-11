import sys
from collections import deque

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# bfs에 필요한 변수들
q = deque()
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한 최단거리 기록
step = [
    [0 for _ in range(m)]
    for _ in range(n)
]

ans = INT_MAX

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return in_range(x, y) and grid[x][y] and not visited[x][y]

# queue에 새로운 위치를 추가하고 방문 여부 표시
# 시작점으로부터의 최단거리 값도 갱신
def push(new_x, new_y, new_step):
    q.append((new_x, new_y))
    visited[new_x][new_y] = 1
    step[new_x][new_y] = new_step

# bfs로 최소 이동 횟수 구하기
def bfs():
    global ans

    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

    # queue에 남은 것이 없을 때까지 반복 
    while q:
        # queue에서 가장 먼저 들어온 원소를 빼기 
        x, y = q.popleft()

        # queue에서 뺀 원소의 위치를 기준으로 4방향 확인 
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy
            if can_go(new_x, new_y):
                # 최단 거리는 이전 최단 거리에서 1 증가 
                push(new_x, new_y, step[x][y] + 1)

    # 우측 하단에 가는 것이 가능할 때만 답 갱신
    if visited[n - 1][m - 1]:
        ans = step[n - 1][m - 1]

# bfs를 이용해 최소 이동 횟수를 구함
push(0, 0, 0)
bfs()

# 불가능한 경우라면 -1가 답이 된다
if ans == INT_MAX:
    ans = -1

print(ans)