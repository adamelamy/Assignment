# Assignment 1 Sliding Part

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

# Assignment 2
## Part 1

Linux username: linuxuser  
Linux password: xPT1Mh76uV!FX8F  
Windows username: windowsuser  
Windows password: epBAW915lC&T3sh  

We used an offline random password generator to generate these passwords. The reason of choosing a random password is to prevent potential dictionary attacks. Also, by including uppercase, lowercase, numbers and symbols, we increase the entropy of the passwords, making it more computational intensive to crack it. 

___________________________________________________________________________

## Part 2  
***
### ftp Linux:
Linux VM already has ftp installed, but we have to install vsftpd to set up the configurations.
1. Download vsftpd here: https://packages.ubuntu.com/trusty/vsftpd
2. scp to move the package into your VM
3. sudo dpkg -i 'package'; to install vsftpd
4. Create a root folder for the anonymous users (ie. /var/ftp/)
5. Once installed, edit the configurations at '/etc/vsftpd.conf'
6. In '/etc/vsftpd.conf', look for the line 'Allow anonymous FTP? (Disable by default)' and uncomment 'anonymous-enable=YES'. If the line is not found, just add it to the file.
7. Next, we comment out 'local-enable=YES' to prevent local user to log in. If the line is not found, just add it to the file.
8. Next, we add 'anon_root=/var/ftp/'
9. Next, we add 'no_anon_password=YES' so it doesn't prompt for password
10. The vsftpd.conf should have these 4 lines: 
    'anonymous-enable=YES' '#local-enable=YES' 'anon_root=/var/ftp/' 'no_anon_password=YES'
11. Run 'sudo service vsftpd restart' to restart ftp server

Testing using Windows Server:

    PS C:\Users\test> ftp 10.229.6.4
    Connected to 10.229.6.4.
    220 (vsFTPd 3.0.2)
    User (10.229.6.4:(none)): username
    530 This FTP server is anonymous only.
    Login failed.

    PS C:\Users\test> ftp 10.229.6.4
    Connected to 10.229.6.4.
    220 (vsFTPd 3.0.2)
    User (10.229.6.4:(none)): anonymous
    230 Login successful.
    ftp> ls
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    ftpcontent.pdf
    pub
    sample.text
    226 Directory send OK.
    ftp: 37 bytes received in 0.00Seconds 37000.00Kbytes/sec.

Testing using Linux VM:

    keanweng@host-10-229-100-135:~$ ftp 10.229.6.4
    Connected to 10.229.6.4.
    220 (vsFTPd 3.0.2)
    Name (10.229.6.4:keanweng): username
    530 This FTP server is anonymous only.
    Login failed.

    keanweng@host-10-229-100-135:~$ ftp 10.229.6.4
    Connected to 10.229.6.4.
    220 (vsFTPd 3.0.2)
    Name (10.229.6.4:keanweng): anonymous
    230 Login successful.
    Remote system type is UNIX.
    Using binary mode to transfer files.
    ftp> ls
    200 PORT command successful. Consider using PASV.
    150 Here comes the directory listing.
    -rw-r--r--    1 0        0              60 Mar 15 21:34 ftpcontent.pdf
    drwxr-xr-x    2 0        0            4096 Mar 15 21:28 pub
    -rw-r--r--    1 0        0               8 Mar 15 21:31 sample.text
    226 Directory send OK.

***
### ftp Windows Server:

We follow this guide closely: https://vpsie.com/knowledge-base/how-to-setup-ftp-server-users-on-windows-2012-r2/
1. For '1- Enable Web Server (IIS) role and FTP Server role service.', follow all the steps.
2. Skip '2- Create FTP users'
3. For '3- Configuring FTP global IIS settings.', follow steps 1 to 6.
4. For '4- Creating FTP site.', follow steps 1 - 19 only. Then in 'Authorization' section, set 'Allow access to:' to 'Anonymous Users' and set 'Permission' accordingly.
5. For '5- IIS Firewall setup.', follow all the steps.
6. For '6-Windows Firewall setup.', follow all the steps.

