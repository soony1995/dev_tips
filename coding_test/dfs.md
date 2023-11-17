# FIFO 
# 재귀 함수, 스택 ( 보통은 재귀함수가 많이 사용되지만 depth가 많아 질수록 stack overflow가 발생할 여지가 있다.)


1. visited 배열을 만들어서 해당 노드를 방문했는 지 체크하자.
   ```python
     visited = [False]*n+1 
   ```
2. 노드를 만드는 방법은 인덱스를 해당 노드의 번호로 부여해서 사용한다.
3. dfs를 호출해서 cnt를 센다.
예시) 
```python
    def dfs(graph, v, visited):
        visited[v] = True
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    n, m = map(int, input().split())  # 정점의 개수, 간선의 개수
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    count = 0  # 연결 노드의 수
    visited = [False] * (n + 1)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1  # dfs 한 번 끝날 때마다 count+1
    print(count)
```
