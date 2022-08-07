# 변수 선언 및 입력
n, m, t = tuple(map(int, input().split()))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

count = [
    [0 for _ in range(n)]
    for _ in range(n)
]
nxt_count = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 초기 count 배열을 설정
# 구슬이 있는 곳에 1을 표시
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    x -= 1
    y -= 1
    count[x][y] = 1


# 범위가 격자 안에 들어가는지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 인접한 곳들 중 가장 값이 큰 위치를 반환
def get_max_neighbor_pos(curr_x, curr_y):
    
    # 상하좌우 순서로 방향을 정의
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    max_num, max_pos = 0, (0, 0)
    
    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인
    for dx, dy in zip(dxs, dys):
        nxt_x, nxt_y = curr_x + dx, curr_y + dy
        
        # 범위안에 들어오는 격자 중 최댓값을 갱신
        if in_range(nxt_x, nxt_y) and arr[nxt_x][nxt_y] > max_num:
            max_num = arr[nxt_x][nxt_y]
            max_pos = (nxt_x, nxt_y)
    
    return max_pos


# (x, y) 위치에 있는 구슬 이동
def move(x, y):
    # 인접한 곳들 중 가장 값이 큰 위치를 계산
    nxt_x, nxt_y = get_max_neighbor_pos(x, y)
    
    # 그 다음 위치에 구슬의 개수를 1만큼 추가
    nxt_count[nxt_x][nxt_y] += 1


# 구슬을 전부 한 번씩 이동시킴
def move_all():
    # 그 다음 각 위치에서의 구슬 개수를 전부 초기화
    for i in range(n):
        for j in range(n):
            nxt_count[i][j] = 0
            
    # (i, j) 위치에 구슬이 있는경우 
    # 움직임을 시도해보고, 그 결과를 전부 next_count에 기록
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    
    # next_count 값을 count에 복사.
    for i in range(n):
        for j in range(n):
            count[i][j] = nxt_count[i][j]


# 충돌이 일어나는 구슬은 전부 삭제
def remove_duplicate_marbles():
    # 충돌이 일어난 구슬들이 있는 위치만 빈 곳으로 설정
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0


# 조건에 맞춰 시뮬레이션을 진행
def simulate():
    # Step1
    # 구슬을 전부 한 번씩 이동시킴 
    move_all()
    
    # Step2
    # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 삭제 
    remove_duplicate_marbles()
 
# t초 동안 시뮬레이션을 진행
for _ in range(t):
    simulate()

# 출력:
ans = 0
for i in range(n):
    for j in range(n):
        ans += count[i][j]

print(ans)
