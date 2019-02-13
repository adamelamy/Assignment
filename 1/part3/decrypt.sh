PASSWORD="qwer1234"

openssl enc -d -des-ecb -nosalt -in file1ECBerror.enc -out file1ECBerror -pass pass:$PASSWORD
openssl enc -d -des-cbc -nosalt -in file1CBCerror.enc -out file1CBCerror -pass pass:$PASSWORD
openssl enc -d -des-cfb -nosalt -in file1CFBerror.enc -out file1CFBerror -pass pass:$PASSWORD
openssl enc -d -des-ofb -nosalt -in file1OFBerror.enc -out file1OFBerror -pass pass:$PASSWORD

openssl enc -d -des-ecb -nosalt -in file2ECBerror.enc -out file2ECBerror -pass pass:$PASSWORD
openssl enc -d -des-cbc -nosalt -in file2CBCerror.enc -out file2CBCerror -pass pass:$PASSWORD
openssl enc -d -des-cfb -nosalt -in file2CFBerror.enc -out file2CFBerror -pass pass:$PASSWORD
openssl enc -d -des-ofb -nosalt -in file2OFBerror.enc -out file2OFBerror -pass pass:$PASSWORD

openssl enc -d -des-ecb -nosalt -in file3ECBerror.enc -out file3ECBerror -pass pass:$PASSWORD
openssl enc -d -des-cbc -nosalt -in file3CBCerror.enc -out file3CBCerror -pass pass:$PASSWORD
openssl enc -d -des-cfb -nosalt -in file3CFBerror.enc -out file3CFBerror -pass pass:$PASSWORD
openssl enc -d -des-ofb -nosalt -in file3OFBerror.enc -out file3OFBerror -pass pass:$PASSWORD

