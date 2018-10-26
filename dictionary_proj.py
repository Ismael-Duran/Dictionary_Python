
import json, string, difflib

data = json.load(open('data.json'))

def dct(keyWord):
    keyWord = keyWord.lower()    
    if keyWord in data:
        return data[keyWord]
    elif keyWord.title() in data:
        return data[keyWord.title()]
    elif keyWord.upper() in data:
        return data[keyWord.upper()]
    elif len(difflib.get_close_matches(keyWord, data.keys(), cutoff=0.7)) > 0:
        yn = input( "Did you mean %s? Enter Y if yes or N if no." %(difflib.get_close_matches(keyWord, data.keys(), cutoff=0.7))[0])

        if yn == "Y":
            return data[difflib.get_close_matches(keyWord, data.keys(), cutoff=0.7)[0]]
        elif yn == "N":
            return "The word does not exist."
        else:
            return "We did not understand your entry."
    else:
        return "The word does not exist."

while True:

    word = input("Enter Key: ")

    if word == " ":
        break

    else:

        ##dct(word)
        output = dct(word)

        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

print("End progam:...")
