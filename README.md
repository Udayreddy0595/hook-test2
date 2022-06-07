List of tasks:

Git commands:

1.How do you set up a script to run every time a repository receives new commits through push?
Ans:

```
$ mkdir hook-test2
$ cd hook-test2/
$ git init
create remote repo 
$ git remote add origin <url> 
$ git remote add origin git@github.com:uday/hook-test2.git
$ cd .git/hooks

$ vi post-commit
#/bin/bash
echo "this script can be run after commit"
$ chmod +x post-commit
```

After you done with this successfully you will be able to see the script gets executed each time you do run push command.

2. How do you find a list of files that have changed in a particular commit?

Ans:
We can use is git diff command to check the list of files
Syntax of this command is:
```
git diff-tree --no-commit-id --name-only -r <commit_SHA>
```
=======================================================================================================================================================
Monitoring using scripts:

1. Monitor a log file, detect a pattern detection, send an email on detection

Ans:
these examples we'll place it into the /opt/logalert directory. Make sure you are root (superuser) to install this
```
mkdir /opt/logalert
curl -L https://github.com/jhuckaby/logalert/releases/latest/download/logalert-linux > /opt/logalert/logalert.bin
chmod 755 /opt/logalert/logalert.bin
/opt/logalert/logalert.bin

```
Alternatively, if you already have Node.js on your server, you can install LogAlert via npm like this:

sudo npm install -g logalert
This has the benefit of allowing you to easily add it as a startup service:

sudo logalert boot
And start it as a background daemon:

sudo logalert start

LogAlert is configured via a JSON text file named config.json
```

example file:

{
	"monitors": [
		{
			"name": "Test Monitor",
			"path": "/Users/me/logalert/test.txt",
			"match": "ERROR",
			"email": "myemail@server.com"
		}
	],
	"mail_settings": {
	"host": "mail.avaamo.in",
	"port": 587,
	"secure": false,
	"auth": {
		"user": "uday",
		"pass": "********"
	},
	"from": "uday@avaamo.in"
},
	"sleep": 5,
	"echo": true,
	"verbose": 3
}
```
Note that many SMTP servers require authentication.
This is done by specifying an auth object. Here is an example using my local ISP's mail server.
They listen on a different port (587), and require user authentication for mail relay:

Single File
For monitoring single files, you need to specify the full filesystem path to the file in your monitor configuration via the path property.
 Here is an example for Linux or macOS:
"path": "/home/jsmith/files/mylog.txt"

Multiple Files
For monitoring multiple files at once, you can use a filesystem glob. This is a special syntax for specifying things like wildcards (i.e. match any file in a directory).
 For example:
"path": "/home/jsmith/files/*.txt"
===========================================================================================================================================================================
2. Monitor process particular process on an instance, send an email on incase of state change like process got stopped, taking more CPU that threshold

Ans:
```
$ vi /opt/scripts/cpu-alert.sh

#!/bin/bash
cpuuse=$(cat /proc/loadavg | awk '{print $3}'|cut -f 1 -d ".")
if [ "$cpuuse" -ge 90 ]; then
SUBJECT="ATTENTION: CPU load is high on $(hostname) at $(date)"
MESSAGE="/tmp/Mail.out"
TO="avavmo@gmail.com"
  echo "CPU current usage is: $cpuuse%" >> $MESSAGE
  echo "" >> $MESSAGE
  echo "+------------------------------------------------------------------+" >> $MESSAGE
  echo "Top 20 processes which consuming high CPU" >> $MESSAGE
  echo "+------------------------------------------------------------------+" >> $MESSAGE
  echo "$(top -bn1 | head -20)" >> $MESSAGE
  echo "" >> $MESSAGE
  echo "+------------------------------------------------------------------+" >> $MESSAGE
  echo "Top 10 Processes which consuming high CPU using the ps command" >> $MESSAGE
  echo "+------------------------------------------------------------------+" >> $MESSAGE
  echo "$(ps -eo pcpu,pid,user,args | sort -k 1 -r | head -10)" >> $MESSAGE
  mail -s "$SUBJECT" "$TO" < $MESSAGE
  rm /tmp/Mail.out
else
echo "Server CPU usage is in under threshold"
  fi
```
I dont have smtp server setup that could be the reason not able to execute above code
============================================================================================================================================================================
Security:

