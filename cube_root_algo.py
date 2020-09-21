# Guess and check the cube root of a number
# With an epilson approximation

# Initialize variables
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0

# While loop
while abs(guess**3 - cube) >= epsilon and guess <= cube:

    guess += increment
    num_guesses += 1

print("")
print('num_guesses =', num_guesses)

if abs(guess**3 - cube) >= epsilon:

    print('Failed on cube root of', cube)

else:

    print(guess, 'is close to the cube root of', cube)
    print("")
    