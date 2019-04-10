# Assignment 2 Sliding Part
1. To become a CA, we need a private key and a signed root certificate.
    1. First, we run `openssl genrsa -des3 -out 333rootCA.key 4096` to generate our private key. -des3 encrypts the key using DES cipher, 4096 is the bit length of the key. We use a random generated passphrase: `q2X6wXVjf3Od`.
    2. Then, we create a root certificate (333rootCA.crt) and sign using our private key (333rootCA.key) by running `openssl req -x509 -new -nodes -key 333rootCA.key -sha256 -days 1024 -out 333rootCA.crt`. Our organization name is "Group06_W19".

2. We create a certificate key to generate a certificate signing request (CSR).
    1. First, we run `openssl genrsa -out 10.229.6.4.key 2048` to create certificate key.
    2. Then, we edit openssl.cnf (/etc/ssl/openssl.cnf) to set `policy = policy_anything`.
    3. Then, we run `openssl req -new -key 10.229.6.4.key -out 10.229.6.4.csr` to generate CSR. Our organization name is `Group06_W19_Web_Services`.
3. We sign the CSR (10.229.6.4.csr) with our CA private key (333rootCA.key) by running `openssl x509 -req -in 10.229.6.4.csr -CA 333rootCA.crt -CAkey 333rootCA.key -CAcreateserial -out 10.229.6.4.crt -days 500 -sha256` and the passphrase set in Step 1(i).
4. We configure Apache2 to use the signed certificate by editing /etc/apache2/sites-enabled/000-default.conf:

        <VirtualHost *:443>
                DocumentRoot /var/www/html
                SSLEngine on
                SSLCertificateFile /home/keanweng/10.229.6.4.crt
                SSLCertificateKeyFile /home/keanweng/10.229.6.4.key
                SSLCertificateChainFile /home/keanweng/333rootCA.crt
        </VirtualHost>

5. To load the certificate on the Windows machine, we have to trust the CA we just made.
    1. First, we scp 333rootCA.crt to the Windows Server and log in into Admin account.
    2. Then, we open 333rootCA.crt and click "Install Certificate".
    3. Select "Local Machine" for "Store Location". Click "Next".
    4. Select "Place all certificates in the following store" and click on "Browse".
    5. Select "Trusted Root Certificate Authorities" to trust the CA we made. Click "Next" then "Finish" to install certificate.
    6. To verify that certificate is installed, goto Windows Search and search for "Manage computer certificates"
    7. Browse to "Trusted Root Certificate Authorities" > "Certificates", and we should see a "G6" certificate.
    8. We are able to access https://10.229.6.4 now.
        Screenshot (in ./assignment_2_sliding):

                Before trusting our CA: does_not_recognize.png
                After trusting our CA: recognized_1.png, recognized_2.png
        
6. These are the iptables rule that we added:

        sudo iptables -R INPUT 3 -s 10.229.0.0/16 -p tcp -m multiport --dports 21,80,443 -j ACCEPT
        sudo iptables -R OUTPUT 3 -d 10.229.0.0/16 -p tcp -m multiport --dports 21,80,443 -j ACCEPT
        (-R to replace our old INPUT/OUTPUT rule at line 3, added port 443 for HTTPS)

