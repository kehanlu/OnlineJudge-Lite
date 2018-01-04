docker run -it -d --memory=32M --memory-swap=32M --cpu-quota=75000 -v /tmp/oj/:/home/jail/ --name="oj_sandbox"  ubuntu /bin/sh 
