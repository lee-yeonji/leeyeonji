# 변수 선언 및 입력
n, r, c = tuple(map(int, input().split()))
lst = [[0] * (n + 1)]
for _ in range(n):
    lst.append([0] + list(map(int, input().split())))
    
# 방문하게 되는 숫자들을 담을 곳
result = []

# 범위가 격자 안에 들어가는지 확인
def in_range(x, y):
    return 0 <= x and x <= n and 0 <= y and y <= n

# 범위가 격자 안이고, 해당 위치의 값이 더 큰지 확인
def can_go(x, y, cur_num):
    return in_range(x, y) and lst[x][y] > cur_num

# 조건에 맞춰 움직이기
# 움직였다면 true 반환
# 움직일 수 있는 곳이 없었다면 false 반환
def simulate():
    global r, c

    # 상하좌우 순서로 방향 정의 
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    # 각각의 방향에 대해 나아갈 수 있는 곳인지 확인 
    for dx, dy in zip(dxs, dys):
        nxt_x, nxt_y = r + dx, c + dy

        # 갈 수 있는 곳이라면 이동하고 true 반환 
        if can_go(nxt_x, nxt_y, lst[r][c]):
            r, c = nxt_x, nxt_y
            return True
    
    # 움직일 수 있는 곳이 없었다는 의미 => false 반환 
    return False

# 초기 위치에 적혀있는 값을 답에 넣어줌
result.append(lst[r][c])
while True:
    # 조건에 맞춰 움직여봄
    better_exist = simulate()

    # 인접한 곳에 더 큰 숫자가 없다면 종료
    if not better_exist:
        break
    
    # 움직이고 난 후의 위치를 답에 넣어줌
    result.append(lst[r][c])

# 출력
for num in result:
    print(num, end=' ')