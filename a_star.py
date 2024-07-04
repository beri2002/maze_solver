import heapq

def heuristic(node, goal):
    # Manhattan distance heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def get_neighbors(node, maze):
    """
    Returns a list of neighboring nodes of the given node in the maze.
    
    Args:
    - node: A tuple representing the coordinates of the node.
    - maze: A 2D list representing the maze.
    
    Returns:
    - A list of neighboring nodes.
    """
    neighbors = []
    
    # Possible movements: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dir in directions:
        # Calculate the coordinates of the neighbor node
        neighbor = (node[0] + dir[0], node[1] + dir[1])
        
        # Check if the neighbor node is within the maze boundaries and not a wall
        if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != '#':
            neighbors.append(neighbor)
    
    return neighbors

def a_star(maze, start, goal):
    """
    A* pathfinding algorithm implementation.
    
    Args:
    - maze: A 2D list representing the maze.
    - start: A tuple representing the coordinates of the start position.
    - goal: A tuple representing the coordinates of the goal position.
    
    Returns:
    - A list representing the path from the start to the goal.
    """
    # Initialize the open set, came from dictionary, g-score dictionary,
    # and f-score dictionary
    open_set = set([start])
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    # Explore the maze until the goal is found
    while open_set:
        # Find the node in the open set with the lowest f-score
        current = min(open_set, key=lambda x: f_score[x])

        # If the current node is the goal, construct the path and return it
        if current == goal:
            break

        # Remove the current node from the open set
        open_set.remove(current)

        # Explore the neighboring nodes
        for neighbor in get_neighbors(current, maze):
            # Calculate the tentative g-score
            tentative_g_score = g_score[current] + 1

            # If the neighbor is not in the open set or the tentative g-score
            # is better than the current g-score, update the g-score and f-score
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                # If the neighbor is not in the open set, add it
                if neighbor not in open_set:
                    open_set.add(neighbor)

    # If the goal is not reachable, print a message and return an empty list
    if goal not in came_from:
        print("Goal not reachable!")
        return []

    # Construct the path from the came from dictionary
    path = []
    node = goal
    while node in came_from:
        path.append(node)
        node = came_from[node]

    # Add the start position to the path and reverse it
    path.append(start)
    path.reverse()

    # Print the path
    print("Path:")
    for i, node in enumerate(path):
        print(f"{i}: {node}")
    
    # Return the path
    return path
