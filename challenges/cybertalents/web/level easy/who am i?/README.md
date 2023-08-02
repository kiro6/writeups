## we have a login page , open inspect and i found Guest user name and password  
![Screenshot_20230802_122104](https://github.com/kiro6/writeups-ctfs/assets/57776872/9cc2c5e3-819e-4dfa-8a21-0333650f40b1)

## when you enter there is a page with this message appear  `Access Denied. You have no admin priviliges, Please login with an administrator account`  , and there is a cookie `Authentication` which seems to be base64 encoded 
![Screenshot 2023-08-02 at 12-23-06 URL Decode From Base64 - CyberChef](https://github.com/kiro6/writeups-ctfs/assets/57776872/223b955d-5777-46ed-a9c4-7319c0e61730)

## I changed the cookie to `Login=administrator` and sent the request again 
![Screenshot_20230802_122530](https://github.com/kiro6/writeups-ctfs/assets/57776872/37f4a71e-5afc-4d77-ac2e-cb1c87e792e0)

## and here is our flag 
```
FLag{B@D_4uTh1Nt1C4Ti0n}
```
