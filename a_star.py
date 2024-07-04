import heapq
from maze import Maze

class AStar:
    @staticmethod
    def heuristic(node, goal):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    @staticmethod
    def a_star(maze, start, goal):
        open_list = []
        heapq.heappush(open_list, (0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0
        
        while open_list:
            current_cost, current_node = heapq.heappop(open_list)
            
            if current_node == goal:
                break
            
            for next_node in Maze.get_neighbors(current_node, maze):
                new_cost = cost_so_far[current_node] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + AStar.heuristic(next_node, goal)
                    heapq.heappush(open_list, (priority, next_node))
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
