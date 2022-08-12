# 변수 선언 및 입력
n, m = tuple(map(int, input().split())) # 4 8
# n * n 크기의 격자 위에 총 m번에 걸쳐 색칠을 진행
arr = [
    [0] * n 
    for _ in range(n)
]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and  y < n

def adj_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    return cnt

for _ in range(m):
    x, y = tuple(map(int, input().split()))
    x -= 1
    y -= 1
    arr[x][y] = 1

    # 해당 칸을 탐색
    if adj_cnt(x, y) == 3:
        print(1)
    else:
        print(0)
