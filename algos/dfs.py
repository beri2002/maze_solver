from maze import Maze

class DFS:
    @staticmethod
    def dfs(maze, start, goal):
        stack = [start]
        came_from = {}
        came_from[start] = None
        
        while stack:
            current_node = stack.pop()
            
            if current_node == goal:
                break
            
            for next_node in Maze.get_neighbors(current_node, maze):
                if next_node not in came_from:
                    stack.append(next_node)
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
