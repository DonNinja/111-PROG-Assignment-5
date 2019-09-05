num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code
max_int = 0

while num_int > 0:
    if num_int > max_int:
        max_int = num_int

    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line

# First we have to take in number
# Then it runs until a negative number is written into the input
# If it sees that the number the user inputs is bigger than the current max_int then it sets max_int as the inputted number
# When the user inputs a negative number then it prints out the largest number that was inputted