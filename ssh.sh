sslocal -s jn.coob.pub -p 10573 -k "1eb3d4" -t 600 > /tmp/ssh.log & 
polipo proxyPort=1090 socksParentProxy=localhost:1080 logFile=/tmp/polipo.log &
exit
