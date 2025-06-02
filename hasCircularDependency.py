from typing import List

def hasCircularDependency(n: int, edges: List[List[int]]) -> bool:
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)

    visited = [False] * n
    in_stack = [False] * n

    def dfs(node):
        visited[node] = True
        in_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif in_stack[neighbor]:
                return True  # cycle detected

        in_stack[node] = False
        return False

    for i in range(n):
        if not visited[i]:
            if dfs(i):
                return True

    return False
if __name__ == "__main__":
    n1 = 4
    edges1 = [[0, 1], [1, 2], [2, 3]]
    print(hasCircularDependency(n1, edges1)) 

    # Example 2
    n2 = 4
    edges2 = [[0, 1], [1, 2], [2, 0]]
    print(hasCircularDependency(n2, edges2))  # Output: True