1. Show how to block ports in linux

Ans:
```
sudo iptables -A INPUT -p tcp --dport 8000 -j DROP
```
=============================================================================================================================================================================
2. show how to setup port forwarding in linux
Ans:
				     ```
 local port farwarding:
 ssh -L local_port:destination_server_ip:remote_port ssh_server_hostname
 ssh –L 5901:188.17.0.5:4492 ubuntu@<hostname>
 
 remote port forwarding:
 ssh -R remote_port:localhost:local_port ssh_server_hostname
 ssh –R 8080:localhost:5534 ubuntu@<hostname>
	```

=============================================================================================================================================================================
Network:

1. Show list of processes using the network
```
Ans:
sudo netstat -tunpl 
sudo netstat -tunp | grep 433
```
================================================================================================================================================================
2. Show the list of IPs a process is connected to 

Ans:
```
netstat -tn 2>/dev/null  | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
netstat -tn 2>/dev/null | grep :22 | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr
```
===================================================================================================================================================================
3.Show how to list open files and kill processes tied to a user
 
Ans:
```
 kill -9 $(lsof -t -u uday)
```
===================================================================================================================================================================
Code:
Write a short program that prints each number from 1 to 100 on a new line.
For each multiple of 3, print "AVA" instead of the number.
For each multiple of 5, print "AMO" instead of the number.
For numbers which are multiples of both 3 and 5, print "AVAAMO" instead of the number.

Ans:
Shell Script:
```
#!/bin/bash
for ((i=1;i<=100;i++)); do
    if ! ((i%15)); then
        echo AVAAMO
    elif ! ((i%3)); then
        echo AVA
    elif ! ((i%5)); then
        echo AMO
    else
        echo $i
    fi;
done


python:


def findMultiples(n):
        a = 3
        b = 5
        for i in range(1,n+1):
                s = ""
                # print  multiple of 3
                if (i == a):
                        a = a + 3
                        s = s + "AVA"

                # print multiple of 5
                if (i == b):
                        b = b + 5
                        s = s + "AMO"
                if (s == ""):
                        print(i)
                else:
                        print(s)

# Driver Code
if __name__ == '__main__':
        findMultiples(100)
```
================================================================================================================================================================================		
Docker:
1. Create a sample docker container with a Node.js Express app and demonstrate the installation.
Guidelines :
● You should be able to find what system packages are needed by looking through the app
● You should not need to change the app code in any way
● The app should be running as a non-privileged user
● The app should be automatically restarted if crashes or is killed
● The app should maximize all of the available CPUs
● Timezone should be in IST
● Follow best practices when writing a dockerfile
```
Dockerfile:

FROM node:16-alpine
ENV TZ=Asia/Kolkata
RUN apk add --update tzdata
# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

EXPOSE 8080
USER node
CMD [ "node", "server.js" ]
```
===================================================================================================================
```
 .dockerignore

node_modules
npm-debug.log

```

===========================================================================================
package.json
```

{
  "name": "docker_node_app",
  "version": "1.0.0",
  "description": "Node.js on Docker",
  "author": "uday",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.16.1"
  }
}
```
=============================================================================================================
```
server.js

'use strict';

const express = require('express');

// Constants
const PORT = 8080;
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('HI... NODEJS APPLICATION');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
```

sudo docker build -t nodeapp:v1 .

sudo docker run -p 8089:8080 --restart=on-failure -d nodeapp:v1

sudo docker ps 
sudo docker exec -it bc5650a97cf2 sh		
		

will upload this file and video both in github and drive
		thanks
		
		























 






















