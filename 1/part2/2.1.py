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


key = []

def format_file_to_hex():
    file = open("ciphertext2",'rb')
    hex_text = file.read()
    hex_list = []
    for c in hex_text:
        cHex = hex(c)
        cHex_list = []
        if len(cHex) == 3:
            cHex_list.append(0)
            cHex_list.append(int(cHex[2],16))
        else:
            cHex_list.append(int(cHex[2],16))
            cHex_list.append(int(cHex[3],16))
        hex_list.extend(cHex_list)
    file.close()
    return hex_list

def format_formats_to_hex():
    raw_formats = [["gif87a","474946383761"],["gif89a","474946383961"],
                    ["jpg1","FFD8FFDB"],["jpg2","FFD8FFE000104A4649460001"],
                    ["jpg3","FFD8FFEE"],["png","89504E470D0A1A0A"],
                    ["pdf","255044462d"],["midi","4D546864"],["sql","53514c69746520666f726d6174203300"],
                    ["ico","00000100"],["zip","504B0304"],["rar","526172211A0700"],
                    ["rar2","526172211A070100"],["wmv","3026B2758E66CF11A6D900AA0062CE6C"],
                    ["ogg","4F676753"],["iso","4344303031"],["flac","664C6143"],
                    ["tar1","7573746172003030"],["tar2","7573746172202000"],["7zip","377ABCAF271C"],
                    ["xz","FD377A585A0000"],["xml","3c3f786d6c20"],["rtf","7B5C72746631"],
                    ["doc","D0CF11E0A1B11AE1"]]
    for i in range(len(raw_formats)):
        hex_list = []
        for single_hex in list(raw_formats[i][1]):
            hex_list.append(int("0x"+single_hex,16))
        raw_formats[i][1] = hex_list
    return raw_formats

def get_key(cipher_text, plain_text):
    key_list = []
    key_string = ''
    for i in range (0,len(plain_text)-1,2):
        key = match_cipher_to_map(cipher_text[i],cipher_text[i+1],plain_text[i],plain_text[i+1])
        if key:
            key_list.extend(key)
        else:
            return
            key_list.extend([0,9])
    for x in key_list:
        key_string = key_string + hex(x)[-1]
    key_string = bytes.fromhex(key_string).decode('ascii')
    return key_string

def match_cipher_to_map(ch, cl, ph, pl):
    key = []
    for j in range(16):
        if map[pl][j] == cl:
            key.append(j)
    for i in range(16):
        if map[ph][i] == ch:
            key.append(i)
    key_hex = key[0]*16 + key[1]
    if key_hex >= 32 and key_hex <= 126:
        return key
    else: 
        return False


cipher_text = format_file_to_hex()
formats = format_formats_to_hex()

for format_type in formats:
    printable_key = get_key(cipher_text,format_type[1])
    if printable_key:
        print(format_type[0])
        print(printable_key)




# keys = []
# for i in range(0,len(hex_list)):
#     keys.append([match_higher(hex_list[i][0]), match_lower(hex_list[i][1])])

# print(keys)