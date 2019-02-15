map = ((0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0 ),
    (0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8 ),
    (0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3 ),
    (0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb ),
    (0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa ),    
    (0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5 ),
    (0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf ),  
    (0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd ),  
    (0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc ),    
    (0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4 ),   
    (0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe ),   
    (0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7 ),   
    (0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6 ),    
    (0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2 ),   
    (0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9 ),   
    (0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1 ))


def frequency(text):
    #return list of the frequency of hex pair in descending order
    freq = dict()
    for c in text:
        cHex = hex(c)
        if len(cHex) < 4:
            cHex = cHex[:2] + '0' + cHex[2]
        if cHex not in freq:
            freq[cHex] = 1
        else:
            freq[cHex] += 1
    sortedFreq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    return sortedFreq

def find_repeated_printable(text, length): 
    #checks blocks of "length" every 9 to 100 chars
    #return percentage of printable chars 
    length_freq = dict()
    
    for i in range(9,100):
        printable_count = 0
        total_count = 0
        for j in range(0, len(text)-length, i):
            for k in range(length):
                if ord(text[j+k])>=32 and ord(text[j+k])<=126:
                    printable_count += 1
                total_count += 1
        length_freq[i] = round(printable_count/total_count,2)  
               
    sortedFreq = sorted(length_freq.items(), key=lambda kv: kv[1], reverse=True)
    return sortedFreq

def freq_partial_decrypted(text,block_length,key_length):
    #returns frequency of blocks of "length" for every "key_length" chars
    #freq of blocks of 4 chars for every 40 chars
    partial_text_char = []
    for i in range(0,len(text)-block_length,key_length):
        partial_text_char.extend(text[i:i+block_length])
    
    partial_text_ascii = []
    for c in partial_text_char:
        partial_text_ascii.append(ord(c))
    partial_freq = frequency(partial_text_ascii)
    return partial_freq

def freq_specific_pos(text, pos, key_length):
    #returns frequency of a specific column out of "key_length" (40)
    pos_text = []
    for i in range(0+pos, len(text), key_length):
        pos_text.append(text[i])
    pos_freq = frequency(pos_text)  
    return pos_freq

def key_from_mapping(cipher,plain):
    #gets single key from plain, cipher
    ch = int(cipher[2],16)
    cl = int(cipher[3],16)
    ph = int(plain[2],16)
    pl = int(plain[3],16)
    kl = 0
    kh = 0
    for i in range (16):
        if map[ph][i] == ch:
            kl = i
    
    for j in range (16):
        if map[pl][j] == cl:
            kh = j
    key = kh*16 + kl
    if key>=32 and key<=126:
        key_hex = hex(key)[2:]
        single_key = bytes.fromhex(key_hex).decode('ascii')
        return single_key
    else:
        return False

def decrypt_with_key(ciphertext,key):
    #decrypts ciphertext with key
    key_list = list(key)
    result = ""
    for i in range(len(ciphertext)):
        result += chr(decryptChar(ciphertext[i],ord(key_list[i%len(key_list)])))
    return result

def decryptChar(encrypted, key):
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
def main():
    file = open ('ciphertext2','rb')
    text = file.read()
    file.close()
    key="[95w"
    partial_text = decrypt_with_key(text,key)

    printable_freq = find_repeated_printable(partial_text, len(key))
    key_length = printable_freq[0][0]
    partial_frequency = freq_partial_decrypted(partial_text, len(key), key_length)

    for i in range(4,key_length):
        pos_freq = freq_specific_pos(text, i, key_length)
        j = 0
        single_key = key_from_mapping(pos_freq[j][0], partial_frequency[0][0])
        while single_key == False:
            j=+1
            single_key = key_from_mapping(pos_freq[j][0], partial_frequency[0][0])
        key = key + single_key
    dText = decrypt_with_key(text, key)
    testFile = open("test_p2.zip", "wb")
    testFile.write(dText.encode('charmap'))
    testFile.close()

    '''
    Using the key '[95wJL4PiE)7u^P-Q(%^-_254dh1F@@nn%128e2o' and looking at the
    output file using xxd, most of the file is decrypted. However, there are  2 
    specific columns, columns 34 and 39, that were decrypted wrongly. This can be 
    seen from common words such as gradient, window, format etc being spelt wrongly
    and these mistakes appears only on column 34 and 39. We will manually fix this
    below
    '''

    pos_freq = freq_specific_pos(text, 33, key_length)

    '''
    Instead of mapping the most frequent hex to 'space' (most freq in partial plaintext),
    we try the second most frequent hex (0xae)
    '''

    single_key_33 = key_from_mapping(pos_freq[1][0], partial_frequency[0][0])

    ''' Do the same thing for column 39 '''

    pos_freq = freq_specific_pos(text, 38, key_length)
    single_key_38 = key_from_mapping(pos_freq[1][0], partial_frequency[0][0])

    ''' Test new key '''

    new_key = key[:33] + single_key_33 + key[34:38] + single_key_38 + key[39:]
    print(new_key)
    dText = decrypt_with_key(text, new_key)
    testFile = open("p2_file.zip", "wb")
    testFile.write(dText.encode('charmap'))
    testFile.close()

    ''' Fully decrypted! zip file with a single svg file "LLVM_Logo.svg" '''
