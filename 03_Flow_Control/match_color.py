fav_color = input("What is your favorite color:  ")
# print (f"You said your favorite color is {fav_color}")
fav_color: str = fav_color.lower()

# instead of match in 3.10

if fav_color.casefold() == "red":
    print("I have Red Car!")
elif fav_color.casefold() == "blue":
    print("I have Blue Shirt!")
elif fav_color.casefold() == "green":
    print("I have Green Chair!")
else:
    print(f"I don't have {fav_color} color!")