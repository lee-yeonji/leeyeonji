# 변수 선언 및 입력
n = int(input())
town = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

town_num = 0
town_nums = list()

# 주어진 x, y가 격자 범위 안에 들어갈 지를 알아보기
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 주어진 위치로 이동 가능 여부 확인
def can_go(x, y):
    if not in_range(x, y):
        return False
    if visited[x][y] or town[x][y] == 0:
        return False
    return True

# dfs 탐색
def dfs(x, y):
    global town_num

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        # 각 위치로 이동할 수 있는지 여부 확인 후 dfs 탐색
        if can_go(new_x, new_y):
            visited[new_x][new_y] = True
        
            # 마을에 존재하는 사람을 한 명 추가 
            town_num += 1
            dfs(new_x, new_y)

# 격자의 각 위치에서 탐색을 시작할 수 있는 경우
# 한 마을에 대한 dfs 탐색 수행
for i in range(n):
    for j in range(n):
        if can_go(i, j):
            # 해당 위치를 방문할 수 있는 경우 visited 배열 갱신
            # 새로운 마을을 탐색한다는 의미로 town_cnt을 1로 갱신
            visited[i][j] = True
            town_num = 1

            dfs(i, j)

            # 한 마을에 대한 탐색이 끝난 경우 마을 내의 사람 수를 저장 
            town_nums.append(town_num)

# 각 마을 내 사람의 수를 오름차순으로 정렬
town_nums.sort()

print(len(town_nums))

for i in range(len(town_nums)):
    print(town_nums[i])