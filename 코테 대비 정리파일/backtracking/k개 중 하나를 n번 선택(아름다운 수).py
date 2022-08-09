# 변수 선언 및 입력
n = int(input())
ans = 0
answer = list()

# 선택된 원소들을 출력
def is_beautiful(n, seq):
    # 연달아 같은 숫자가 나오는 시작 위치를 잡음
    i = 0
    while i < n:
        # 만약 연속해서 해당 숫자가 나올 수 없으면 아름다운 수가 아님
        if i + answer[i] - 1 >= n:
            return False
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인
        # 하나라도 다른 숫자가 있으면 아름다운 수가 아님
        for j in range(i, i + answer[i]):
            if answer[j] != answer[i]:
                return False
        
        i += answer[i]

    return True

def cnt_beautiful_seq(n, cnt, seq):
    if cnt == n:
        if is_beautiful(n, seq):
            return 1
        return 0
    
    can_cnt = 0
    for i in range(1, 5):
        answer.append(i)
        can_cnt += cnt_beautiful_seq(n, cnt + 1, seq)
        answer.pop()

    return can_cnt

def solution(sol_n):
    seq = list()
    return cnt_beautiful_seq(sol_n, 0, seq)


print(solution(n))