from my_project_console import console
from rich.table import Table

def main():
   
    while True:
        try:
            surface = float(input("Enter a value: "))
            break
        except:
            print("It's not a number")
    #calculate 
    pallete,basket = weight(surface)
    fuge_glue,primer_I = rest_calculate(surface)
    table = Table(title="Resluts")
    table.add_column("meters\u00b2",justify="center",style="cyan")
    table.add_column("pallets",justify="center",style="magenta")
    table.add_column("baskets",justify="center",style="magenta")
    table.add_column("Fuge and Glue(L)",justify="center",style="magenta")
    table.add_column("Primer(L)",justify="center",style="magenta")
    table.add_row(str(surface),str(pallete),str(basket),str(fuge_glue),str(primer_I))

    console.print(table)




def weight(m):
    #total weigt of bricks
    w = m * 35
    #how many pallets
    p = w/800
    #total amount of basket
    b = m/0.7
    return round(p,1), round(b,1)

def rest_calculate(s):
    #total glue and Fuge
    GF = round(s/0.3,1)
    #total primer and I
    PI = round(s/0.8,1)
    return GF,PI

    


if __name__ == "__main__":
    main()