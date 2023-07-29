<?php

function send($link)
{
    $curl_handle=curl_init();
    curl_setopt($curl_handle,CURLOPT_URL,$link);
    curl_setopt($curl_handle,CURLOPT_CONNECTTIMEOUT,2);
    curl_setopt($curl_handle,CURLOPT_RETURNTRANSFER,1);
    $buffer = curl_exec($curl_handle);
    curl_close($curl_handle);

    if (empty($buffer))
    {
        return "Nothing returned from url.<p>";
    }

    else
    {
        return $buffer;
    }
}


if (!empty($_GET['url']))
{
    $url=$_GET['url'];

    if(preg_match('/^http/',$url) || !preg_match('/file/',$url))
    {
        echo send($url);
    }
    else
    {
        die("Don't Hack Me Plzzz");
    }
}
?>



<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    Hello
</body>
</html>