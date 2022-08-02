# 변수 선언 및 입력
words = input()
x, y = 0, 0
dir_num = 0 

# 북, 동, 남, 서 순으로 dx, dy를 정의
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

dirs = {"E":0, "W":1, "S":2, "N":3}

sec = 0 # 이동시간

n = len(words)
# 움직이는 것을 진행
for c_dir in words:
    sec += 1
    # 반시계방향 90' 회전
    if c_dir == 'L':
      dir_num = (dir_num - 1 + 4) % 4
    # 시계방향 90' 회전
    elif c_dir == 'R':
      dir_num = (dir_num + 1) % 4
    # 직진
    else:
      x, y = x + dxs[dir_num], y + dys[dir_num]

# 시작점으로 돌아왔을 때
    if x == 0 and  y == 0:
      break
if x == 0 and y == 0:
    print(sec)
else:
    print(-1)
