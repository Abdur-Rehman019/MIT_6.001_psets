#cube root of +ve cubes
cube = 27
epsilon = 0.01
low = 0
high = cube # 27
guess = (low + high)/2.0
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    num_guesses+=1
    guess = (low + high)/2.0

print(f"No. of guesses: {num_guesses}")
print(f"guess is: {guess}")

