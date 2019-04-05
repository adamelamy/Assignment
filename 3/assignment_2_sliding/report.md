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
        Screenshot:

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


