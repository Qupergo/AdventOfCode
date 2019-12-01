
with open("input.txt", "r") as file:
    data = file.read().strip().split("\n")
    total = sum([(int(num)//3-2) for num in data])
    print(total)
        
