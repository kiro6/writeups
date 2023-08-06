# iniecto easy challenge 

## first we have a page with only an image , using fuzzing i found GET parameter `name` which reflect the input in the page 

## i found that inserting `"` raise an error revealing that the code using `eval()` so maybe the code in it using `echo` so may can inject our code

## the site was filtering most of dangerous functions and have char limit to 39 chars only 

## i used `var_dump(scandir'./')`  to view directory files i found `flag.php` and `challenge~` which i read to view source code of challenge and check what is filtered and how

## final payload 
```
";(sy.(st).em)(c.'a'.t.' *');"
```

## and our flag is 
```
ASCWG{yeah_mrx_come_her!!!!!!!!!!!!!!!!}
```