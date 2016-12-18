from robots import time_robots, get_next_move, has_to_press, initialise_positions


# main function
def test_time_robots():
    assert time_robots(["B2", "B1"], ["B", "O"]) == 4


def test_time_robots_case_2():
    assert time_robots(["O2", "B1", "B2", "O1"], ["B", "O"]) == 6


# get_next_move
def test_get_next_move_is_forward():
    assert get_next_move("B", ["B2"], 0, 1) == 2


def test_get_next_move_is_backwards():
    assert get_next_move("B", ["B2", "B1"], 1, 2) == 1


def test_get_next_move_is_no_move():
    assert get_next_move("O", ["B2", "B1"], 1, 1) == 1


# has_to_press
def test_has_to_press_true():
    assert has_to_press("B", "B2", 2) == True


def test_has_to_press_false_when_not_correct_robot():
    assert has_to_press("O", "B2", 2) == False


def test_has_to_press_false_when_not_matching_sequence_position():
    assert has_to_press("B", "B2", 1) == False


# initialise_positions
def test_initialise_positions():
    assert initialise_positions(["B", "O"]) == {"B": 1, "O": 1}
