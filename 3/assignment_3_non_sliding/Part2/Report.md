# Part 2
## Step 1

### 1:

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

## Step 2
### 10.229.100.151 Server
	Ping Request to 156 155 154 150 147 144 142 141 139 138 137 136 133 132 131 130 102 101
	Ping Reply to 138 
	Sends /example.gif back in HTTP using multiple tcp fragments
	Sends /example.mp3 back in HTTP using multiple tcp fragments
	Sends /page.htm back in HTTP
	
### 10.229.100.154 Client
	Ping Request to 151
	Ping Reply to 151
	HTTP1.1 GET /example.gif
	Uses wget
	
### 10.229.100.101 Client
	Ping Request to 151
	Ping Reply to 151
	HTTP GET /example.mp3
	HTTP GET /page.htm
	Uses wget

- 101 downloads example.mp3 and page.htm from 151 using http
- 154 downloads example.gif from 151 using http

### Recovered data is in the folder Part2/content
### PCAP is in the folder Part2/dump