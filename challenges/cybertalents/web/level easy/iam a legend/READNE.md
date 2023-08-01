## we have only login page
![Screenshot 2023-08-01 at 15-08-20 Iam A Legend](https://github.com/kiro6/writeups-ctfs/assets/57776872/01d82ec5-f00b-478d-b1ae-05cded2ff94d)

## using I send `'` to check for sqli and by using burpsuite i intercepted the request, but i noticed there is an alert saying `wrong password` appeared even the request is intercepted

## so it is a frontend function , incpect the code and found a script encoded in jsfuck , i tried to decode it but alot of tools and website did not recoginse it until i found [deobfuscatejavascript](deobfuscatejavascript.com/)

## after decoding it the result : 
```js
String.fromCharCode(102, 117, 110, 99, 116, 105, 111, 110, 32, 99, 104, 101, 99, 107, 40, 41, 123, 10, 10, 118, 97, 114, 32, 117, 115, 101, 114, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 91, 34, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 34, 93, 40, 34, 117, 115, 101, 114, 34, 41, 91, 34, 118, 97, 108, 117, 101, 34, 93, 59, 10, 118, 97, 114, 32, 112, 97, 115, 115, 32, 61, 32, 100, 111, 99, 117, 109, 101, 110, 116, 91, 34, 103, 101, 116, 69, 108, 101, 109, 101, 110, 116, 66, 121, 73, 100, 34, 93, 40, 34, 112, 97, 115, 115, 34, 41, 91, 34, 118, 97, 108, 117, 101, 34, 93, 59, 10, 10, 105, 102, 40, 117, 115, 101, 114, 61, 61, 34, 67, 121, 98, 101, 114, 34, 32, 38, 38, 32, 112, 97, 115, 115, 61, 61, 32, 34, 84, 97, 108, 101, 110, 116, 34, 41, 123, 97, 108, 101, 114, 116, 40, 34, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 67, 111, 110, 103, 114, 97, 116, 122, 32, 92, 110, 32, 70, 108, 97, 103, 58, 32, 123, 74, 52, 86, 52, 95, 83, 99, 114, 49, 80, 116, 95, 49, 83, 95, 83, 48, 95, 68, 52, 77, 78, 95, 70, 85, 78, 125, 34, 41, 59, 125, 32, 10, 101, 108, 115, 101, 32, 123, 97, 108, 101, 114, 116, 40, 34, 119, 114, 111, 110, 103, 32, 80, 97, 115, 115, 119, 111, 114, 100, 34, 41, 59, 125, 10, 10, 125)
```
## the code is sonstructing a string using fromCharCode function , using the browser console the output will be : 
```js
function check(){

var user = document["getElementById"]("user")["value"];
var pass = document["getElementById"]("pass")["value"];

if(user=="Cyber" && pass== "Talent"){alert("                      Congratz \\n Flag: {J4V4_Scr1Pt_1S_S0_D4MN_FUN}");} 
else {alert("wrong Password");}

}
```

## and here is out flag

```
FLAG{J4V4_Scr1Pt_1S_S0_D4MN_FUN}
```
