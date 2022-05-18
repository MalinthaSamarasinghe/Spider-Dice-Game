# importing built-in random module
import random

# creating variables
unlockBodyPart = False
firstPlace = False
plyerNumber = 0
playerName = ''
returnedNumber = ''
playerRound = 0


def main():
    """
    The Function name   : main
    Last modified       : 05/18/2022

        printing the welcome message to the players of the dice game
        printing the explanation of spider dice game rules
        calling reRun function
        ending the program of the spider dice game
    """

    print("\n//\(oo)/\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\n")
    print("\t\t\t\tWelcome to The Spider Dice Game")
    print("\n//\(oo)/\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\n")
    print("\n<<<<<<<<<<<<<<< The Rules of The Spider Dice Game >>>>>>>>>>>>>>>>>")
    print("\n1. The object of the spider dice game is to be the first person to draw the spider."
          "\n2. Each player rolls one dice at a time; if they get a 6, they can draw the spider's body ( )."
          "\n3. After they've drawn the body – if they roll a 3 or 4 they can draw a leg, or a 1 to draw an eye."
          "\n4. The first person who draws the spider by adding a final part will win the game."
          "\n5. Important: Players must draw the spider's body () before adding to the other body parts.")
    print("\n//\(oo)/\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\   //\(oo)/\\\\\n")

    reRun()  # calling the reRun function
    exit()  # ending the program


def reRun():
    """
    The Function name   : reRun
    Last modified       : 05/18/2022

        creating a while loop to repeat the game if the user desires
        calling the gameLogic function
    """

    while True:  # creating a while loop to repeat the game if the user desires

        global firstPlace  # declaring variable as global

        gameLogic()  # calling the gameLogic function

        # getting user input for rerunning the program or not
        option = str(input("\nDo you want to play again? (y/n) ")).lower()

        print()

        while option not in ['y', 'n']:  # displaying rerun statement until the users enter a valid option
            print("Invalid Option! Please enter 'y' or 'n'")

            # getting user input for rerunning the program or not
            option = str(input("\nDo you want to play again? (y/n) ")).lower()

            print()
        else:
            if option == 'n':
                print("Thank you for taking the time to play.\n\t\t\t\tBye!!!")
                break  # if condition True: break loop
            else:
                firstPlace = False
                continue  # if condition False: continue loop --> calling the gameLogic function


