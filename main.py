from maze_loader import read_maze_file, save_maze_file_with_path, find_start_and_goal
from a_star import a_star
import os

def main():
    """
    The main function that runs the maze solver.
    
    This function prompts the user to enter the path to a maze image file. It checks if the file exists and if it is a valid image file. If the file is valid, it reads the maze image data and converts it into a 2D array. It then finds the start and goal positions on the edges of the maze and runs the A* algorithm to find the shortest path from the start to the goal. Finally, it saves the maze image with the path highlighted.
    
    Parameters:
    None
    
    Returns:
    None
    """
    while True:
        maze_file_path = input("Please enter the path to the maze.png file: ")
        if os.path.isfile(maze_file_path):
            break
        print("Invalid path. Please try again.")
    
    maze_data = read_maze_file(maze_file_path)

    print(f"Loaded maze file: {maze_file_path}")
    
    if maze_data is None:
        return
    
    # Convert maze_data to a 2D array (assuming grayscale maze image)
    maze_array = []
    width, height = maze_data.size
    for y in range(height):
        row = []
        for x in range(width):
            pixel = maze_data.getpixel((x, y))
            # print(pixel)
            if pixel == 0:  # Assuming black pixels represent walls
                row.append('#')
            else:
                row.append('.')
        maze_array.append(row)
    
    # print(maze_array)
    # Find start and goal positions on the edges
    start, goal = find_start_and_goal(maze_data)
    
    if start is None or goal is None:
        print("Start or goal position not found on the edges of the maze.")
        return
    
    # Run A* algorithm to find the path
    path = a_star(maze_array, start, goal)
    
    save_maze_file_with_path(maze_data, maze_file_path, path)

if __name__ == "__main__":
    main()
