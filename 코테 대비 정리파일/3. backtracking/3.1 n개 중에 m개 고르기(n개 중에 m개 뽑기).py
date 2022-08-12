# 변수 선언 및 입력
n, m = tuple(map(int,input().split()))
combination=[]

# 방문한 원소들 출력
def print_combination():
    for elem in combination:
        print(elem, end= ' ')
    print()

def find_combination(curr_num, cnt):
    # n개의 숫자를 모두 탐색했으면 더 이상 탐색 안함
    if curr_num == n+1:
        # 탐색하는 과정에서 m개의 숫자를 뽑은 경우 답 출력
        if cnt == m:
            print_combination()
        return

    # curr_num에 해당하는 숫자를 사용했을 때의 경우 탐색
    combination.append(curr_num)
    find_combination(curr_num+1,cnt+1)
    combination.pop()

    # curr_num에 해당하는 숫자를 사용하지 않았을 때의 경우 탐색
    find_combination(curr_num+1,cnt)

find_combination(1, 0)