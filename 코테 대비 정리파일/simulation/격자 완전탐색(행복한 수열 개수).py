# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
seq = [0 for _ in range(n)]

# seq가 행복한 수열인지를 판단하는 함수
def is_happy_sequence():
    happy_count, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            happy_count += 1
        else:
            happy_count = 1
        max_cnt = max(max_cnt, happy_count)

    # 최대로 연속한 횟수가 m 이상이면 true 반환
    return max_cnt >= m

num_happy = 0

# 가로로 행복한 수열의 수 세기 
for i in range(n):
    seq = grid[i][:]
    
    if is_happy_sequence(): 
        num_happy += 1
        
# 세로로 행복한 수열의 수 세기 
for j in range(n):
    # 세로로 숫자들을 모아 새로운 수열을 만듦
    for i in range(n):
        seq[i] = grid[i][j]
    if is_happy_sequence():
        num_happy += 1

print(num_happy)