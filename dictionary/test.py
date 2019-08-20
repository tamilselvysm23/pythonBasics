import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def myfunction(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:
        x = input("Did you mean %s instead? Enter Y (or) y if YES, or N (or) n if NO: " % get_close_matches(word, data.keys())[0])

        if x == "Y" or x == "y":
            return data[get_close_matches(word, data.keys())[0]]

        elif x == "N" or x == "n":
            return "This word doesn't exist. Please check it."

        else:
            return "Invalid"

    else:
        return "This word doesn't exist. Please check it."

user_input = input("Enter word: ")
result = myfunction(user_input)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)