Testing using Windows Server:

    PS C:\Users\Administrator> ftp 10.229.6.5
    Connected to 10.229.6.5.
    220 Microsoft FTP Service
    User (10.229.6.5:(none)): username
    331 Password required
    Password:
    530-User cannot log in.
     Win32 error:   The user name or password is incorrect.
     Error details: An error occurred during the authentication process.
    530 End
    Login failed.

    PS C:\Users\Administrator> ftp 10.229.6.5
    Connected to 10.229.6.5.
    220 Microsoft FTP Service
    User (10.229.6.5:(none)): anonymous
    331 Anonymous access allowed, send identity (e-mail name) as password.
    Password:
    230 User logged in.
    ftp> ls
    200 PORT command successful.
    125 Data connection already open; Transfer starting.
    ftpcontent.pdf
    test.txt
    226 Transfer complete.
    ftp: 29 bytes received in 0.00Seconds 29000.00Kbytes/sec.

Testing using Linux VM:

    keanweng@host-10-229-100-135:~$ ftp 10.229.6.5
    Connected to 10.229.6.5.
    220 Microsoft FTP Service
    Name (10.229.6.5:keanweng): username
    331 Password required
    Password:
    530 User cannot log in.
    Login failed.

    keanweng@host-10-229-100-135:~$ ftp 10.229.6.5
    Connected to 10.229.6.5.
    220 Microsoft FTP Service
    Name (10.229.6.5:keanweng): anonymous
    331 Anonymous access allowed, send identity (e-mail name) as password.
    Password:
    230 User logged in.
    Remote system type is Windows_NT.
    ftp> ls
    200 PORT command successful.
    125 Data connection already open; Transfer starting.
    03-16-19  12:32PM                   51 ftpcontent.pdf
    03-15-19  02:19PM                    0 test.txt
    226 Transfer complete.
 
***
### http Windows Server:

Setting up a http server (Web Site) is fairly similar to setting up ftp. By default, IIS already has a HTTP Web Site running called "Default Web Site"
1. Open Server Manager, go to Tools > Internet Information Services (IIS) Manager
2. In the left pane, expand the server icon (in the tree below the option Start Page) and navigate to 'Sites' > 'Default Web Site'.
3. In 'Authentication', make sure everything is disabled except for 'Windows Authentication'
4. In 'Authorization Rules', delete all rules and 'Add Allow Rule...' on the right.
5. Select 'Specified users' and add the regular user (in our case, its windowsuser)
6. Done! Now only 'windowsuser' can access the HTTP Web Site
7. (optional) We disabled 'Default Documents' and enabled 'Directory Browsing'

***
### http Linux Server:

We have to install Apache in the Linux VM to host a HTTP server. Then, we use mod-authnz-external to do a custom authentication with the Linux password file.
1. Download these packages from: https://packages.ubuntu.com/ and scp to Linux VM

        apache2_2.4.7-1ubuntu4.20_amd64.deb
        apache2-bin_2.4.7-1ubuntu4.20_amd64.deb
        apache2-data_2.4.7-1ubuntu4.20_all.deb
        apache2-utils_2.4.7-1ubuntu4.20_amd64.deb
        libapache2-mod-authnz-external_3.3.1-0.1_amd64.deb
        libapr1_1.5.0-1_amd64.deb
        libaprutil1_1.5.3-1_amd64.deb
        libaprutil1-dbd-sqlite3_1.5.3-1_amd64.deb
        libaprutil1-ldap_1.5.3-1_amd64.deb
        pwauth_2.3.8-1_amd64.deb

2. Install all of them using 'sudo dpkg -i *'
3. Pick a root directory for the http server (for our case, /var/www/html/)
4. Edit /etc/apache2/apache2.conf and add the following:  
    /var/www/html/ is our root, linuxuser is our regular user

        <Directory "/var/www/html/">
          AuthType Basic
          AuthName "Authentication Required"
          AuthBasicProvider external
          AuthExternal pwauth
          Require user linuxuser

          Order allow,deny
          Allow from all
        </Directory>

        <IfModule mod_authnz_external.c>
          DefineExternalAuth pwauth pipe /usr/sbin/pwauth
        </IfModule>
        
5. Run 'sudo chmod u+s /usr/sbin/pwauth' to allow setuid permission for pwauth.
6. Run 'sudo service apache2 reload' to restart Apache server
7. Done! Root directory is now /var/www/html and you can put the files there.

