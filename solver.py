from maze import Maze
from algos.a_star import AStar
from algos.bfs import BFS
from algos.dfs import DFS

def main():
    maze_file_path = "/home/beri/Documents/maze_solver/mazes/normal.png"
    maze = Maze(maze_file_path)
    
    if maze.maze_data is None:
        return
    
    print("Loaded maze file:", maze_file_path)
    
    if maze.start is None or maze.goal is None:
        print("Start or goal position not found on the edges of the maze.")
        return
    
    print("Start position:", maze.start)
    print("Goal position:", maze.goal)

    # Prompt user to choose an algorithm
    print("Choose an algorithm to solve the maze:")
    print("1. A*")
    print("2. BFS")
    print("3. DFS")
    choice = input("Enter the number of the algorithm: ")
    
    algorithm_name = ""
    if choice == '1':
        path = AStar.a_star(maze.maze_array, maze.start, maze.goal)
        algorithm_name = "AStar"
    elif choice == '2':
        path = BFS.bfs(maze.maze_array, maze.start, maze.goal)
        algorithm_name = "BFS"
    elif choice == '3':
        path = DFS.dfs(maze.maze_array, maze.start, maze.goal)
        algorithm_name = "DFS"
    else:
        print("Invalid choice!")
        return
    
    if not path:
        print("No path found from start to goal.")
        return
    
    maze.save_maze_file_with_path(path, algorithm_name)


if __name__ == "__main__":
    main()
