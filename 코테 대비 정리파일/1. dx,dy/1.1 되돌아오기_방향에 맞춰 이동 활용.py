# 변수 선언 및 입력
n = int(input())

# 시작 위치를 기록
x, y = 0, 0
sec = 0 # 이동시간 
# 동, 서, 남, 북 순으로 dxs, dys 를 정의
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

# 각 방향에 맞는 번호를 붙여줌
dirs = {"E":0, "W":1, "S":2, "N":3}

# 움직이는 것을 진행
for i in range(n):
    # input().split() # ["N", "3"]
    c_dir, dist = tuple(input().split())
    dist = int(dist)
    dir_num = dirs[c_dir]
    
    for _ in range(dist):
        x += dx[dir_num]
        y += dy[dir_num]
        sec += 1 # 이동한 시간을 기록

        # 시작 위치에 도달했다면 종료
        if x == 0 and  y == 0:
            break
    if x == 0 and y == 0:
        break
if x == 0 and y == 0:
    print(sec)
else:
    print(-1)
