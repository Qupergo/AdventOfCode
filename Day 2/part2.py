
with open("input.txt", "r", encoding = "utf-16") as file:
    data = list(map(int, file.read().split(",")))



def computer(input_data):
    data = input_data.copy()
    for count, num in enumerate(data):
        if (count) % 4 == 0:
            total = 0
            if num == 1:
                # Addition
                for i in range(2):
                    total += data[data[count + i + 1]]

                data[data[count + i + 2]] = total

            elif num == 2:
                # Multiplication
                total = 1
                for i in range(2):
                    total *= data[data[count + i + 1]]
                data[data[count + i + 2]] = total

            elif num == 99:
                # Stop
                break

    return data

for i in range(99):
    for j in range(99):
        data[1] = i
        data[2] = j
        if computer(data)[0] == 19690720:
            print(f"{i} and {j}")
