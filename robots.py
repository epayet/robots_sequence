def time_robots(sequence, robots):
    current_sequence_index = 0
    min_time = 0
    positions = initialise_positions(robots)
    button_pressed = False

    while current_sequence_index < len(sequence):
        print("\nCurrent sequence:", sequence[current_sequence_index])

        for robot in robots:
            next_move = get_next_move(robot, sequence, current_sequence_index, positions[robot])
            if has_to_press(robot, sequence[current_sequence_index], positions[robot]):
                button_pressed = True
                print(robot, "presses the button, position:", positions[robot])
            elif next_move > positions[robot]:
                positions[robot] += 1
                print(robot, "moves forward, new position:", positions[robot])
            elif next_move < positions[robot]:
                positions[robot] -= 1
                print(robot, "moves backward, new position:", positions[robot])
            else:
                print(robot, "waits, position:", positions[robot])

        if button_pressed:
            current_sequence_index += 1
            button_pressed = False

        min_time += 1

    return min_time


def get_next_move(robot, sequence, current_sequence_index, robot_position):
    for i in range(current_sequence_index, len(sequence)):
        current_sequence_robot = sequence[i][0]
        current_sequence_position = int(sequence[i][1])
        if robot == current_sequence_robot:
            return current_sequence_position

    return robot_position


def has_to_press(robot, current_sequence, robot_position):
    current_sequence_robot = current_sequence[0]
    current_sequence_position = int(current_sequence[1])
    return robot == current_sequence_robot and robot_position == current_sequence_position


def initialise_positions(robots):
    positions = {}
    for robot in robots:
        positions[robot] = 1
    return positions

