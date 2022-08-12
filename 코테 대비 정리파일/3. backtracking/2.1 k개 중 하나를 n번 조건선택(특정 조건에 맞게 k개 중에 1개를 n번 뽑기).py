# 변수 선언 및 입력
k, n = tuple(map(int, input().split()))
answer = []

# 선택된 원소들을 출력
def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

def find_permutation(curr_num):
    # n개를 모두 뽑은 경우 답을 출력
    if curr_num == n:
        print_answer()
        return
    
    # 1부터 k까지의 각 숫자가 뽑혔을 경우를 탐색
    for i in range(1, k + 1):
        if curr_num >= 2 and i == answer[-1] and i == answer[-2]:
            continue
        else:
            answer.append(i)
            find_permutation(curr_num + 1)
            answer.pop()

find_permutation(0)