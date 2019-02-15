The plaintext after decryption is a poem which has been saved as plaintext.txt in part1 directory. 
The key is solved and output as a list from our program 1.py automatically: "['_', 'L', 'i', 't', 'F', 'u', 'T', '_'].

(functions mentioned below are all part of 1.py, the whole process is automated)

Since we know the plaintext is an article written in English, first we put the top 4 frequent characters in English in decending order into a list:frequent_char = [' ','e','t','a']. Then we used the frequency() function to find all the hex-character frequencies of cipher text then sort them in decending order as well. 

Afterwards, we assumed the most frequent plaintext character " " will match the most frequent ciphertext character. Under this assumption, we used the function "given_plaintext_ciphertext_find_key(plain_text,cipher_text)" to find the key that satisfies the assumption. As a result, we found "_". 

To make sure "_" in actually part of the key, since we know all plaintext characters are printables, we decide to decrypt the ciphertext with "_" as the key. After applying "_" as the key and decrypt the ciphertext, we notice following pattern: when two consecutive printable appears, 7 letter after the those letters, threre is always another pair of printable letters. The pattern always appears in the 1,8,9,16 position of each
line (i.e. in the first line, we see "T7.>...en3.....s", and T,e,n,s are all
printables) throught out the whole decryped text assuming "_" is the key. Thus
we deduce the key is 8 characters long and is "_??????_". (? represents unknown)

To find rest of the keys, we move on to the next most frequent hex characters in the cipher text (will be called C below). Then we try to find the corresponding key given C as cipher character and "_"(1st in the English frequency list) is valid by calling check_valid_key_letter() to check if the key is a printable character. If not, we move on to the second element in the English frequency list which is "e" and repeat the same method. 

When we find a printable key, we subsitute it with all the "?" in "_??????_" with that key and decrypt the whole file with the modified key. By calling check_valid_at_position(key_letter,index,cipher_text), we check if one of the position will lead to all printables at a specific index for every 8 characters. If yes, then the key is at that position.

We apply the same algorithm above to rest of the top frequent ciphertext hex characters, and stops until all key characters are found.




