if __name__ == '__main__':
    r = "rock"
    s = "scissors"
    p = "paper"
    P1W = "Player 1 wins!"
    P2W = "Player 2 wins!"
    Dr = "Draw!"

    while True:
        inputA = input("Player 1: ").lower()
        inputB = input("Player 2: ").lower()
        state = ""

        if (inputA == r and inputB == s) or (inputA == s and inputB == p) or (inputA == p and inputB == r):
            state = P1W
        elif (inputB == r and inputA == s) or (inputB == s and inputA == p) or (inputB == p and inputA == r):
            state = P2W
        else:
            state = Dr

        print(state)

        ch = input("Wanna play again? Y\\N: ")

        if ch == 'N':
            break