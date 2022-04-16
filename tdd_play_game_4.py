from random import choice


def play_game(player_choice: str, computer_choice: str) ->int:
    choice_to_number = {
        'paper': 1,
        'rock': 2,
        'scissors': 3
    }

    player = choice_to_number[player_choice]
    ai = choice_to_number[computer_choice]

    if player == ai:
        return 0

    if (player == 1 and ai == 2) or (player == 2 and ai == 3) or (player == 3 and ai == 1):
        return 1

    return 2  # w pozostałych przypadkach, czyli gdy wygra komputer


def test_play_game_player_wins():
    assert play_game('rock', 'scissors') == 1
    assert play_game('paper', 'rock') == 1
    assert play_game('scissors', 'paper') == 1


def test_play_game_player_lose():
    assert play_game('rock', 'paper') == 2
    assert play_game('paper', 'scissors') == 2
    assert play_game('scissors', 'rock') == 2


def test_play_game_draw():
    assert play_game('rock', 'rock') == 0
    assert play_game('paper', 'paper') == 0
    assert play_game('scissors', 'scissors') == 0


if __name__ == '__main__':
    player = input('Pick: rock, paper, scissors: ')
    while player not in ['rock', 'paper', 'scissors']:
        player = input('Pick: rock, paper, scissors: ')

    computer = choice(['rock', 'paper', 'scissors'])

    print(f'Computer choice {computer}.')
    result = play_game(player, computer)

    if result == 1:
        print('Player win')
    elif result == 2:
        print('Computer win')
    else:
        print('Draw')
