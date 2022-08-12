n = int(input())
visited = [0] * (n + 1)
answer = []

def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

def choose(cnt):
    # 모든 원소를 선택했을 때, 해당 순열을 출력
    if cnt == n+1:
        print_answer()
        return

    # 앞에서부터 하나씩 원소를 선택
    for i in range(1, n+1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)

        choose(cnt + 1)

        visited[i] = False
        answer.pop()

choose(1)