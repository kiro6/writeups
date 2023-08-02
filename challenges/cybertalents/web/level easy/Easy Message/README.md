## we have a login page which is not vuln 

## check robots 
```bash
$ curl "http://wcamxwl32pue3e6mxwl322yue3e6ndvjrx94fezy-web.cybertalentslabs.com/robots.txt"
User-agent: *
Disallow: /?source
```

## check ?source , you will find php code , decode the base64 it is `Cyber-Talent`
```php
 <?php

$user = $_POST['user'];
$pass = $_POST['pass'];

include('db.php');

if ($user == base64_decode('Q3liZXItVGFsZW50') && $pass == base64_decode('Q3liZXItVGFsZW50'))
    {
        success_login();
    }
    else {
        failed_login();
}

?> 
```

## login in using `Cyber-Talent` you will find this page
```html
<br><br><b>I Have a Message For You<br><br><br>
..-. .-.. .- --. -.--. .. -....- -.- -. ----- .-- -....- -.-- ----- ..- -....- .- .-. ...-- -....- -- ----- .-. ... ...-- -.--.-
```

## using cyberchef decode the message 
![Screenshot 2023-08-02 at 13-29-10 From Morse Code - CyberChef](https://github.com/kiro6/writeups-ctfs/assets/57776872/53511f15-c74b-4815-a235-dfea09e320a3)

 ## and here is our flag
```
FLAG(I-KN0W-Y0U-AR3-M0RS3)
```
