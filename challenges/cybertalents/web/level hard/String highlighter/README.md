## we have function that take input and print it on the server 
![Screenshot 2023-08-11 at 08-57-25 Welcome to String highlighter 1](https://github.com/kiro6/writeups-ctfs/assets/57776872/1ed0cbdd-9ca8-49f5-bb54-d6da8a6c8be6)


## using burp i tried some input the `"` was triggering an error 
![Screenshot_20230811_085549](https://github.com/kiro6/writeups-ctfs/assets/57776872/58f309b4-3baf-4449-af03-3b2777a89c85)


## based on the functionality i thought the backend code will be somthing like this 
```php
<?php

$input = $_POST['stp'];

eval("echo \"$input\" ; ");

//other staff
?>
```

## so i tried to escape inject php code to get RCE  but there was 2 problem
- the server always responde with server error
- php danger functions filter

## first problem i thought the server error because there is some string which is not handled yet so i tried `stp=red:"; echo "s` but there was always error i thought maybe it is not using echo to print stuff , so i tried `print()`
![Screenshot_20230811_090905](https://github.com/kiro6/writeups-ctfs/assets/57776872/67cc48e8-a56a-4b0c-b08b-b847a4b754af)

## i was right lets inject php code , here is the second problem arise , i found that the `eval()` was not filtered so i used concatenating to list dir files 
![Screenshot_20230811_085555](https://github.com/kiro6/writeups-ctfs/assets/57776872/ca6772bd-032b-4c51-948c-8a75c57744ee)

## final step lets get the flag
![Screenshot_20230811_085601](https://github.com/kiro6/writeups-ctfs/assets/57776872/14cb7912-a381-426e-b671-0f8d8ba68576)

```
kshd125fddw
```
