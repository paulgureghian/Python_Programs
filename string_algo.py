# An algorithm which takes a string
# And uses a loop and conditionals to find certain letters in the string

# Initialize variables
an_letters = "aefhilmnorsxAEFHILMNORSX"
print("")
word = input("Enter a word: ")
times = int(input("Times (1-10): "))

# For loop through the inputted word
for char in word:

    if char in an_letters:
        print("Give me an " + char)

    else:
        print("")
        print("Give me a  " + char)
        print("")

for i in range(times):
    print("")
    print(word, "\n")
