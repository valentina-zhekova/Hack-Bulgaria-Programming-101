# even more unfinished
from AI import AI


def prompt():
    # prompts for possible commands
    pass


def get_palyer_input():
    # get player move and calls game.player_move()
    pass


def print_result():
    # print(game.__str__()) to print the board
    # and maybe some other prompts
    pass


def main():
    game = AI()

    prompt()
    while(True):
        # while EOG
        get_palyer_input()
        game.make_move()
        print_result()
        # if EOG => "break"

if __name__ == '__main__':
    main()
