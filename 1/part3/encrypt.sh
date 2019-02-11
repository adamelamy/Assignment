PASSWORD="qwer1234"

#openssl enc -e -des-ecb -nosalt -in file1 -out file1ECB.enc -pass pass:$PASSWORD
#openssl enc -e -des-cbc -nosalt -in file1 -out file1CBC.enc -pass pass:$PASSWORD
#openssl enc -e -des-cfb -nosalt -in file1 -out file1CFB.enc -pass pass:$PASSWORD
#openssl enc -e -des-ofb -nosalt -in file1 -out file1OFB.enc -pass pass:$PASSWORD

#openssl enc -e -des-ecb -nosalt -in file2 -out file2ECB.enc -pass pass:$PASSWORD
#openssl enc -e -des-cbc -nosalt -in file2 -out file2CBC.enc -pass pass:$PASSWORD
#openssl enc -e -des-cfb -nosalt -in file2 -out file2CFB.enc -pass pass:$PASSWORD
#openssl enc -e -des-ofb -nosalt -in file2 -out file2OFB.enc -pass pass:$PASSWORD

openssl enc -e -des-ecb -nosalt -in file3 -out file3ECB.enc -pass pass:$PASSWORD
openssl enc -e -des-cbc -nosalt -in file3 -out file3CBC.enc -pass pass:$PASSWORD
openssl enc -e -des-cfb -nosalt -in file3 -out file3CFB.enc -pass pass:$PASSWORD
openssl enc -e -des-ofb -nosalt -in file3 -out file3OFB.enc -pass pass:$PASSWORD

