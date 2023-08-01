## challenge description `Webmaster developed a simple script to do cool effects on your name, but his code not filtering the inputs correctly execute javascript alert and prove it.` , XSS ofcourse

## open dveloper tools and check Debugger , you will find where is your input reflected 

## tried `<script>alert()</script>`

![Screenshot_20230801_164329](https://github.com/kiro6/writeups-ctfs/assets/57776872/26c9914b-435e-44de-9728-083916bf410f)

## there is more than one way to do xss , then i tried `<img src=x onerror=alert()>`

![Screenshot_20230801_164341](https://github.com/kiro6/writeups-ctfs/assets/57776872/33b0b429-6bb0-4615-bd04-e4b255c50116)

## and here is our flag
```
ciyypjz
```
