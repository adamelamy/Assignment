PASSWORD="qwer1234"

#openssl enc -d -des-ecb -in file1ECBerrorsalted.enc -out file1ECBerrorsalted -pass pass:$PASSWORD
#openssl enc -d -des-cbc -in file1CBCerrorsalted.enc -out file1CBCerrorsalted -pass pass:$PASSWORD
#openssl enc -d -des-cfb -in file1CFBerrorsalted.enc -out file1CFBerrorsalted -pass pass:$PASSWORD
#openssl enc -d -des-ofb -in file1OFBerrorsalted.enc -out file1OFBerrorsalted -pass pass:$PASSWORD

#openssl enc -d -des-ecb -in file2ECBerrorsalted.enc -out file2ECBerrorsalted -pass pass:$PASSWORD
#openssl enc -d -des-cbc -in file2CBCerrorsalted.enc -out file2CBCerrorsalted -pass pass:$PASSWORD
#openssl enc -d -des-cfb -in file2CFBerrorsalted.enc -out file2CFBerrorsalted -pass pass:$PASSWORD
#openssl enc -d -des-ofb -in file2OFBerrorsalted.enc -out file2OFBerrorsalted -pass pass:$PASSWORD

openssl enc -d -des-ecb -in file3ECBerrorsalted.enc -out file3ECBerrorsalted -pass pass:$PASSWORD
openssl enc -d -des-cbc -in file3CBCerrorsalted.enc -out file3CBCerrorsalted -pass pass:$PASSWORD
openssl enc -d -des-cfb -in file3CFBerrorsalted.enc -out file3CFBerrorsalted -pass pass:$PASSWORD
openssl enc -d -des-ofb -in file3OFBerrorsalted.enc -out file3OFBerrorsalted -pass pass:$PASSWORD