If the user account changes their password, this change is automatically reflected. In Linux VM, this is done by having an external authentication (mod-authnz-external) to authenticate with the Linux password file. In Windows Server, the http server already has a Windows Authentication feature that would authenticate with Windows users. The similarity in the two systems is both systems issue a HTTP 401 Challenge that authenticates with the user password. The difference in the two systems is this feature is already built in for Windows Server whereas the Linux VM has to use an external authentication library.


***
## Part 3  

These are the rules used:

    -N LOG_DROP
    -A LOG_DROP -j LOG --log-prefix "DEFAULT VIOLATION" --log-level 7
    -A LOG_DROP -j DROP
    // adding a new chain called LOG_DROP to log on debug level and drop the connection

    -A INPUT -s 10.229.6.0/24 -j ACCEPT
    // complete access to our Linux host from any hosts from our own group's network 

    -A INPUT -p tcp -m tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
    -A INPUT -p icmp -m icmp --icmp-type any -j ACCEPT
    // ssh access and ICMP echo messages to our Linux host from any host from any network

    -A INPUT -s 10.229.0.0/16 -p tcp -m multiport --dports 21,80 -j ACCEPT
    // http and ftp access to our Linux host from any host from the network 10.229.*.*

    -A INPUT -s 10.229.4.0/24 -p tcp -m multiport --dports 21,80 -j LOG_DROP
    -A INPUT -s 10.229.100.51/32 -p tcp -m multiport --dports 21,80 -j LOG_DROP
    -A INPUT -s 10.229.51.0/24 -p tcp -m multiport --dports 21,80 -j LOG_DROP
    // block http and ftp access to our Linux host from any hosts belonging to group 4, 10.229.100.51 and 10.229.51.*

    -A FORWARD -s 10.229.0.0/16 -d 10.229.6.5/32 -p tcp -m multiport --dports 21,80 -j ACCEPT
    // http and ftp access to our Windows host from any host from the network 10.229.*.*

    -A FORWARD -s 10.229.8.0/24 -d 10.229.6.5/32 -p tcp -m multiport --dports 21,80 -j LOG_DROP
    -A FORWARD -s 10.229.100.52/32 -d 10.229.6.5/32 -p tcp -m multiport --dports 21,80 -j LOG_DROP
    -A FORWARD -s 10.229.52.0/24 -d 10.229.6.5/32 -p tcp -m multiport --dports 21,80 -j LOG_DROP
    // block http and ftp access to our Windows host from any hosts belonging to group 8, 10.229.100.52 and 10.229.52.*, then logs it at /var/log/kern.log

    -A FORWARD -d 10.229.6.0/24 -p tcp -m tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
    -A FORWARD -d 10.229.6.0/24 -p icmp -m icmp --icmp-type any -j ACCEPT
    // ssh access and ICMP echo messages to our Windows host from any host from any network

    -A FORWARD -s 10.229.6.0/24 -d 10.229.6.0/24 -j ACCEPT
    // complete access to any hosts from our own group's network from any hosts from our own group's network 

    -A FORWARD -s 10.229.6.5/32 -d 10.229.5.0/24 -j LOG_DROP
    -A FORWARD -s 10.229.6.5/32 -d 10.229.100.52/32 -j LOG_DROP
    -A FORWARD -s 10.229.6.5/32 -d 10.229.52.0/24 -j LOG_DROP
    // block any access to any hosts beloging to group 5, 10.229.100.52, 10.229.52.* from our Windows host, then logs it at /var/log/kern.log

    -A OUTPUT -p tcp -m tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
    -A OUTPUT -p icmp -m icmp --icmp-type any -j ACCEPT
    // (BIDIRECTIONAL) ssh access and ICMO echo messages to any host from any network from our Linux host

    -A OUTPUT -d 10.229.6.0/24 -j ACCEPT
    // (BIDIRECTIONAL) complete access to any host on our network from our Linux host

    -A OUTPUT -d 10.229.0.0/16 -p tcp -m multiport --dports 21,80 -j ACCEPT
    // (BIDIRECTIONAL) http and ftp access to any host from the network 10.229.*.* from our Linux host
   




