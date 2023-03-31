correct_guess: bool = False
guess: str = ""
planet: str = "Zortan"

while correct_guess is not True:
    guess = input('Can you guess the planet I am thinking of? >>>')
    if guess.lower() == planet.lower():
        print("Right guess!! Louis is at Zortan 🪐")
        correct_guess = True
    else:
        print('Nope, try again!')
