# 변수 선언 및 입력
commands = input() # LF
dir_num = 3
x, y = 0, 0

# 동, 남, 서, 북 순으로 dx, dy를 정의
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# 움직이는 것을 진행
for command in commands:
  # 반시계방향 90' 회전
  if command == 'L':
      dir_num = (dir_num - 1 + 4) % 4
  # 시계방향 90' 회전
  elif command == 'R':
      dir_num = (dir_num + 1) % 4
  # 직진
  else:
      x, y = x + dx[dir_num], y + dy[dir_num]
    
print(x, y)