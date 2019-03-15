# Part 1 Sliding Report

## Tools
All passwords were generated using PassGen.py while using JohnTheRipper stdin mode.

## Results

### UNIX Hashes
***
$1$PqS2KEk8$IDlM1oInP23nbSIcHX/GJ/\
exhi8i7ioner\
python3 .\PassGen.py leet | john --stdin .\hashes_linux.txt\
4 Minutes
***
$1$eUchdTyd$vUUVy.31j4ehOVEZKBApr/\
robinetterie\
python3 .\PassGen.py french | john --stdin .\hashes_linux.txt\
1 Minute
***
$1$I8kZvQEu$qxLLGYz2upD0KD/xOMoYk1\
5e22a8b0\
python3 .\PassGen.py hex | john --stdin .\hashes_linux.txt\
9.7 Hours
***
$1$mhd/ynSi$BJeU4IONenaV3UMACxebM/\
No Hint. Not Found.
***
$1$Zd0GhNfL$zXDi539NtghrzN1/bE4SY1\
katie_zaferes\
python3 .\PassGen.py tri | john --stdin .\hashes_linux.txt\
Less Than 1 Minute
***
### Windows Hashes
5FFEFBE2116A6921E5097CFFA8459B70\
MANAGER\
python3 .\PassGen.py english | john --format=NT --stdin .\hashes_windows.txt\
Less than 1 Minute
***
7F4444685F1296FC5052DA157C24310A\
No Hint. Not Found.
***
B00C82B8DF872377447E79D6917732B3\
SarahKlassen\
python3 .\PassGen.py novelist | john --format=NT --stdin .\hashes_windows.txt\
Less than 1 Minute
***

### Dictionary Files Are Downloade From:
http://www.gwicks.net/dictionaries.htm

## Methods
- Hex: Passwords were generated in hex() from 0 to f for length 1 to 16. Correct one was found at length 8.
- French: Passwords are iterated from the file francais.txt
- Leet: Passwords are generated from English dictionary then replace 2 characters to their leet transformation. itertools.combination was used for different combinations.
- Triathlete: Names are mined from wikipedia using JS listed in PassGen.py. They are stored in triatheletes.txt and mangled using python.
- English: Passwords iterated from English dictionary.
- Novelist: Names are mined from wikipedia using JS listed in PassGen.py. They are stored in novelist.txt and manipulated using python.

## Performance
John was ran against hases_linux/widnows_unsolved.txt instead.
Solved hashes were removed to increase performance in the case where stored passwords in john were removed.


## Hashes Without Hints
We tried to crack the last two hashes using brute force at first. Neither worked for 8 length ASCII passwords.
Then we tried to crack it using custom charset obtained from already cracked passwords.
pass.chr, pass_linux.chr and pass_windows.chr were generated and used.
But still no password was found.
