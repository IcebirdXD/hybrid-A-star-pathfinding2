from math import pi


class TestCase:
    """ Provide some test cases for a 10x10 map. """

    def __init__(self):

        #self.start_pos = [4.6, 2.4, 0]
        #self.end_pos = [1.6, 8, -pi/2]

        #self.start_pos2 = [4, 4, 0]
        #self.end_pos2 = [4, 8, 1.2*pi]

        #self.obs = [
        #    [2, 3, 6, 0.1],
        #    [2, 3, 0.1, 1.5],
        #    [4.3, 0, 0.1, 1.8],
        #    [6.5, 1.5, 0.1, 1.5],
        #    [0, 6, 3.5, 0.1],
        #    [5, 6, 5, 0.1]
        #]
        # Case Turtlebot3 - 4 rooms
        self.start_pos = [2, 2, 0]
        self.end_pos = [2, 17, 3*pi/4]

        self.start_pos2 = [4, 4, 0]
        self.end_pos2 = [4, 8, -pi]

        self.obs = [
            [0, 6, 6, 0.1],
            [6, 0, 0.1, 4],
            [0, 14, 4, 0.1],
            [6, 14, 0.1, 6],
            [14, 14, 6, 0.1],
            [14, 16, 0.1, 4],            
            [16, 6, 4, 0.1],
            [14, 0, 0.1, 6],
        ]


class TestCase2:
    """ Provide some test cases for a 10x10 map. """

    def __init__(self):

        self.start_pos = [0.2, 0.2, 0]
        self.end_pos = [0.8, 1, 0]

        # [x_position, y_position, x_width, y_width]
        self.obs = [
            # [0.25, 1.1, 0.5, 0.2],   # box_wall_right
            [0.25, 1.1, 0.5, 0.2],   # box_wall_left
            [1.7, 0.8, 0.5, 0.2],    # box_wp1
            [3.41, 0.8, 0.5, 0.2],   # box_wp2
            [1.3, 1.85, 0.2, 0.4],   # random_1
            [2.3, 1.85, 0.4, 0.4],   # random_2
            [3.81, 1.95, 0.4, 0.2],  # box_wp6
        ]