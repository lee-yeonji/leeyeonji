import sys
from collections import deque

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

# bfs에 필요한 변수들
q = deque()
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# step[i][j] : 시작점으로부터 (i, j) 지점에 도달하기 위한 최단거리 기록
step = [
    [0 for _ in range(n)]
    for _ in range(n)
]

ans = INT_MAX

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y]

# queue에 새로운 위치를 추가하고 방문 여부 표시
# 시작점으로부터의 최단거리 값도 갱신
def push(new_x, new_y, new_step):
    q.append((new_x, new_y))
    visited[new_x][new_y] = 1
    step[new_x][new_y] = new_step

# bfs로 최소 이동 횟수 구하기
def bfs():
    global ans

    # queue에 남은 것이 없을 때까지 반복 
    while q:
        # queue에서 가장 먼저 들어온 원소를 빼기 
        x, y = q.popleft()

        dxs = [-2, -1, 1, 2, -2, -1, 1, 2]
        dys = [1, 2, 2, 1, -1, -2, -2, -1]

        # queue에서 뺀 원소의 위치를 기준으로 4방향 확인 
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이라면
            # 새로 queue에 넣어줌
            if can_go(new_x, new_y):
                # 최단 거리는 이전 최단 거리에서 1 증가 
                push(new_x, new_y, step[x][y] + 1)

    # 우측 하단에 가는 것이 가능할 때만 답 갱신
    if visited[r2][c2]:
        ans = step[r2][c2]

# bfs를 이용해 최소 이동 횟수를 구함
push(r1, c1, 0)
bfs()

# 불가능한 경우라면 답은 -1이 된다
if ans == INT_MAX:
    ans = -1

print(ans)