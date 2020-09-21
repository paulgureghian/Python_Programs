# Guess the cube root of a number 
# With a bisection algorithm

# Initialize variables
cube = 27
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0

# While loop
while abs(guess**3 - cube) >= epsilon:

    if guess**3 < cube:
        low = guess

    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1

print("")
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)
print("")
