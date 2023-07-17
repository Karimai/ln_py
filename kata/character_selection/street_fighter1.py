def next_pos(curr_row, curr_col, move: str):
    match move:
        case "up":
            curr_row = max(curr_row - 1, 0)
        case "down":
            curr_row = min(curr_row + 1, 1)
        case "right":
            curr_col = curr_col + 1 if curr_col != 5 else 0
        case "left":
            curr_col = curr_col - 1 if curr_col else 5
    return curr_row, curr_col


def street_fighter_selection(fighters, initial_position, moves):
    curr_row, curr_col = initial_position
    res = []
    for move in moves:
        curr_row, curr_col = next_pos(curr_row, curr_col, move)
        res.append(fighters[curr_row][curr_col])
    return res


def test_street_fighter_selection():
    fighters = [
        ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
        ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
    ]
    # moves = []
    # solution = []
    # assert street_fighter_selection(fighters, (0, 0), moves) == solution
    # moves = ["left"] * 8
    # solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
    # assert street_fighter_selection(fighters, (0, 0), moves) == solution
    #
    # moves = ["right"] * 8
    # solution = ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
    # assert street_fighter_selection(fighters, (0, 0), moves) == solution
    #
    # moves = ["up"] * 4
    # solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
    # assert street_fighter_selection(fighters, (0, 0), moves) == solution

    moves = ["down", "right", "up", "left"] * 2
    solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
    assert street_fighter_selection(fighters, (0, 0), moves) == solution
