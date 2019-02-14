import string
import random
import os
import operator

METHODS = ["CBC", "CFB", "ECB", "OFB"]

def getRandomString(characters, length):
    return "".join(random.choice(characters) for i in range(length))

def getRandomASCIIString(length):
    return getRandomString(string.printable, length)

def printFileLength(fileNumber, method, suffix = ""):
    with open("file" + str(fileNumber) + method + suffix + ".enc", "rb") as file:
        content = bytearray(file.read())
        print("file" + str(fileNumber) + method + suffix + ".enc: " + hex(len(content)))

def makeErrorFile(fileNumber, method, suffix = ""):
    with open("file" + str(fileNumber) + method + suffix + ".enc", "rb") as file:
        content = bytearray(file.read())
        with open("file" + str(fileNumber) + method + "error" + suffix + ".enc", "wb") as errorFile:
            errorLocation = int(len(content) / 2)
            print("Error Pos for file" + str(fileNumber) + method + suffix + ": " + hex(errorLocation))
            content[errorLocation] = operator.xor(content[errorLocation], 0xFF)
            errorFile.write(content)

def compareError(fileNumber, method, suffix = ""):
    originalContent = None
    with open("file" + str(fileNumber), "rb") as file:
        originalContent = bytearray(file.read())

    with open("file" + str(fileNumber) + method + "error" + suffix, "rb") as file:
        content = bytearray(file.read())
        print("Comparing file" + str(fileNumber) + method + suffix)
        
        errorOriginalValues = list()
        errorValues = list()

        errorStartLocation = None
        errorEndLocation = None

        def printErrorRange():
            print("Pos From: " + hex(errorStartLocation) + " To: " + hex(errorEndLocation))
            print("\tOriginal:")
            print("\t\t", end="")
            for originalValue in errorOriginalValues:
                if originalValue == None:
                    print("--", end=" ")
                else:
                    print(hex(originalValue), end=" ")
            print()
            print("\tError:")
                    
            print("\t\t", end="")
            for errorValue in errorValues:
                print(hex(errorValue), end=" ")
            print()

        for i in range(len(content)):
            b = content[i]
            ob = None
            if i < len(originalContent):
                ob = originalContent[i]

            if b != ob:
                if errorStartLocation == None:
                    errorStartLocation = i
                    errorEndLocation = i
                    errorOriginalValues.append(ob)
                    errorValues.append(b)
                elif i == errorEndLocation + 1:
                    errorEndLocation = i
                    errorOriginalValues.append(ob)
                    errorValues.append(b)
                
            if (b == ob or i == len(content) - 1) and len(errorValues) > 0:
                    printErrorRange()
                    errorOriginalValues.clear()
                    errorValues.clear()

                    errorStartLocation = None
                    errorEndLocation = None




with open("file3", "w") as file:
    random.seed(42)
    file.write(getRandomASCIIString(513))

# No Salt

print("encrypt.sh")
os.system("./encrypt.sh")

for i in range(1, 4):
    with open("file" + str(i), "rb") as file:
        originalContent = bytearray(file.read())
        print("Original file" + str(i) + ": " + hex(len(originalContent)))
    for method in METHODS:
        printFileLength(i, method)
    
for i in range(1, 4):
    for method in METHODS:
        makeErrorFile(i, method)

print("decrypt.sh")
os.system("./decrypt.sh")

for i in range(1, 4):
    for method in METHODS:
        compareError(i, method)
        print()

#SALT

print("encrypt_salt.sh")
os.system("./encrypt_salt.sh")

for i in range(1, 4):
    with open("file" + str(i), "rb") as file:
        originalContent = bytearray(file.read())
        print("Original: " + str(len(originalContent)))
    for method in METHODS:
        printFileLength(i, method, suffix = "salted")

for i in range(1, 4):
    for method in METHODS:
        makeErrorFile(i, method, suffix = "salted")


print("decrypt_salt.sh")
os.system("./decrypt_salt.sh")

for i in range(1, 4):
    for method in METHODS:
        compareError(i, method, suffix = "salted")
        print()