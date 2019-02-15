import itertools

#top frequent letter in English text
frequent_char = [' ','e','t','a']

#mapping stored in a 2D list
map = [[0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0 ],   
                [0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8 ],   
                [0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3 ],  
                [0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb ],  
                [0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa ],   
                [0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5 ],    
                [0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf ],  
                [0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd ],  
                [0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc ],    
                [0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4 ],   
                [0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe ],   
                [0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7 ],   
                [0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6 ],    
                [0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2 ],   
                [0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9 ],   
                [0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1 ]]

def decryptChar(encrypted, key):
#returns the decrypted character given a cipher character and its key
    el = encrypted & 0x0F
    eh = encrypted >> 4
    kl = key & 0x0F
    kh = key >> 4
    ph = findPlainChar(eh, kl)
    pl = findPlainChar(el, kh)
    return (ph << 4) + pl

def findPlainChar(e, k):
    for i in range(len(map)):
        row = map[i]
        if row[k] == e:
            return i

def decrypt(encryptedText, key):
    for i in range(len(encryptedText)):
        c = encryptedText[i]
    
        k = ord(key[i % len(key)])
        p = decryptChar(c, k)
        print(chr(p), end='')


def frequency(text):
#returns list of the frequency of hex pair in descending order
    freq = dict()
    for c in text:
        cHex = hex(c)
        if cHex not in freq:
            freq[cHex] = 1
        else:
            freq[cHex] += 1
    sortedFreq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    return sortedFreq

def decrypt_with_key(ciphertext,key):
# decrypts ciphertext with key and returnt the result
    key_list = list(key)
    result = ""
    for i in range(len(ciphertext)):
        result += chr(decryptChar(ciphertext[i],ord(key_list[i%len(key_list)])))
    return result

def split_digit(number):
# splite the 2 byte hex into first and second digit
    digit1 = number//16
    digit2 = number%16
    return hex(digit1),hex(digit2)

def combine_digit(digit1,digit2):
# calculate the hex with the given number as first and second digit
    return hex(digit1*16+digit2)



def given_plaintext_ciphertext_find_key(plain_text,cipher_text):
# returns key under assumption the plain_text has been encrypted to the ciphertext 
    ph,pl = split_digit(ord(plain_text))
    ch,cl = split_digit(int(cipher_text,16))
    #print(map[int(ph,16)])
    first_digit = map[int(pl,16)].index(int(cl,16))    
    second_digit = map[int(ph,16)].index(int(ch,16))
    #print(first_digit,second_digit)
    return chr(int(combine_digit(first_digit,second_digit),16))


def check_valid_key_letter(key_letter,cipher_letter):
    #check if the key and cipherletter can deduce a printable plaintext letter or not
    character = decryptChar(cipher_letter,ord(key_letter))
        # print("assumption: {}".format(format_header[i]))
        # print("cipher: {}".format(cipher_header[i]))
    #print(chr(character))
    if character not in range(32,127):
        if character == 0x0a:
            return True
        else: return False
    return True

def find_more_key_letter(key,cipher_letter,cipher_text):
# iterate through the unknown values of the given marked as "?" and returns the valid key letter
    key_letter = "\n"
    index = 0
    valid_key_letter = []

    while ord(key_letter) not in range(32,127) and index <len(frequent_char):
        key_letter = given_plaintext_ciphertext_find_key(frequent_char[index],cipher_letter)
        index +=1
    
    for i in range(len(key)):
        if key[i] == "?":
            if check_valid_at_position(key_letter,i,cipher_text):
                valid_key_letter.append((i,key_letter))
                    
            # while check_valid_key_letter(key_letter,cipher_text[index])
    return valid_key_letter

def check_valid_at_position(key_letter,index,cipher_text):
# check a key letter is valid by decrypt the cipher_text at index, returns 
# true if all decipherd letter is printable
    pointer = index
    counter = 0
    while pointer<len(cipher_text):
        #print(chr(cipher_text[pointer]))
        
        is_valid = check_valid_key_letter(key_letter,cipher_text[pointer])
        if not is_valid:
            return False
        pointer+=8
        counter+=1
    return True


file = open("ciphertext1", "rb")
encryptedText = file.read()
frequency = frequency(encryptedText)
key_letter=given_plaintext_ciphertext_find_key(frequent_char[0],frequency[0][0])
dText = decrypt_with_key(encryptedText,key_letter)
is_valid = check_valid_key_letter(key_letter,encryptedText[0])

"""
After applying "_" as the key and decrypt the ciphertext, we notice 
the follow pattern: when two consecutive printable appears, 7 letter
after the those letters, threre is always another pair of printable
letters. The pattern always appears in the 1,8,9,16 position of each
line (i.e. in the first line, we see "T7.>...en3.....s", and T,e,n,s are all
printables) throught out the whole decryped text assuming "_" is the key. Thus
we deduce the key is 8 characters long and is "_??????_" (? represents unknown)
"""
key = ["_","?","?","?","?","?","?","_"]
index = 1
while ("?" in key):
    valid_key_letter = find_more_key_letter(key,frequency[index][0],encryptedText)
    if len(valid_key_letter)>0:
        key[valid_key_letter[0][0]] = valid_key_letter[0][1]
    index+=1
print(key)

dText = decrypt_with_key(encryptedText,key)
testFile = open("plaintext.txt", "wb")
testFile.write(dText.encode('charmap'))

# print(hex(decryptChar(0xda,ord("_"))))
