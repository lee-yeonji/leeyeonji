# 변수 선언 및 입력
vertices_num, edges_num = tuple(map(int, input().split()))

# index를 1번 부터 사용하기 위해 edges_num + 1 만큼 할당
graph = [[] for _ in range(vertices_num + 1)]

for _ in range(edges_num):
    v1, v2 = map(int, input().split())
    # 각 정점에 대한 간선을 각각 저장
    graph[v1].append(v2) # v1 -> v2
    graph[v2].append(v1) # v2 -> v1

# 방문 배열
visited = [False for _ in range(vertices_num + 1)]

# dfs 탐색
def dfs(vertex):
    # vertex에 연결된 정점 탐색
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v) # 재귀 함수 호출

start_vertex = 1
visited[start_vertex] = True
dfs(start_vertex)

vertex_cnt = 0
for i in range(1, vertices_num + 1): # i번 정점을 갈 수 있을 때
   if visited[i]:
       vertex_cnt += 1
print(vertex_cnt - 1)