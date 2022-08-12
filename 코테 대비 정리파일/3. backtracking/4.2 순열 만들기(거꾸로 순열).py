# 변수 선언 및 입력
n = int(input())
visited = [0] * (n + 1)
answer = []

# 모든 원소를 선택했을 때, 해당 순열을 출력
def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

def choose(curr_num):
    if curr_num == n+1:
        print_answer()
        return
    # 뒤에서부터 하나씩 원소를 선택 
    for i in range(n, 0, -1):
        if visited[i]:
            continue
            
        visited[i] = True
        answer.append(i)

        choose(curr_num + 1)
        
        visited[i] = False
        answer.pop()
        
choose(1)