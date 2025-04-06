from collections import deque

def breadth_first_search(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None

def input_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    for i in range(vertices):
        vertex = input(f"Enter vertex {i+1}: ").strip()
        neighbors = input(f"Enter neighbors of vertex {vertex} (space-separated): ").strip().split()
        graph[vertex] = neighbors
    return graph

def display_graph(graph):
    print("\nGraph:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {' '.join(neighbors)}")

# Main execution
start_node = input("Enter start node: ").strip()
goal_node = input("Enter goal node: ").strip()
graph = input_graph()
display_graph(graph)
result = breadth_first_search(graph, start_node, goal_node)
if result:
    print("Path found:", result)
else:
    print("Path not found!")
