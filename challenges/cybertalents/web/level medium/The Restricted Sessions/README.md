## we have this site
![Screenshot 2023-08-11 at 00-20-46 Sessions](https://github.com/kiro6/writeups-ctfs/assets/57776872/92d41b22-ea5d-41da-80ba-64bff3fffda8)

## in the response we have this code, which send paramter `PHPSESSID` to `getcurrentuserinfo.php` endpoint
```js
      if(document.cookie !== ''){
        $.post('getcurrentuserinfo.php',{
          'PHPSESSID':document.cookie.match(/PHPSESSID=([^;]+)/)[1]
        },function(data){
          cu = data;
        });
      }
    
```

## i sent a request without PHPSESSID paramter  , which give me a PHPSESSID  
![Screenshot_20230811_012704](https://github.com/kiro6/writeups-ctfs/assets/57776872/4c2faaa5-63dc-4c98-b620-5c8917b68fa4)

## after i get a session cookie i used this session and requested index.php again 
![Screenshot_20230811_013719](https://github.com/kiro6/writeups-ctfs/assets/57776872/8194fbd9-7b95-49a0-b928-c95d3a7c0f31)

## i accessed `data/session_store.txt` which contained 
```
iuqwhe23eh23kej2hd2u3h2k23
11l3ztdo96ritoitf9fr092ru3
ksjdlaskjd23ljd2lkjdkasdlk
```
## i send paramter `PHPSESSID` to `getcurrentuserinfo.php` endpoint with one of the values i found , we have some info about the user 
![Screenshot_20230811_002213](https://github.com/kiro6/writeups-ctfs/assets/57776872/e6c4acbf-43c9-4632-b7d9-715f4fb07079)


## requested index.php again with the phpsession i found , i requested UserInfo Cookie and we have some info lets try
![Screenshot_20230811_002201](https://github.com/kiro6/writeups-ctfs/assets/57776872/c68c20d0-6fd3-4e97-809f-d02b29c856d3)

## submited the username which i fiund earlier , done we get the flag
![Screenshot_20230811_002206](https://github.com/kiro6/writeups-ctfs/assets/57776872/14b23e96-73ef-44c4-8e07-7aa16587f90c)

```
sessionareawesomebutifitsecure
```
