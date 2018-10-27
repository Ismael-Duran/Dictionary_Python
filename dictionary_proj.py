## Import the following 
import json, string, difflib

## Download the JSON file on Github called "data.json"
data = json.load(open('data.json'))

# Function used to search for the word user queries
def dct(keyWord):
    keyWord = keyWord.lower()   ## lowercase all letters in the keyWord
    
    if keyWord in data:             ## search for word in data
        return data[keyWord]
    
    elif keyWord.title() in data:   ## used string.title() to convert original keyWord and try to search again 
        return data[keyWord.title()]
    
    elif keyWord.upper() in data:       ## used string.upper() to uppercase all letters and search again
        return data[keyWord.upper()]
    
    elif len(difflib.get_close_matches(keyWord, data.keys(), cutoff=0.7)) > 0: ##user mistypes keyWord, find approximate in dictionary
        
        yn = input( "Did you mean %s? Enter Y if yes or N if no. " %(difflib.get_close_matches(keyWord, data.keys(), cutoff=0.7))[0])
        
        if yn == "Y":
            return data[difflib.get_close_matches(keyWord, data.keys(), cutoff=0.7)[0]]
        elif yn == "N":
            return "The word does not exist. And enter another key."
        else:
            return "We did not understand your entry. And enter another key."
    else:
        return "The word does not exist. And enter another key."


word = input("Enter Key or press Enter to end program: ")

while word != "":

    output = dct(word) ## assign output with returned definition

    if type(output) == list: ## if word has more than one definition print all
        for item in output:
            print("Definition: " + item)
        word = input("Enter Key or press Enter to end program: ")
    else:
        print(output)
        word = input("Enter Key or press Enter to end program: ")

print("End progam:...")
