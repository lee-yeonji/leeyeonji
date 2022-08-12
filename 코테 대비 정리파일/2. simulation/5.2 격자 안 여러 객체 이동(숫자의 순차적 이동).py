# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 범위가 격자 안에 들어가는지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 위치 찾기
def find_pos(num):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                return (i, j)

# 위치 찾은 후 반환               
def nxt_pos(pos):

    # 순서 상관없이 방향을 정의
    dxs, dys = [-1, 0, 1, -1, 1, -1, 0, 1], [1, 1, 1, 0, 0, -1, -1, -1]
    
    x, y = pos

    max_num = -1
    max_pos= (-1, -1)
    
    # 각각의 방향에 대해 나아갈 수 있는 곳이 있는지 확인
    for dx, dy in zip(dxs, dys):
        # 조사할 위치 
        nxt_x, nxt_y = x + dx, y + dy
        
        # nxt_x, nxt_y가 범위 내에 있고, 현재 최댓값보다 클 경우 최댓값 갱신  
        if in_range(nxt_x, nxt_y) and arr[nxt_x][nxt_y] > max_num:
            # 최댓값 갱신
            max_num, max_pos = arr[nxt_x][nxt_y], (nxt_x, nxt_y)
    return max_pos

# 바꿔주기
def swap(pos, nxt_pos):
    (x, y), (nxt_x, nxt_y) = pos, nxt_pos
    arr[x][y], arr[nxt_x][nxt_y] = arr[nxt_x][nxt_y], arr[x][y]

# 시뮬레이션 함수 만들기    
def simulate():
    # 번호가 증가하는 순으로 그 다음 위치를 구해 한 칸씩 움직임
    for num in range(1, n * n + 1):
        pos = find_pos(num)
        max_pos = nxt_pos(pos)
        swap(pos, max_pos)

# m번 시뮬레이션 돌리기
for _ in range(m):   
    simulate()
                                            
# 출력하기
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()