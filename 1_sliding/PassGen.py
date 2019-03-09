import itertools
import sys

HEX_CHARSET = "0123456789abcdef"

def hex():
    count = 16 ** 7
    charsetLength = len(HEX_CHARSET)
    while (count < (16 ** 16)):
        password = ""
        tmp = count
        while True:
            index = tmp % charsetLength
            tmp = int(tmp / charsetLength)
            
            password = HEX_CHARSET[index] + password
            if tmp == 0:
                break
        print(password)
        print(password.upper())
        count += 1

FRENCH_FILE_NAME = "francais.txt"
def french():
    with open(FRENCH_FILE_NAME, "r") as file:
        words = file.read().split("\n")
        for word in words:
            print(word)
            print(word.upper())

ENGLISH_FILE_NAME = "english.txt"
def english():
    with open(ENGLISH_FILE_NAME, "r") as file:
        words = file.read().split("\n")
        for word in words:
            print(word)
            print(word.upper())

NOVELIST_FILE_NAME = "novelist.txt"
def novelist():
    with open(NOVELIST_FILE_NAME, "r") as file:
        words = file.read().split("\n")
        for word in words:
            print(word.title().replace(" ", ""))
            

ENGLISH_SMALL_FILE_NAME = "english_small.txt"
ENGLISH_TINY_FILE_NAME = "english_tiny.txt"
LEET_TABLE = {
    "a": {"4", "@"},
    "b": {"6", "8"},
    "c": {"{", "<"},
    "e": {"3"},
    "g": {"6", "9"},
    "i": {"1", "!"},
    "l": {"1"},
    "o": {"0"},
    "p": {"9"},
    "q": {"2", "9"},
    "s": {"5", "$"},
    "t": {"7", "+"},
    "x": {"%"},
    "z": {"2"},
    }
def leet():
    with open(ENGLISH_FILE_NAME, "r") as file:
        words = file.read().split("\n")
        for word in words:
            word = word.lower()
            print(word)
            indexes = [i for i in range(len(word)) if word[i] in LEET_TABLE]
            combinations = list(itertools.combinations(indexes, 2))
            for combination in combinations:
                indexA = combination[0]
                indexB = combination[1]
                charA = word[combination[0]]
                charB = word[combination[1]]
                for mutA in LEET_TABLE[charA]:
                    for mutB in LEET_TABLE[charB]:
                        tmp = word
                        tmp = tmp[:indexA] + mutA + tmp[indexA + 1:]
                        tmp = tmp[:indexB] + mutB + tmp[indexB + 1:]
                        print(tmp)

TRIATHELETES_FILE_NAME = "triatheletes.txt"
def triatheletes():
    with open(TRIATHELETES_FILE_NAME, "r") as file:
        words = file.read().split("\n")
        for word in words:
            types = [1, 2, 3]
            combinations = list(itertools.combinations_with_replacement(types, 2))
            for combination in combinations:
                names = word.split(" ")
                for i in range(2):
                    type = combination[i]
                    if type == 1:
                        names[i] = names[i].upper()
                    elif type == 2:
                        names[i] = names[i].lower()
                    elif type == 3:
                        names[i] = names[i].title()

                print(names[0] + "$" + names[1])
                print(names[0] + "%" + names[1])
                print(names[0] + "*" + names[1])
                print(names[0] + "_" + names[1])

#WIKI DATA
#$("tr>td:first-child").each(function(index){console.log($(this).text())});

if __name__ == "__main__":
    type = sys.argv[1]
    if type == "hex":
        hex()
    elif type == "french":
        french()
    elif type == "english":
        english()
    elif type == "novelist":
        novelist()
    elif type == "leet":
        leet()
    elif type == "tri":
        triatheletes()