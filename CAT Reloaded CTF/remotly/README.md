## Description
`Hi My Name Is Mosaa Just small Hacker and searching for a work remotely`

##### website 
![Screenshot_20230729_122424](https://github.com/kiro6/writeups-ctfs/assets/57776872/d297f89a-20d5-4868-8cba-eec37148e4e7)



##### the website was using parameter `mosaa` to construct web pages:
```bash
curl "http://185.69.167.144:8090/Remotely/?mosaa\=contact" 

<h1><center>Hi My Name Is Mosaa Just small Hacker</center></h1><!DOCTYPE html>  
<html>  
<head>  
   <meta charset="utf-8">  
   <meta name="viewport" content="width=device-width, initial-scale=1">  
   <title>Mosaa Profile</title>  
</head>  
<body>  
   <center>  
       <form method="GET" action="">  
           <a href="?mosaa=index">Index</a>  
           <br><br>  
           <a href="?mosaa=contact">Contact Me</a>  
       </form>  
   </center>  
  
</body>  
</html>%

```

##### it is maybe a file inclusion , i tired  many techniques and found that  `../` , `php` and `http` was blocked then i tried data wrapper 
![Screenshot_20230729_124002](https://github.com/kiro6/writeups-ctfs/assets/57776872/a33702bd-9d13-4105-8752-3b3a151bfe9e)


##### it worked and here is our flag 
`CATF{NiC3_Y0u_Hack3d_Mosaa}`
