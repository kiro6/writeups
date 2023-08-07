## challenge description `Can you find a way to login as the administrator of the website and free nginxatsu?` , we have login and register page 
![Screenshot 2023-08-07 at 04-14-48 nginxatsu](https://github.com/kiro6/writeups-ctfs/assets/57776872/a99c1a03-4b26-4100-b4a6-ecb6f3a299bb)

## made an account and logged in , there is a functionality to make your own server config , i just used what is default which is a route to storage endpoint which have directory indexing
![Screenshot 2023-08-07 at 04-15-18 nginxatsu](https://github.com/kiro6/writeups-ctfs/assets/57776872/6d80b3b9-64b9-49d7-8a14-4be1ba8b8779)

## chech the endpoint we have database backup file 
![Screenshot 2023-08-07 at 04-15-36 Index of _storage_](https://github.com/kiro6/writeups-ctfs/assets/57776872/79499dd6-cb02-48b2-af89-9509d2d5f951)

## downloaded and checked it , we have `nginxatsu-adm-01@makelarid.es` which seems to be admin email and `e7816e9a10590b1e33b87ec2fa65e6cd` which seems to be hashed password
```bash
$ sqlite3 database.sqlite
SQLite version 3.38.5 2022-05-06 15:25:27
Enter ".help" for usage hints.
sqlite> SELECT name FROM sqlite_master WHERE type='table';
migrations
sqlite_sequence
users
password_resets
failed_jobs
nginx_configs
sqlite> select * from users
   ...> ;
1|jr|nginxatsu-adm-01@makelarid.es|e7816e9a10590b1e33b87ec2fa65e6cd|k0ZgIBubWFdSuqAjcrx0ZIbPBCcgMLLCUcvd4ygAchkHYMmZDBLtWA9rLNO5SNQMiggY||2023-08-07 01:01:17|2023-08-07 01:01:17
2|Giovann1|nginxatsu-giv@makelarid.es|ebd9e5e3bd3b3fc832d697d36bc5641a|Sxpt3r1OiH0vTyEkSRToNtqKAGdAFzOYrJIeSnFoNRaeOCko8xWePD0GQfpknu98Wgm6||2023-08-07 01:01:17|2023-08-07 01:01:17
3|me0wth|nginxatsu-me0wth@makelarid.es|9981a1fe9c5381fcc6cd40d39e15c976|TixBNDRuxhoVo6hjSjSK3CqLzVFCRedBSLXefnTzlvYODIBhdU0JSMmsvrmxgEoBsBwN||2023-08-07 01:01:17|2023-08-07 01:01:17
```
## crack passowrd
```
$ dcode e7816e9a10590b1e33b87ec2fa65e6cd

    __                         __
  |/  |                   | / /
  |   | ___  ___  ___  ___|  (
  |   )|___)|    |   )|   )| |___ \   )
  |__/ |__  |__  |__/ |__/ | |     \_/
                                    /
[+] Cracked MD5 Hash : adminadmin1
[+] Decoded from Hex : çnY
                          3¸~ÂúeæÍ
```

## login as admin 
![Screenshot 2023-08-07 at 04-18-51 nginxatsu](https://github.com/kiro6/writeups-ctfs/assets/57776872/ee94d6e4-254e-4368-8b61-cacacd7842f9)

## and we have the flag 
```
HTB{ng1ngx_r34lly_b3_sp1ll1ng_my_w3ll_h1dd3n_s3cr3ts??}
```

