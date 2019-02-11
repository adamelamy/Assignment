PASSWORD="qwer1234"

#openssl enc -e -des-ecb -in file1 -out file1ECB.enc -pass pass:$PASSWORD
#openssl enc -e -des-cbc -in file1 -out file1CBC.enc -pass pass:$PASSWORD
#openssl enc -e -des-cfb -in file1 -out file1CFB.enc -pass pass:$PASSWORD
#openssl enc -e -des-ofb -in file1 -out file1OFB.enc -pass pass:$PASSWORD

#openssl enc -e -des-ecb -in file2 -out file2ECB.enc -pass pass:$PASSWORD
#openssl enc -e -des-cbc -in file2 -out file2CBC.enc -pass pass:$PASSWORD
#openssl enc -e -des-cfb -in file2 -out file2CFB.enc -pass pass:$PASSWORD
#openssl enc -e -des-ofb -in file2 -out file2OFB.enc -pass pass:$PASSWORD

openssl enc -e -des-ecb -in file3 -out file3ECBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cbc -in file3 -out file3CBCsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-cfb -in file3 -out file3CFBsalted.enc -pass pass:$PASSWORD
openssl enc -e -des-ofb -in file3 -out file3OFBsalted.enc -pass pass:$PASSWORD

