# 변수 선언 및 입력
n, m, k = tuple(map(int, input().split()))
grid = [ list(map(int, input().split())) for _ in range(n) ]
flag = False

# 해당 row에 [col_s, col_e] 열에 전부 블럭이 없는지 확인 
def none_block(row, col_s, col_e):
    return all([
        not grid[row][col]
        for col in range(col_s, col_e + 1)
    ])

# 최종적으로 도달하게 될 위치는 그 다음 위치에 최초로 블럭이 존재하는 순간임
def get_target_r():
    for row in range(n - 1):
        if not none_block(row + 1, k, k + m - 1):
            return row
    
    return n - 1

k -= 1

# 최종적으로 멈추게 될 위치를 구함
target_r = get_target_r()

# 최종 위치에 전부 블럭 표시
for col in range(k, k + m):
    grid[target_r][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print() 