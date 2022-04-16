def play_game(player_choice, computer_choice):
    count = 0
    if player_choice == 'rock':
        if computer_choice == 'scissors':
            count = 3
        elif computer_choice == 'paper':
            count = 2
        else:
            count = 0

    if player_choice == 'paper':
        if computer_choice == 'rock':
            count = 3
        elif computer_choice == 'scissors':
            count = 2
        else:
            count = 0

    if player_choice == 'scissors':
        if computer_choice == 'paper':
            count = 3
        elif computer_choice == 'rock':
            count = 2
        else:
            count = 0

    return count


def test_win():
    assert play_game('rock', 'scissors') == 3
    assert play_game('paper', 'rock') == 3
    assert play_game('scissors', 'paper') == 3


def test_lose():
    assert play_game('rock', 'paper') == 2
    assert play_game('paper', 'scissors') == 2
    assert play_game('scissors', 'rock') == 2


def test_draw():
    assert play_game('rock', 'rock') == 0
    assert play_game('paper', 'paper') == 0
    assert play_game('scissors', 'scissors') == 0
