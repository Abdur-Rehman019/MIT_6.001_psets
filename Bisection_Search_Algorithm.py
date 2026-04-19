#bisection search
x = int(input("Enter number :"))
#declare var
low = 0
high = x
num_guesses = 0
guess = (high + low)/2.0
epsilon = 0.1 # defining a range

while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses+=1

print(f"No. of guesses: {num_guesses}")
print(f"guess is: {guess}")

