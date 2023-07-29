## challenge description
`once you find it you will find your gift in Flag.txt`

##### there was a contact page in the website with file upload image functionality , so lets try insecure file upload 
![[Screenshot 2023-07-29 at 14-15-16 Contact Us.png]]


##### the upload function only accepts png and jpg extensions , so i tried to use a shell with png signature 
![[Screenshot_20230729_142920.png]]

##### now we succeed to upload our shell (that does not matter anyway we will see), now we want to get the path for it 

##### there are many ways to do that one of them to make the file name too big which will raise an error revealing the path
![[Screenshot_20230729_143207.png]]

##### the path is `Sup3r_S3cret_H1dd3n/` , back to the challenge description `once you find it you will find your gift in Flag.txt` our flag is in this path
```bash
curl "http://185.69.167.144:2023/Sup3r_S3cret_H1dd3n/Flag.txt"  

CATF{Ezzz_4_U_Don't_Forget_Palestine_!N_0ur_H34rts3>}
```
