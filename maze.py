import os
from PIL import Image, ImageDraw

class Maze:
    def __init__(self, file_path):
        self.file_path = file_path
        self.maze_data = self.read_maze_file(file_path)
        self.maze_array = self.convert_to_array(self.maze_data)
        self.start, self.goal = self.find_start_and_goal(self.maze_data)

    def read_maze_file(self, file_path):
        try:
            maze_data = Image.open(file_path)
            return maze_data
        except IOError:
            print(f"Unable to open file {file_path}.")
            return None

    def convert_to_array(self, maze_data):
        maze_array = []
        width, height = maze_data.size
        for y in range(height):
            row = []
            for x in range(width):
                pixel = maze_data.getpixel((x, y))
                if pixel == 0:  # Assuming black pixels represent walls
                    row.append('#')
                else:
                    row.append('.')
            maze_array.append(row)
        return maze_array

    def find_start_and_goal(self, maze_data):
        width, height = maze_data.size
        start = None
        goal = None

        # Check top and bottom edges
        for x in range(width):
            if maze_data.getpixel((x, 0)) != 0:  # Top edge
                start = (0, x)
            if maze_data.getpixel((x, height - 1)) != 0:  # Bottom edge
                goal = (height - 1, x)

        # Check left and right edges
        for y in range(height):
            if maze_data.getpixel((0, y)) != 0:  # Left edge
                start = (y, 0)
            if maze_data.getpixel((width - 1, y)) != 0:  # Right edge
                goal = (y, width - 1)

        return start, goal

    @staticmethod
    def get_neighbors(node, maze):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible movements: up, down, left, right
        
        for dir in directions:
            neighbor = (node[0] + dir[0], node[1] + dir[1])
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] != '#':
                neighbors.append(neighbor)
        
        return neighbors

    def save_maze_file_with_path(self, path, algorithm_name, line_width=1):
        if not isinstance(self.maze_data, Image.Image):
            print("Invalid maze_data format. Expected PIL.Image.Image object.")
            return
        
        # Convert to RGB mode
        maze_with_path = self.maze_data.convert('RGB')
        draw = ImageDraw.Draw(maze_with_path)

        for i in range(len(path) - 1):
            node1 = path[i]
            node2 = path[i + 1]
            # Calculate the color gradient from red to blue
            ratio = i / (len(path) - 1)
            red = int(255 * (1 - ratio))
            blue = int(255 * ratio)
            path_color = (red, 0, blue)
            draw.line([(node1[1], node1[0]), (node2[1], node2[0])], fill=path_color, width=line_width)
        
        # Replace "mazes" with "solved" and add algorithm name to the file path
        output_dir = self.file_path.replace("mazes", "solved")
        output_file = os.path.splitext(output_dir)[0] + f"_{algorithm_name}.png"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Create directories if they don't exist
        maze_with_path.save(output_file)
        print(f"Saved maze with path to {output_file}")
