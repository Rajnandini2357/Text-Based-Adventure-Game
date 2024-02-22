def intro():
    print("Welcome to the Brainly Adventure Game!")
    print("You find yourself in a mysterious room filled with puzzles and riddles.")
    print("Your mission is to solve each challenge to unlock the door and escape.")
    print("Are you ready to test your wits?")
    choice = input("Type 'start' to begin or 'quit' to exit: ").lower()
    if choice == 'start':
        start_game()
    elif choice == 'quit':
        print("You chose to quit. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        intro()

def start_game():
    print("\nYou're faced with your first challenge: a riddle!")
    print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
    answer = input("Your answer: ").lower()
    if answer == 'echo':
        print("Correct! The door unlocks, and you proceed to the next room.")
        room_two()
    else:
        print("Incorrect! Try again.")
        start_game()

def room_two():
    print("\nYou enter the second room, where you find a sequence of numbers written on the wall.")
    print("Each number seems to follow a pattern. Can you figure it out?")
    sequence = [2, 4, 6, 8, 10, 12, 14]
    print("Sequence:", sequence)
    guess = input("What is the next number in the sequence?: ")
    if guess == '16':
        print("Well done! The door opens, allowing you to proceed.")
        room_three()
    else:
        print("Incorrect! Keep trying.")
        room_two()

def room_three():
    print("\nIn the third room, you encounter a grid puzzle.")
    print("You must navigate from the top-left corner to the bottom-right corner,")
    print("using only right and down movements.")
    print("Each 'X' represents a blocked path, and each 'O' represents a valid path.")
    grid = [
        ['O', 'X', 'O', 'O'],
        ['O', 'O', 'X', 'O'],
        ['X', 'O', 'O', 'O'],
        ['O', 'X', 'O', 'O']
    ]
    print("Grid:")
    for row in grid:
        print(' '.join(row))
    path = input("Enter your path (e.g., DDRR): ").upper()
    if path == 'DDRR':
        print("Congratulations! You've solved the puzzle and unlocked the final door.")
        victory()
    else:
        print("Incorrect path! Try again.")
        room_three()

def victory():
    print("\nCongratulations! You've successfully navigated through all the challenges and escaped the room.")
    print("You're free to explore the outside world once again.")
    print("Thank you for playing the Brainly Adventure Game!")

# Start the game
intro()