def fuel_calculation(mass):
    fuel = mass//3 - 2
    if fuel <= 0:
        return 0
    return fuel + fuel_calculation(fuel)


with open("input.txt", "r") as file:
    data = map(int, file.read().strip().split("\n"))
    total = sum([fuel_calculation(mass) for mass in data])
    print(total)
    
