class Obstacle:
    def __init__(self, x_position: int, y_position: int):
        self.x_position = x_position
        self.y_position = y_position

    def is_blocking(self, next_position):
        return self.x_position == next_position[0] and self.y_position == next_position[1]