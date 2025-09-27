from tic_tac_toe import Game, HumanPlayer, ComputerPlayer

def main():
    print("Welcome to Tic-Tac-Toe!")
    mode = input("Choose mode: (1) Friend vs Friend, (2) Human vs Computer: ")

    if mode == "1":
        name1 = input("Enter name for Player 1: ")
        name2 = input("Enter name for Player 2: ")
        p1 = HumanPlayer(name1, "X")
        p2 = HumanPlayer(name2, "O")

    elif mode == "2":
        name1 = input("Enter your name: ")
        p1 = HumanPlayer(name1, "X")
        p2 = ComputerPlayer("Computer", "O")

    else:
        print("Invalid choice, exiting.")
        return

    game = Game([p1, p2])
    game.play()

if __name__ == '__main__':
    main()
