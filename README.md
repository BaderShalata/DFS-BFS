These algorithms are pretty basic.
DFS:
Depth first search, I created a graph using dictionary, then I created a set so we dont have any duplicates, a method called dfs, that accepts arguemnts visisted,graph, node.
This algorithm runs recursively as the dfs function is called inside the for loop if the neighbour of the node is not in visisted set.
BFS:
Breadth first search, created a graph using dictionary, then I created a queue list and visited list, a while loop for the queue which eventually runs for each node because its popping index 0 and then calling it on graph[index[0]], which means it will check each node.
