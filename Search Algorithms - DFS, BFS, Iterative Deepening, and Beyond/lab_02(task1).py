from collections import deque

def dfs(graph, current_node, visited_nodes=None):
    if visited_nodes is None:
        visited_nodes = set()
    visited_nodes.add(current_node)
    print(current_node, end=' ')
    for neighbor in graph[current_node]:
        if neighbor not in visited_nodes:
            dfs(graph, neighbor, visited_nodes)

def bfs(graph, starting_node):
    visited_nodes = set()
    queue = deque()
    queue.append(starting_node)
    while queue:
        current_node = queue.popleft()
        print(current_node, end=' ')
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                visited_nodes.add(neighbor)

def iterative_deepening_dfs(graph, root_node, target_node):
    depth = 0
    while True:
        result = depth_limited_dfs(graph, root_node, target_node, depth)
        if result is not None:
            return result, depth
        depth += 1

def depth_limited_dfs(graph, current_node, target_node, depth):
    if current_node == target_node:
        return current_node
    if depth == 0:
        return None
    for neighbor in graph[current_node]:
        result = depth_limited_dfs(graph, neighbor, target_node, depth - 1)
        if result is not None:
            return result
    return None

def depth_limited_search(graph, current_node, limit, visited_nodes):
    if limit == 0:
        print(current_node, end=' ')
        return True
    if current_node not in visited_nodes:
        visited_nodes.add(current_node)
        for neighbor in graph[current_node]:
            if depth_limited_search(graph, neighbor, limit - 1, visited_nodes):
                return True
        visited_nodes.remove(current_node)
    return False

def iterative_dls(graph, start_node, max_depth):
    for limit in range(max_depth):
        visited_nodes = set()
        if depth_limited_search(graph, start_node, limit, visited_nodes):
            return

def main():
    adjacency_list = [[2, 1, 3], [1, 7], [], [], [3, 1, 3, 6], [2, 0, 3], [1, 4], [1, 5]]
    bfs(adjacency_list, 0)
    print()
    dfs(adjacency_list, 0)
    print()

    graph_structure = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G'],
        'E': [],
        'F': [],
        'G': []
    }

    start_node = 'A'
    target_node = 'B'

    found_node, depth_level = iterative_deepening_dfs(graph_structure, start_node, target_node)
    print(found_node, depth_level)

main()
