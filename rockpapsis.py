def rock_paper_scissor(num1, num2, bit1, bit2):
    p1 = int(num1[bit1]) % 3
    p2 = int(num2[bit2]) % 3
    if player1[p1] == player2[p2]:
        print('Draw')

    elif player1[p1] == 'Rock' and player2[p2] == 'Scissor':
        print("P1 Wins")

    elif player1[p1] == 'Rock' and player2[p2] == 'Paper':
        print("P2 Wins")

    elif player1[p1] == 'Paper' and player2[p2] == 'Scissor':
        print("P2 Wins")

    elif player1[p1] == 'Paper' and player2[p2] == 'Rock':
        print("P1 wins")

    elif player1[p1] == 'Scissor' and player2[p2] == 'Rock':
        print("P2 Wins")

    elif player1[p1] == 'Scissor' and player2[p2] == 'Paper':
        print("P1 wins")

player1 = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
player2 = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}
while 1:
    num1 = input("P1, Enter Choice")
    num2 = input("P2, Enter Choice")
    bit1 = int(input("P1, Enter Secret bit"))
    bit2 = int(input("P2, Enter Secret bit"))
    rock_paper_scissor(num1, num2, bit1, bit2)
    ch = input("Continue?")
    if ch == 'y':
        break
