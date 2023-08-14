graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
visisted = []
queue = []
def bfs(visited,graph,start_node):
    visited.append(start_node)
    queue.append(start_node)
    while queue:
        s = queue.pop(0)
        print("S " + s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
bfs(visisted,graph,"A")
