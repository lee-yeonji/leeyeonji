# 변수 선언 및 입력
n = int(input())
x, y = 0, 0

# 움직이는 것을 진행
for i in range(n):
    # input().split() # ["N", "3"]
    c_dir, dist = tuple(input().split())
    dist = int(dist)

    # 동, 남, 서, 북 순으로 dx, dy를 정의
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    if c_dir == "N":
        dir_num = 3
    elif c_dir == "E":
        dir_num = 0
    elif c_dir == "S":
        dir_num = 1
    else:
        dir_num = 2
    
    # 주어진 방향대로 dist 거리만큼 이동했을 경우의 위치를 구해줌
    x, y = x + dx[dir_num]*dist , y + dy[dir_num]*dist

print(x, y)