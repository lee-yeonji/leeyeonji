# 변수 선언 및 입력

n = int(input())
arr = [
    list(map(int, input().split())) 
    for _ in range(n)
]
next_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and \
           abs(x - center_x) + abs(y - center_y) < bomb_range

def bomb(center_x, center_y):
    bomb_range = arr[center_x][center_y]   
    
    # step 1. 폭탄이 터질 위치 => 0으로 채우기 
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                arr[i][j] = 0
    
    # step 2. 폭탄이 터진 이후의 결과 => next_arr에 저장
    for j in range(n):
        next_row = n - 1
        for i in range(n-1, -1, -1):
            if arr[i][j]:
                next_arr[next_row][j] = arr[i][j]
                next_row -= 1

    # step 3. arr로 다시 값을 옮김
    for i in range(n):
        for j in range(n):
            arr[i][j] = next_arr[i][j]

r, c = tuple(map(int, input().split()))
bomb(r - 1, c - 1)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()