from PIL import Image, ImageDraw
import os



def read_maze_file(file_path):
    """
    Reads a maze image file from the given file path.

    Args:
    - file_path: The path to the maze image file.

    Returns:
    - The maze image data as a PIL.Image.Image object if the file is successfully read.
    - None if there is an error reading the file.
    """
    try:
        # Open the maze image file using PIL
        maze_data = Image.open(file_path)
        return maze_data
    except IOError:
        # Print an error message if the file cannot be opened
        print(f"Unable to open file {file_path}.")
        return None

def save_maze_file_with_path(maze_data, file_path, path):
    """
    Saves the maze image with the given path highlighted.

    Args:
    - maze_data: A PIL.Image.Image object representing the maze.
    - file_path: The path to the maze image file.
    - path: A list of tuples representing the coordinates of the nodes in the path.
    """
    # Check if the maze_data is of type PIL.Image.Image
    if not isinstance(maze_data, Image.Image):
        print("Invalid maze_data format. Expected PIL.Image.Image object.")
        return
    
    # Create a copy of the maze_data and create a draw object
    maze_with_path = maze_data.copy()
    draw = ImageDraw.Draw(maze_with_path)
    
    # Set the color for the path
    path_color = (120, 20, 100)  # Red color for the path
    
    # Draw lines between consecutive nodes in the path
    for i in range(len(path) - 1):
        node1 = path[i]
        node2 = path[i + 1]
        draw.line([(node1[1], node1[0]), (node2[1], node2[0])], fill=path_color, width=1)
    
    # Create the output file path by replacing "mazes" with "solved"
    output_file = file_path.replace("mazes", "solved")
    
    # Create the output directories if they don't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Save the maze image with the path highlighted
    maze_with_path.save(output_file)
    print(f"Saved maze with path to {output_file}")

def find_start_and_goal(maze_data):
    """
    Finds the start and goal positions on the edges of the maze.

    Args:
    - maze_data: A PIL.Image.Image object representing the maze.

    Returns:
    - A tuple containing the start position and goal position.
    """
    # Get the dimensions of the maze image
    width, height = maze_data.size

    # Initialize start and goal positions to None
    start = None
    goal = None

    # Check top and bottom edges
    for x in range(width):
        # If the top edge pixel is not a wall, set start to the corresponding coordinates
        if maze_data.getpixel((x, 0)) != 0:  # Top edge
            start = (0, x)
        # If the bottom edge pixel is not a wall, set goal to the corresponding coordinates
        if maze_data.getpixel((x, height - 1)) != 0:  # Bottom edge
            goal = (height - 1, x)

    # Check left and right edges
    for y in range(height):
        # If the left edge pixel is not a wall, set start to the corresponding coordinates
        if maze_data.getpixel((0, y)) != 0:  # Left edge
            start = (y, 0)
        # If the right edge pixel is not a wall, set goal to the corresponding coordinates
        if maze_data.getpixel((width - 1, y)) != 0:  # Right edge
            goal = (y, width - 1)

    return start, goal
