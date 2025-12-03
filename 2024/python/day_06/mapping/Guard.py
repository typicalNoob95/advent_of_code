class Guard:
    def __init__(self, x_position: int, y_position: int, orientation_char: str):
        self.x_position = x_position
        self.y_position = y_position
        self.orientation = self.determine_orientation(orientation_char)
        self.position_visited = {
            (self.x_position, self.y_position): True
        }
        self.position_visited_with_orientation = {
            (self.x_position, self.y_position, self.orientation): True
        }
        self.position_turned = {}
        self.in_a_loop = False

    def determine_orientation(self, orientation_char: str) -> str:
        orientation = {
            "^": "UP",
            ">": "RIGHT",
            "<": "LEFT",
            "v": "DOWN"
        }

        return orientation[orientation_char]

    def rotate(self):
        if self.orientation == "UP":
            self.orientation = "RIGHT"
        elif self.orientation == "RIGHT":
            self.orientation = "DOWN"
        elif self.orientation == "DOWN":
            self.orientation = "LEFT"
        else:
            self.orientation = "UP"

        self.add_position_turned()

    def find_next_position(self) -> (int, int):
        directions = {
            "UP": (0, -1),
            "RIGHT": (1, 0),
            "DOWN": (0, 1),
            "LEFT": (-1, 0)
        }

        actual_direction = directions[self.orientation]
        return self.x_position + actual_direction[0], self.y_position + actual_direction[1]

    def add_position_visited(self) -> None:
        self.position_visited[self.x_position, self.y_position] = True
        self.add_position_visited_with_orientation()

    def add_position_visited_with_orientation(self) -> None:
        if (self.x_position, self.y_position, self.orientation) in self.position_visited_with_orientation.keys():
            self.in_a_loop = True
        else:
            self.position_visited_with_orientation[self.x_position, self.y_position, self.orientation] = True

    def add_position_turned(self) -> None:
        """
        Adds a position where the guard turned.  If the guard has already turned here, then we set the loop flag to true.
        :return: None
        """
        if (self.x_position, self.y_position, self.orientation) not in self.position_turned.keys():
            self.position_turned[(self.x_position, self.y_position, self.orientation)] = True
            return
        #print(f"Position where turning in a loop x: {self.x_position}, y: {self.y_position}, orientation: {self.orientation}")
        self.in_a_loop = True