def gameLogic():
    """
    The Function name   : gameLogic
    Last modified       : 05/18/2022

        creating a while loop to repeat the game if the user desires
        calling the gameLogic function
    """

    while True:  # creating a while loop to execute the set of statements as long as break the code

        try:  # preventing entering something other than integer for player count

            # creating a while loop to execute the set of statements until getting user input between including 1 and 4
            while True:
                # getting user input for players' count
                playerCount = int(input('How many players are there? (1..4) '))

                if playerCount in [1, 2, 3, 4]:  # checking if user-entered values are in the valid count range
                    break  # if condition True: break loop
                elif playerCount < 1:
                    print('At least need one player to play the spider dice game.\n')
                else:
                    print('Only maximum 4 players can play the spider dice game.\n')

            # in the following loop, the number of players should increase by 1
            playerCount += 1  # playerCount = playerCount + 1

            # playerDictionary is used to store data values in key:value pairs
            # playerDictionary stores playerNumber, playerName, number of rounds played, unlockBodyPart bool value,
            # and the drawing progress of the spider.
            playerDictionary = {}

            # playerNamelist is used to store multiple items in a single variable
            # playerNamelist stores names of players
            playerNamelist = []

            # winnerName is used to store data values in key:value pairs
            # winnerName stores names of the winner
            winnerName = []

            # winnerRound is used to store data values in key:value pairs
            # winnerName stores number of rounds played by the winner
            winnerRound = []

            global plyerNumber, returnedNumber, playerRound, playerName, firstPlace  # declaring variable as global

            # the for loop is used for iterating over a sequence
            # declaring 1 as a starting value of this for loop
            # declaring playerCount  as the endpoint of this for loop
            # declaring incrementing the sequence by 1 of this for loop
            for plyerNumber in range(1, playerCount, 1):

                # creating a while loop to execute the set of statements until getting correct and available names
                while True:
                    # getting user input for players' names
                    playerName = input(f'\nPlayer {str(plyerNumber)} : Please enter your name: ')

                    if playerName == '':  # checking if user-entered names or not
                        print('Please enter a proper name.')
                    elif playerName in playerNamelist:  # checking if the user-entered name already exists
                        print('Already have this name. Please enter another name.')
                    else:
                        playerNamelist.append(playerName)  # adding the name to the end of the playerNamelist
                        break  # break loop

                # the spider_drawing list is used to draw the spider from dice results
                spider_drawing = [*[''], *[''], *[''], *[''], *[''], *[''], *[''], *[''], *[''], *['']]

                # each player's details store playerDictionary with key as a plyerNumber
                playerDictionary[plyerNumber] = [playerName, '', playerRound, unlockBodyPart, spider_drawing]

            # creating a while loop to execute the set of statements until coming to a winner
            while not firstPlace:

                # this for loop ensures that each player of the game is able to play the game
                for plyerNumber in playerDictionary:

                    # calling the rollingTheDice function by parsing playerDictionary
                    # and storing the return value to a variable called returnedNumber
                    returnedNumber = \
                                rollingTheDice((playerDictionary[plyerNumber][0]), (playerDictionary[plyerNumber][3]),
                                               (playerDictionary[plyerNumber][4]))

                    # incrementing the number of rounds played by 1 when the player rolled the dice
                    playerDictionary[plyerNumber][2] += 1

                    # each player should be rolled the 6 to start drawing the spider
                    if returnedNumber == 6:
                        playerDictionary[plyerNumber][3] = True  # if condition True: unlockBodyPart assigned to True

                    # if unlockBodyPart == True
                    if playerDictionary[plyerNumber][3]:

                        # if condition True: drawing the spider's body
                        if returnedNumber == 6 and ((playerDictionary[plyerNumber][4][3] != '(') and (
                                playerDictionary[plyerNumber][4][6] != ')')):

                            # updating each player's spider_drawing [3] and [6] with ( )
                            playerDictionary[plyerNumber][4][3] = '('
                            playerDictionary[plyerNumber][4][6] = ')'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                    # if unlockBodyPart == True
                    if playerDictionary[plyerNumber][3]:

                        # if condition True: drawing the spider's left eye
                        if returnedNumber == 1 and (playerDictionary[plyerNumber][4][4] != 'o'):

                            # updating each player's spider_drawing [4] with o
                            playerDictionary[plyerNumber][4][4] = 'o'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                        # elif condition True: drawing the spider's right eye
                        elif (returnedNumber == 1) and (playerDictionary[plyerNumber][4][5] != 'o'):

                            # updating each player's spider_drawing [5] with o
                            playerDictionary[plyerNumber][4][5] = 'o'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                    # if unlockBodyPart == True
                    if playerDictionary[plyerNumber][3]:

                        # if condition True: drawing the spider's a leg
                        if ((returnedNumber == 3) or (returnedNumber == 4)) and (
                                playerDictionary[plyerNumber][4][0] != '/'):

                            # updating each player's spider_drawing [0] with /
                            playerDictionary[plyerNumber][4][0] = '/'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                        # elif condition True: drawing the spider's a leg
                        elif ((returnedNumber == 3) or (returnedNumber == 4)) and (
                                playerDictionary[plyerNumber][4][1] != '/'):

                            # updating each player's spider_drawing [1] with /
                            playerDictionary[plyerNumber][4][1] = '/'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                        # elif condition True: drawing the spider's a leg
                        elif ((returnedNumber == 3) or (returnedNumber == 4)) and \
                                playerDictionary[plyerNumber][4][2] != '\\':

                            # updating each player's spider_drawing [2] with \
                            playerDictionary[plyerNumber][4][2] = '\\'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                        # elif condition True: drawing the spider's a leg
                        elif ((returnedNumber == 3) or (returnedNumber == 4)) and \
                                playerDictionary[plyerNumber][4][7] != '/':

                            # updating each player's spider_drawing [7] with /
                            playerDictionary[plyerNumber][4][7] = '/'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                        # elif condition True: drawing the spider's a leg
                        elif ((returnedNumber == 3) or (returnedNumber == 4)) and \
                                playerDictionary[plyerNumber][4][8] != '\\':

                            # updating each player's spider_drawing [8] with \
                            playerDictionary[plyerNumber][4][8] = '\\'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                        # elif condition True: drawing the spider's a leg
                        elif ((returnedNumber == 3) or (returnedNumber == 4)) and \
                                playerDictionary[plyerNumber][4][9] != '\\':

                            # updating each player's spider_drawing [9] with \
                            playerDictionary[plyerNumber][4][9] = '\\'

                            # to make it simpler for the user to see, spiderArt is shown as a string
                            spiderArt = ''.join(playerDictionary[plyerNumber][4])

                            # the spider's progress is saved in the playerDictionary at index 1
                            playerDictionary[plyerNumber][1] = spiderArt

                    print(f'\n{(playerDictionary[plyerNumber][0])}, So far the spider :  '
                          f'[    {(playerDictionary[plyerNumber][1])}    ]')

                    # for debugging purpose (commented)
                    # print(playerDictionary)

                    # if condition True: one player completed drawing the spider
                    if (playerDictionary[plyerNumber][1]) == '//\\(oo)/\\\\':

                        # adding the winner's name to the end of the winnerName
                        winnerName.append(playerDictionary[plyerNumber][0])

                        # adding the number of rounds played by the winner to the end of the winnerRound
                        winnerRound.append(playerDictionary[plyerNumber][2])

                        # firstPlace assigned to True -->  break the while loop
                        firstPlace = True

            print()
            print('=' * 65)  # printing dashed lines
            # printing the winner's name and the number of rounds played by the winner
            print(f'\nCongratulation!!! The winner was {winnerName[0]} with {(winnerRound[0])} rounds.\n')
            print('=' * 65)  # printing dashed lines

            break  # break the while loop

        except ValueError:  # if there is a value error in the player input, this 'except' block will run
            print('Expecting an Integer value.\n')


