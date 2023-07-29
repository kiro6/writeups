import flag
from rich.console import Console
from rich.table import Table

console = Console()
table = Table()

class CATS:
    def __init__(meow, name):
        meow.name = name

def meow(name,cats):
        console.print(f"[blue]Prrrrr [yellow]{name}[/yellow] ₍^⸝⸝> ·̫ <⸝⸝ ^₎[/blue]".format(cats=cats))


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
