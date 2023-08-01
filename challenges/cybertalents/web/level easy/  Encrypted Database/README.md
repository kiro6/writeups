## we have blog , i opened inpsect elemnts and found interesting url `admin/assets/app.js`

![Screenshot_20230801_172420](https://github.com/kiro6/writeups-ctfs/assets/57776872/4ad7e74e-420a-43f1-ae21-93a78413abb5)

## I accessed `/admin` , and found hidden paramter contains another interesting url `secret-database/db.json`

![Screenshot_20230801_172437](https://github.com/kiro6/writeups-ctfs/assets/57776872/e945ce9a-534b-48a7-95ec-5544d72ec427)

## `/admin/secret-database/db.json` will return a json contains 
```json
flag :"ab003765f3424bf8e2c8d1d69762d72c"
```

## i tried to sumbit the flag , but this was not the flag it seems to be encoded , hashed ...etc  , so i used [Decodify](https://github.com/s0md3v/Decodify) tool 
```bash
$ dcode ab003765f3424bf8e2c8d1d69762d72c

    __                         __      
  |/  |                   | / /        
  |   | ___  ___  ___  ___|  (         
  |   )|___)|    |   )|   )| |___ \   )
  |__/ |__  |__  |__/ |__/ | |     \_/ 
                                    /  
[+] Cracked MD5 Hash : badboy
[+] Decoded from Hex : «7eóBKøâÈÑÖb×,
```

## our flag is `badboy`
