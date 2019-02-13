PASSWORD="qwer1234"

openssl enc -e -des-ecb -in file1 -out file1ECBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cbc -in file1 -out file1CBCsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cfb -in file1 -out file1CFBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-ofb -in file1 -out file1OFBsalted.enc -pass pass:$PASSWORD

openssl enc -e -des-ecb -in file2 -out file2ECBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cbc -in file2 -out file2CBCsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cfb -in file2 -out file2CFBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-ofb -in file2 -out file2OFBsalted.enc -pass pass:$PASSWORD

openssl enc -e -des-ecb -in file3 -out file3ECBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cbc -in file3 -out file3CBCsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cfb -in file3 -out file3CFBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-ofb -in file3 -out file3OFBsalted.enc -pass pass:$PASSWORD

