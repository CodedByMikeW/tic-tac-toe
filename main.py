import random


art="""          
           |           |
           |           |
 l-top     |   m-top   |  r-top
           |           |
           |           |
__________ | _________ | ____________
           |           |
           |           |
 l-middle  |  m-middle |  r-middle
           |           |
           |           |
__________ | _________ | ____________
           |           |
           |           |
 l-bottom  | m-bottom  |  r-bottom
           |           |
           |           |

"""
# Cross ^^^


def tictactoe_game():
    game_on = True
    print(art)
    positions = ["l-top","m-top","r-top",
                 "l-middle","m-middle","r-middle",
                 "l-bottom","m-bottom","r-bottom"]
    #robot_positions = ["(R)_l-top ", "(R)_m-top", "(R)_r-top",
                # "(R)_l-middle", "(R)_m-middle", "(R)_r-middle",
                # "(R)_l-bottom", "(R)_m-bottom", "(R)_r-bottom"]
    board=[]
    user_board=[]
    robot_board=[]


    robo_nice=True
    print("Welecome to the tictactoe game")
    print("The game will have have to be played with numbers 0-8\n")
    while game_on :

        print(f"Choices: {positions}")
        user=input("Type here: ")
        robot = random.choice(positions)

        if user not in board and robot not in board:
            board.append(user)
            user_board.append(user)
            print(f"you have now these choices{positions}\n")

            print(f"robot chose: {robot}")

            board.append(robot)
            #robot=(f"Robo:{robot}")
            robot_board.append(robot)
            print(art)
            print(f"This is on the Game board {board}")
            print(f"Robot board{robot_board} ")
            print(f"Your board {user_board}\n")


            #print(f"Now that the robot picked this is the board\n{board}\n")

            if "l-top" in user_board and "m-top" in user_board and "r-top" in user_board  :
                print("YOu WIN")
                print("Game_over")
                game_on = False
            elif "l-middle" in user_board and "m-middle" in user_board and "r-middle" in user_board:
                print("YOu WIN")
                print("Game_over")
                game_on = False
            elif 'l-bottom' in user_board and 'm-bottom' in user_board and 'r-bottom' in user_board:
                print("YOu WIN")
                print("Game_over")
                game_on = False

            #--------------------------------------------------------------------------
            elif "Robo:l-top" in robot_board and "Robo:m-top" in robot_board and "Robo:r-top" in robot_board  :
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False
            elif "Robo:l-middle" in robot_board and "Robo:m-middle" in robot_board and "Robo:r-middle" in robot_board:
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False
            elif 'Robo:l-bottom' in robot_board and 'Robo:m-bottom' in robot_board and 'Robo:r-bottom' in robot_board:
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False
            #---------------------------------------------------------------------------------

                    # horzontail ^^^

            elif 'l-top' in user_board and 'l-middle' in user_board and 'l-bottom' in user_board:
                print("YOu WIN")
                print("Game_over")
                game_on = False
            elif 'm-top' in user_board and 'm-middle' in user_board and 'm-bottom' in user_board:
                print("YOu WIN")
                print("Game_over")
                game_on = False
            elif 'r-top' in user_board and 'r-middle' in user_board and 'r-bottom' in user_board:
                print("YOu WIN")
                print("Game_over")
                game_on = False

                #----------------------------------------------------------
            elif 'Robo:l-top' in robot_board and 'Robo:l-middle' in robot_board and 'Robo:l-bottom' in robot_board:
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False
            elif 'Robo:m-top' in robot_board and 'Robo:m-middle' in robot_board and 'Robo:m-bottom' in robot_board:
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False
            elif 'Robo:r-top' in robot_board and 'Robo:r-middle' in robot_board and 'Robo:r-bottom' in robot_board:
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False
            #----------------------------------------------------------------------------------------
                    # vertical ^^^^

            elif 'l-top' in user_board and 'm-middle' in  user_board and 'r-bottom' in user_board:
                print("YOu WIN")
                print("Game_over")
                game_on = False
            elif 'r-top' in user_board and 'm-middle' in user_board and 'l-bottom' in user_board:
                print("YOu WIN")
                print("Game_over")
                game_on = False

                #------------------------------------------
            elif 'Robo:l-top' in robot_board and 'Robo:m-middle' in robot_board and 'Robo:r-bottom' in robot_board:
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False
            elif 'Robo:r-top' in robot_board and 'Robo:m-middle' in robot_board and 'Robo:l-bottom' in robot_board:
                print("Robot WoN You loseeeee.")
                print("Game_over")
                game_on = False

                #--------------------------------
                #crossss^^^^^
        elif user in board and robot in board:
            print("Spot taken Try again")

        # if robot in board:
        # print(robot)
        # print("Robo picked a spot that was taken  has to pick again ")
        # robot=random.choice
        # print(f"robo new choice{robot}")
tictactoe_game()

tictactoe_game()
