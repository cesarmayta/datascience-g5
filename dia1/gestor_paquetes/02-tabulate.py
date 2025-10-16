from tabulate import tabulate

table = [
    ["4111212","cesar mayta","cesar@gmail.com"],
    ["4111212","cesar mayta","cesar@gmail.com"],
    ["4111212","cesar mayta","cesar@gmail.com"],
      ]

cabeceras = ["DNI","NOMBRE","EMAIL"]

print(tabulate(table,headers=cabeceras,tablefmt="grid"))