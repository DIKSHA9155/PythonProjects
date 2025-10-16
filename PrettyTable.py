from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Squirtle", "Charmander", "Pikachu"])
table.add_column("Type", ["Water", "Fire", "Electric"])
table.align = "l"
print(table)

