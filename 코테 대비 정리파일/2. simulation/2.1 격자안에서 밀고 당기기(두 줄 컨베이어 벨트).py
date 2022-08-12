# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(t):
    # step 1
    # 위에서 가장 오른쪽에 있는 숫자를 temp값에 따로 저장
    temp = arr1[n-1]

    # step2
    for i in range(n-1, 0, -1):
        arr1[i] = arr1[i-1]
    arr1[0] = arr2[n-1]

    for i in range(n-1, 0, -1):
        arr2[i] = arr2[i-1] 
    arr2[0] = temp

# 출력
for elem in arr1:
    print(elem, end=' ')
print()
for elem in arr2:
    print(elem, end=' ')