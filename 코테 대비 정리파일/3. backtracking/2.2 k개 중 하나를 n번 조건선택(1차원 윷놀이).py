n, m, k = tuple(map(int, input().split())) # 턴의 수, 윷놀이 판, 말의 수 
turnNum = list(map(int, input().split())) # 앞으로 나아가는 숫자 모음 
nowNum = [ 1 for _ in range(k)]
ans = 0

def find_max(cnt, score):
    global ans
    ans = max(ans, score)

    # 지금까지의 최대 점수인 ans보다 더 좋은 점수가 절대 나올 수 없는 경우, 더 이상 탐색 진행 안함
    # 앞으로 최대로 더 얻을 수 있는 이상적인 점수 : min(k - score, n - cnt)임을 이용 
    if score + min(k - score, n - cnt) <= ans:
        return
    if cnt == n:
        return
    for i in range(k):
        # 이미 m번 칸에 도달한 말은 더 이상 선택하지 않음
        if nowNum[i] >= m:
            continue
        
        nowNum[i] += turnNum[cnt] # 말을 바로 움직여줌
        new_score = score + 1 if nowNum[i] >= m else score
        find_max(cnt+1, new_score)
        nowNum[i] -= turnNum[cnt]  # 퇴각시 말을 제자리로 돌려놓음

find_max(0, 0)
print(ans)