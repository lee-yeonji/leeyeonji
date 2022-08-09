# 변수 선언 및 입력
n, m = tuple(map(int,input().split()))
list_num = list(map(int, input().split()))
answer = []
curr_ans = 0

def calc_xor():
    curr_ans = 0
    for elem in answer:
        curr_ans ^= elem
    return curr_ans

# n개의 숫자들 중 m개를 고르기
def choose_num(curr_num, cnt):
    global curr_ans
    if curr_num == n:
        if cnt == m:
            curr_ans = max(curr_ans, calc_xor())
        return

    # list_num에 있는 숫자를 선택한 경우 
    answer.append(list_num[curr_num])
    choose_num(curr_num + 1, cnt + 1)
    answer.pop()

    # list_num에 있는 숫자를 선택하지 않은 경우 
    choose_num(curr_num + 1, cnt )

choose_num(0, 0)
print(curr_ans)