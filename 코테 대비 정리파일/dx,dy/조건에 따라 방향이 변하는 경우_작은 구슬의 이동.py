# 변수 선언 및 입력
n, t = tuple(map(int, input().split())) # 격자의 크기를 나타내는 n과 시간 t
x, y, c_dir = tuple(input().split())

# 각 알파벳 별 방향 번호를 설정
mapper = { 'R' : 0, 'D' : 1, 'U' : 2, 'L' : 3 }

x, y, move_dir = int(x)-1, int(y)-1, mapper[c_dir]

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n 

# 시뮬레이션 진행
for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    # 범위 안에 들어온다면 그대로 진행
    if in_range(nx, ny):
        x, y = nx, ny
    # 벽에 부딪힌다면, 방향을 바꿔줌
    else:
        move_dir = 3 - move_dir
    '''
    방향이 뒤집어지는 문제에서 0번과 3번이, 1번과 2번이 반대 방향이 되도록
    dx, dy를 설정해주면,
    3에서 현재 방향을 뺀 것 만드로 방향이 뒤집어지는 효과를 만들어줌
    '''

print(x+1, y+1)