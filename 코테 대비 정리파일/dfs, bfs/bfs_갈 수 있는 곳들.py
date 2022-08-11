from collections import deque
# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

# bfs에 필요한 변수들
q = deque()
visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]
    
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and not graph[x][y]

def bfs():
    # queue에 남은 것이 없을 때까지 반복 
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺌 
        x, y = q.popleft()
        
        dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            # 아직 방문한 적이 없으면서 갈 수 있는 곳이면
            # 새로 queue에 넣어주고 방문 여부를 표시 
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

# 시작점을 모두 queue에 넣음
for _ in range(k):
    x, y = tuple(map(int, input().split()))
    q.append((x-1, y-1))
    visited[x-1][y-1] = True                    

bfs()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1
print(cnt)