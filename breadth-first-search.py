from collections import deque

def bfs(graph, start):
    visited = set([1, 2, 3])
    queue = deque([start])
    visited.add(start)
    
    while queue:
        current_node = queue.popleft()
        print(f"\nУзел: {current_node}")
        print(f"Посещенные: {visited}")
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

        print(f"Очередь после: {queue}")
        print(f"Посещенные после: {queue}")

graph = {
    1: [1, 2, 3, 3],
    2: [1, 2, 5],
    3: [2, 8, 11],
    5: [8],
    8: [11],
    11: []
}

bfs(graph, 5)
