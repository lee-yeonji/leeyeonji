import sys
sys.setrecursionlimit(2500)

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
zone_num = 0

# 이전 탐색에서 방문했던 집의 정보는 의미가 없으므로
# visited 배열 초기화
def return_visited():
    for i in range(n):
        for j in range(m):
           visited[i][j] = False

# 주어진 위치가 격자를 벗어나는지 여부를 반환
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 주어진 위치로 이동할 수 있는지 여부 확인
def can_go(x, y, k):
    if not in_range(x, y):
        return False
    if visited[x][y] or grid[x][y] <= k:
        return False
    return True

def dfs(x, y, k):
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

    # 네 방향에 각각 dfs 탐색 
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x, new_y, k):
            visited[new_x][new_y] = True
            dfs(new_x, new_y, k)

def zone_num_get(k):
    global zone_num

    # 새로운 탐색 시작 의미로 zone_num을 0으로 갱신한 후
    # visited 배열을 초기화
    zone_num = 0
    return_visited()

    # 격자의 각 위치에 대하여 탐색을 시작할 수 있는 경우
    # 해당 위치로부터 시작한 DFS 탐색을 수행
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                # 해당 위치 탐색 가능 시, visited 배열을 갱신
                # 안전 영역을 하나 추가
                visited[i][j] = True
                zone_num += 1

                dfs(i, j, k)

max_zone_num = -1
k_answer = 0
height_max = 100

# 각 가능한 비의 높이에 대하여 안전 영역의 수를 탐색
for k in range(1, height_max+1):
    zone_num_get(k)

    # 기존의 최대 영역의 수보다 클 경우 갱신하고 인덱스를 저장
    if zone_num > max_zone_num:
        max_zone_num, k_answer = zone_num, k

print(k_answer, max_zone_num)