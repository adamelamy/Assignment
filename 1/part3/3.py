import string
import random
import os

ERROR_LOCATION = 0x148

def getRandomString(characters, length):
    return "".join(random.choice(characters) for i in range(length))

def getRandomASCIIString(length):
    return getRandomString(string.printable, length)

def makeErrorFile(method, suffix = ""):
    with open("file3" + method + suffix + ".enc", "rb") as file:
        content = bytearray(file.read())
        print(method + ": " + str(len(content)))
        with open("file3" + method + "error" + suffix + ".enc", "wb") as errorFile:
            content[ERROR_LOCATION] = 0x42
            errorFile.write(content)

def compareError(original, method, suffix = ""):
    with open("file3" + method + "error" + suffix, "rb") as file:
        content = bytearray(file.read())
        print("Comparing: " + method)
        for i in range(len(content)):
            b = content[i]
            if b != originalContent[i]:
                print("Pos: " + hex(i) + " Original: " + hex(originalContent[b]) + " Error: " + hex(b))


with open("file3", "w") as file:
    random.seed(42)
    file.write(getRandomASCIIString(512))

print("encrypt.sh")
os.system("./encrypt.sh")

originalContent = None
with open("file3", "rb") as file:
    originalContent = bytearray(file.read())
    print("Original: " + str(len(originalContent)))
    

makeErrorFile("CBC")
makeErrorFile("CFB")
makeErrorFile("ECB")
makeErrorFile("OFB")

print("decrypt.sh")
os.system("./decrypt.sh")

compareError(originalContent, "CBC")
compareError(originalContent, "CFB")
compareError(originalContent, "ECB")
compareError(originalContent, "OFB")

print("encrypt_salt.sh")
os.system("./encrypt_salt.sh")

makeErrorFile("CBC", suffix = "salted")
makeErrorFile("CFB", suffix = "salted")
makeErrorFile("ECB", suffix = "salted")
makeErrorFile("OFB", suffix = "salted")

print("decrypt_salt.sh")
os.system("./decrypt_salt.sh")

compareError(originalContent, "CBC", suffix = "salted")
compareError(originalContent, "CFB", suffix = "salted")
compareError(originalContent, "ECB", suffix = "salted")
compareError(originalContent, "OFB", suffix = "salted")