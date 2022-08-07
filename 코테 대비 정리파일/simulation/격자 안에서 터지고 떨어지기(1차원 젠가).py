n = int(input())
arr = [int(input()) for _ in range(n)]
rest_block_cnt = n # 남아있는 블록 개수

# 입력 배열에서 지우고자 하는 부분 수열 삭제
def cut_array(s, e): # start ~ end 인덱스
    global rest_block_cnt
    temp = []

    # 구간 외의 부분만 temp 배열에 순서대로 저장
    for i in range(rest_block_cnt):
        if not (s <= i <= e):
            temp.append(arr[i])
    
    # temp 배열을 다시 arr 배열로 옮겨줌
    rest_block_cnt = len(temp)
    for i in range(rest_block_cnt):
        arr[i] = temp[i]

# 두 번에 걸쳐 지우는 과정 반복
for _ in range(2):
    start, end = tuple(map(int, input().split()))
    # 위에서부터 start~end 구간 삭제
    cut_array(start-1, end-1) # start~end번 인덱스 제거해주는 함수

# 출력
print(rest_block_cnt)
for i in range(rest_block_cnt):
    print(arr[i])