def rollingTheDice(player_name, unlock_body, spider_drawing):
    """
    The Function name   : rollingTheDice
    Last modified       : 05/18/2022
    Parameters          : player_name    --> current round player name
                          unlock_body    --> current round player's unlockBodyPart value
                          spider_drawing --> current round player's spider_drawing

        creating a while loop to roll the dice
    """

    while True:
        print()
        print('-' * 65)  # printing dashed lines
        # getting user input to roll the dice
        rollingDice = input(f"\n{player_name}, Press 'Enter' to roll the dice")

        # if condition True: generating a random number between including 1 and 6 and assigning to the rolledNumber
        if rollingDice == '':
            rolledNumber = random.randint(1, 6)
            print()

            # if unlock_body == True
            if unlock_body:

                # if condition True: displaying a set of statement
                if rolledNumber == 6:
                    print(f'Rolls a {rolledNumber}')
                    print("Already have the spider's body")

            # if unlock_body == False
            if not unlock_body:

                # if condition True: displaying a set of statement
                if rolledNumber == 6:
                    print(f'Rolls a {rolledNumber}')
                    print("Unlocked the spider's body (  )")

            # if unlock_body == False
            if not unlock_body:

                # if condition True: displaying a set of statement
                if rolledNumber == 3 or rolledNumber == 4 or rolledNumber == 1:
                    print(f'Rolls a {rolledNumber}')
                    print("Should unlock the spider's body first")

                # if condition True: displaying a set of statement
                if rolledNumber == 2 or rolledNumber == 5:
                    print(f'Rolls a {rolledNumber}')
                    print("Doesn't unlock anything this round")

            # if unlock_body == True
            if unlock_body:

                # if condition True: displaying a set of statement
                if (rolledNumber == 1) and (spider_drawing[4] != 'o'):
                    print(f'Rolls a {rolledNumber}')
                    print("Unlocked the spider's eye o")

                # if condition True: displaying a set of statement
                if (rolledNumber == 1) and ((spider_drawing[4] == 'o') and (spider_drawing[5] != 'o')):
                    print(f'Rolls a {rolledNumber}')
                    print("Unlocked the spider's eye o")

                # if condition True: displaying a set of statement
                if (rolledNumber == 1) and ((spider_drawing[4] == 'o') and (spider_drawing[5] == 'o')):
                    print(f'Rolls a {rolledNumber}')
                    print("Already have spider's eyes oo")

            # if unlock_body == True
            if unlock_body:

                # if condition True: displaying a set of statement
                if ((rolledNumber == 3) or (rolledNumber == 4)) and (spider_drawing[9] != '\\'):
                    print(f'Rolls a {rolledNumber}')
                    print("Unlocked the spider's leg / \\")

                # if condition True: displaying a set of statement
                if ((rolledNumber == 3) or (rolledNumber == 4)) and (spider_drawing[9] == '\\'):
                    print(f'Rolls a {rolledNumber}')
                    print("Already have spider's legs / \\")

                # if condition True: displaying a set of statement
                if rolledNumber == 2 or rolledNumber == 5:
                    print(f'Rolls a {rolledNumber}')
                    print("Doesn't unlock anything this round")

            return rolledNumber  # returned rolledNumber value

        else:  # if condition False: displaying a statement
            print("Please press 'Enter' to roll the dice")


# calling the main function
if __name__ == '__main__':
    main()
