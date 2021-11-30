from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

# Holds all of the stacks
stacks = [left_stack, middle_stack, right_stack]

""" -- Game set up -- """
# Grabbing the input from the player
num_disks = int(input("\nHow many disks do you want to play with?\n"))

# forces the user to input something great than 3
while(num_disks < 3 and num_disks < left_stack.limit):
  num_disks = int(input("Enter a number greater than or equal to 3\n"))

# making disk
for i in range(num_disks, 0, -1):
  stacks[0].push(i)

# getting the optimial number of moves
num_optimal_moves = (2 ** num_disks) - 1
print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves")
        
""" --- User Input --- """
def get_input():
  # grabs the first letter of each stack
  choices = [stack.get_name()[0] for stack in stacks]
  choice = None
  # prompts users to enter a choice, until choice is valid
  while choice not in choices:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print(f"Enter {letter} for the {name} stack")
    # grabs input and returns stack the matchs input
    user_input = input("")
    if user_input in choices:
        for i in range(len(stacks)):
          if user_input == choices[i]:
            print(stacks[i])
            return stacks[i]
    else:
      print("\n -- PLEASE MAKE A VALID CHOICE -- \n")

""" --- Playing the game --- """
num_user_moves = 0

# Win condition
while right_stack.get_size() != num_disks:
  print("\n\n\n...Current Stacks...")
  # prints out stacks each move
  for stack in stacks:
    stack.print_items()
  # holds true until a valid move is made
  while True:
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    if from_stack == None:
      print("\n\nInvalid Move. Try Again")
    # checks move validity
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      # if valid moves the disk
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nInvalid Move. Try Again")
      
print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")
