n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# row행의 col_s~col_e 사이의 금의 개수를 계산
def get_num_of_gold(row_s, col_s, row_e, col_e):
    num_of_gold = 0

    for row in range(row_s, row_e+1):
        for col in range(col_s, col_e+1):
            num_of_gold += grid[row][col]
    return num_of_gold

max_gold = 0

# (row, col)의 3 * 3 격자의 좌측 모서리인 경우를 전부 탐색
for row in range(n-2):
    for col in range(n-2):
        
        # 금의 개수를 계산
        num_of_gold = get_num_of_gold(row, col, row+2, col + 2)

        # 최대 금의 개수를 저장
        max_gold = max(max_gold, num_of_gold)
print(max_gold)