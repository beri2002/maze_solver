from collections import deque
from maze import Maze


class BFS:
    @staticmethod
    def bfs(maze, start, goal):
        queue = deque([start])
        came_from = {}
        came_from[start] = None
        
        while queue:
            current_node = queue.popleft()
            
            if current_node == goal:
                break
            
            for next_node in Maze.get_neighbors(current_node, maze):
                if next_node not in came_from:
                    queue.append(next_node)
                    came_from[next_node] = current_node
        
        if goal not in came_from:
            print("Goal not reachable!")
            return []
        
        # Reconstruct path from `came_from` dictionary
        path = []
        node = goal
        while node != start:
            path.append(node)
            node = came_from[node]
        path.append(start)
        path.reverse()
        
        return path
