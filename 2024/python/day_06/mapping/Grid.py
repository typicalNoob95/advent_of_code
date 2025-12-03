from mapping.Guard import Guard
from mapping.Obstacle import Obstacle

class Grid:
    def __init__(self, filepath: str):
        self.width = 0
        self.length = 0
        self.guard = None
        self.number_of_guard_moves = 0
        self.obstacles = []
        self.obstructions_for_loop = 0

        with open(filepath) as file:
            for line in file.readlines():
                self.length += 1
                line = line.replace("\n", "")
                self.width = len(line)
                for i in range(self.width):
                    if line[i] == "#":
                        self.obstacles.append(Obstacle(i , self.length - 1))
                    elif line[i] in ["^", "v", "<", ">"]:
                        self.guard = Guard(i, self.length - 1, line[i])

    def guard_position_is_valid(self):
        if self.guard.x_position < 0 or self.guard.x_position >= self.width:
            return False
        if self.guard.y_position < 0 or self.guard.y_position >= self.length:
            return False
        return True

    def move_guard(self):
        next_position = self.guard.find_next_position()

        # Check if next move is blocked by an obstacle
        for obstacle in self.obstacles:
            if obstacle.is_blocking(next_position):
                self.guard.rotate()
                next_position = self.guard.find_next_position()

        self.guard.x_position = next_position[0]
        self.guard.y_position = next_position[1]
        if self.guard_position_is_valid():
            self.guard.add_position_visited()
        if self.guard.in_a_loop:
            self.obstructions_for_loop += 1

        # Update the number of guard moves
        self.number_of_guard_moves += 1