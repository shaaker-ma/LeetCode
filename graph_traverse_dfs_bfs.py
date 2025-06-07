from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
visited = set()

def dfs(node, visited, graph):
  stack = deque([node])
  while stack:
    current_node = stack.pop()
    if(current_node not in visited):
      visited.add(current_node)
      print(current_node)
      for neighbor in graph[current_node]:
        if neighbor not in visited:
          stack.append(neighbor)

def bfs(node, visited, graph):
  queue = deque([node])
  while(queue):
    current_node = queue.popleft()
    if(current_node not in visited):
      visited.add(current_node)
      print(current_node)
      for neighbor in graph[current_node]:
        queue.append(neighbor)

dfs('A', set(), graph)
print("---")
bfs('A', set(), graph)