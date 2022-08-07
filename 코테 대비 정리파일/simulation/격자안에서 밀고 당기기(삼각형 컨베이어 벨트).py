# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
fir = list(map(int, input().split()))
sec = list(map(int, input().split()))
thi = list(map(int, input().split()))

for _ in range(t):
    # step 1
    # 왼쪽에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장
    temp = fir[n - 1]

    # step 2
    # 왼쪽에 있는 숫자들을 완성함
    # 벨트를 기준으로 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 아래에서 가져와야 함
    for i in range(n - 1, 0, -1):
        fir[i] = fir[i - 1]
    fir[0] = thi[n - 1]
    
    # step 3
    # 오른쪽에 있는 숫자들을 완성
    # 벨트를 기준으로 마찬가지로 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 이전 단계에서 미리 저장해놨던 temp값을 가져와야 함
    temp2 = sec[n - 1]
    for i in range(n -1, 0, -1):
        sec[i] = sec[i - 1]
    sec[0] = temp

    # step 4
    # 아래에 있는 숫자들을 완성
    # 마찬가지로 벨트를 기준으로 오른쪽에서부터 채워넣어야 하며,
    # 맨 왼쪽 숫자는 이전 단계에서 미리 저장해놨던 temp값을 가져와야 함
    for i in range(n - 1, 0, -1):
        thi[i] = thi[i - 1]
    thi[0] = temp2
    
# 출력
for elem in fir:
    print(elem, end=' ')
print()

for elem in sec:
    print(elem, end=' ')
print()

for elem in thi:
    print(elem, end=' ')
print()