7. To sign Java jar files with our CA, the process is similar to signing a certificate. We create a keystore and then create a CSR. Then, we get our CA to sign the CSR. Then, we install the signed certificates into the keystore. Then, we sign the JAR file using the keystore. Purpose of each step is at the last sentence.
    1. First we install keytool and jarsigner from JDK. We need keytool to manage keystore and jarsigner to sign JAR files.
    2. To create Java Keystore File, we run `keytool -genkey -alias 333jar -keyalg RSA -keysize 2048 -keystore keystore.jks`. Enter relevant info and set a password. This will give us keystore file (keystore.jks). We need a Java Keystore File to generate CSR. 
    3. We generate CSR from keystore by `keytool -certreq -alias 333jar -file 333jar.csr -keystore keystore.jks`. Enter keystore password set in Step 2. This will give us a CSR (333jar.csr). We need a CSR for our CA to sign.
    4. We sign CSR (333jar.csr) with our CA by running `openssl x509 -req -in 333jar.csr -CA 333rootCA.crt -CAkey 333rootCA.key -CAcreateserial -out 333jar.crt -days 500 -sha256`. CA signs CSR to generate the signed certificate.
    5. We install the signed certificates (333rootCA.crt, 333jar.crt) into keystore (333jar.jks) by running:

            keytool -import -trustcacerts -alias root -file 333rootCA.crt -keystore keystore.jks
            keytool -import -trustcacerts -alias 333jar -file 333jar.crt -keystore keystore.jks
        Enter keystore password set in Step 2. Now, keystore is CA verified.
    6. Now we are ready to sign jar files using keystore.jks.
    7. We run `jarsigner -tsa http://sha256timestamp.ws.symantec.com/sha256/timestamp -keystore keystore.jks [jar-filename] 333jar`. Enter keystore password set in Step 2.  Time Stamp Authority (TSA) so that we don't have to resign JAR file once the certificates expires.
    8. jar file is signed! We verify by running `jarsigner -verify -verbose -certs [jar-filename]`

# Assignment 3
## Part 1
1. The program reads from stdin and randomly capitalize the input string by subtracting 0x20 for each character. By running `echo "aaaaaaaa" | ./weak | od -A n -t x1`, we can see that some random 'a's (0x61) is output as 'A's (0x41). The program only outputs a maximum of 12 characters. If input is longer than 19 characters, the program gets a segmentation fault.
2. Since we know the buffer is set before calling scanf, we interrupt scanf in gdb to get memory address `0x805155d`. By looking at the objdump, we know entry point is `0x8051540`. Then we search for all instructions that jumps to this address and we can see some memory allocation before jumping. We input a long string to make the program segfault, and look at the location of the buffer overflow, which is near `0xffffd550`. Looking at the stack with and without buffer flowing, we can see that the buffer size is 12 bytes and we have to account for the saved registers, therefore, overflowing starts 20 bytes after start of buffer.
3. First, we look at the .rodata section of the program by running `objdump -s -j .rodata`. We can see that all of the "Owned by group XX" strings are stored in the front of .rodata.

        Contents of section .rodata:
        809f8a0 03000000 01000200 4f776e65 64206279  ........Owned by
        809f8b0 2067726f 75702030 310a004f 776e6564   group 01..Owned
        809f8c0 20627920 67726f75 70203032 0a004f77   by group 02..Ow
        809f8d0 6e656420 62792067 726f7570 2030330a  ned by group 03.
        809f8e0 004f776e 65642062 79206772 6f757020  .Owned by group 
        809f8f0 30340a00 4f776e65 64206279 2067726f  04..Owned by gro
        809f900 75702030 350a004f 776e6564 20627920  up 05..Owned by 
        809f910 67726f75 70203036 0a004f77 6e656420  group 06..Owned 
        809f920 62792067 726f7570 2030370a 004f776e  by group 07..Own
        809f930 65642062 79206772 6f757020 30380a00  ed by group 08..
        809f940 4f776e65 64206279 2067726f 75702030  Owned by group 0
        809f950 390a004f 776e6564 20627920 67726f75  9..Owned by grou
        809f960 70203130 0a004f77 6e656420 62792067  p 10..Owned by g
        809f970 726f7570 2031310a 004f776e 65642062  roup 11..Owned b
        809f980 79206772 6f757020 31320a00 4f776e65  y group 12..Owne
        809f990 64206279 2067726f 75702031 330a0025  d by group 13..%

    Then, we look at starting address of "Owned by group 06" which is `0x809f907`. In objdump, we search for the instruction that push this string into stack, which is `80482a5:	68 07 f9 09 08       	push   $0x809f907`. Now we know the starting address of our function is `0x0804829c`. Then, we buffer overflow the program to make it jump to `0x0804829c`. To make program terminate normally after calling that function, we have to buffer overflow is with a correct return address. Since exit is a syscall, we use gdb to catch the syscall and get the memory address to jump to. In gdb, we run `catch syscall 1 252` to call 'exit' and 'exit\_group' syscall. Then, we just run the program without segfault so that it exits normally. From gdb, we get `Catchpoint 2 (call to syscall exit_group), 0x08051447 in ?? ()`. `0x08051447` is the address we want to jump to exit normally. 

4.  Our exploit source code:

        #!/bin/bash
        python -c 'print " "*20 + "\x9c\x82\x04\x08" + "\x47\x14\x05\x08"' | ./weak

5.  Our exploit is just piping `20 spaces + address of our function + address of exit syscall` into the program. We find the padding space by overflowing the buffer with a long string, then running `info registers` to look at the registers. $esp is pointing at `0xffffd550` on the stack and loads the content into $eip as the address of next instruction. This position on the stack is 20 bytes after the buffer which is why we overflow it with the address of our function. After running our desired function, the program seg faults because of invalid return address. We run `info registers` in gdb and see that $esp is pointing at `0xffffd554` on the stack and loads the content into $eip as return address. This address is right after our initial 24 bytes overflow, therefore we overflow it with the memory address of our exit to make the program terminate normally.

## Part 2
### Step 1

#### 1:

Command: 
- nmap -oN output.txt -sS -A -p 21,22,80,443,3389 10.229.100.0/24

10.229.100.151 (Victim, Server)
- Port 80 Open with IIS 8.5
- Port 3389 Open Windows RDP
- hostname: victimswindowsinstance.yeg.cloud.cybera.ca
- IIS 8.5 => Windows Server 2012 R2

10.229.100.101 (Victim, Client)
- Port 22 Open with ssh 2.0
- Data returned from port 22 shows it's x86_64 linux-gnu Ubuntu
- OpenSSH 6.6.1p1x20Ubuntu-2ubuntu2.8
- Port 80 Open 
- List of dates
- 1.0
2007-01-19
2007-03-01
2007-08-29
2007-10-10
2007-12-15
2008-02-01
2008-09-01
2009-04-04

10.229.100.154 (Victim, Client, Logger)
- Port 22 Open with ssh 2.0
- Data returned from port 22 shows it's x86_64 linux-gnu Ubuntu
- hostname: logger.yeg.cloud.cybera.ca

10.229.100.155 (TA FW)
- hostname: greatta1fw.yeg.cloud.cybera.ca
- Port 21 Open with ftp. Has anonymous login.
- Port 22 Open with ssh 2.0
- Data returned from port 22 shows it's x86_64 linux-gnu Ubuntu
- OpenSSH 6.6.1p1x20Ubuntu-2ubuntu2.8

10.229.100.156 (TA ARP Test)
- hostname: arptest.yeg.cloud.cybera.ca 
- Port 22 Open with ssh 2.0
- Data returned from port 22 shows it's x86_64 linux-gnu Ubuntu
- OpenSSH 6.6.1p1x20Ubuntu-2ubuntu2.8

NMap sends a corresponding request to each service. 
The responce is used to determine what exact version and variant of the service is running.

Example: For port 80, NMap sends a HTTP request. The response from 154 shows the server is running IIS 8.5.

### Step 2
#### 10.229.100.151 Server
	Ping Request to 156 155 154 150 147 144 142 141 139 138 137 136 133 132 131 130 102 101
	Ping Reply to 138 
	Sends /example.gif back in HTTP using multiple tcp fragments
	Sends /example.mp3 back in HTTP using multiple tcp fragments
	Sends /page.htm back in HTTP
	
#### 10.229.100.154 Client
	Ping Request to 151
	Ping Reply to 151
	HTTP1.1 GET /example.gif
	Uses wget
	
#### 10.229.100.101 Client
	Ping Request to 151
	Ping Reply to 151
	HTTP GET /example.mp3
	HTTP GET /page.htm
	Uses wget

- 101 downloads example.mp3 and page.htm from 151 using http
- 154 downloads example.gif from 151 using http

#### Recovered data is in the folder Part2/content
#### PCAP is in the folder Part2/dump
