with open("input.txt", "r") as file:
    data = file.read().split("\n")
    for count, wire in enumerate(data):
        data[count] = wire.split(",")

def check_if_intercept(start_pos, end_pos, other):
    start_pos_other = other[0]
    end_pos_other = other[1]
    if min(start_pos[0], end_pos[0]) < max(start_pos_other[0], end_pos_other[0]) <= max(start_pos[0], end_pos[0]):
        return True

    if min(start_pos[1], end_pos[1]) < max(start_pos_other[1], end_pos_other[1]) <= max(start_pos[1], end_pos[1]):
        return True
    return False

def where_intercept(start_pos, end_pos, other):
    start_pos_other = other[0]
    end_pos_other = other[1]

    if start_pos[0] > start_pos_other[0]:
         return (start_pos[0], start_pos_other[1])

    else:
        return (start_pos[1], start_pos_other[0])


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

positions = []
for count, wire in enumerate(data):
    current_pos = [0, 0]
    for instruction in wire:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        if count == 0:
            positions.append(current_pos)

            if direction == "U":
                current_pos[1] += magnitude
            
            if direction == "D":
                current_pos[1] -= magnitude
            
            if direction == "R":
                current_pos[0] += magnitude
            
            if direction == "L":
                current_pos[0] -= magnitude
        else:

            old_pos = current_pos.copy()
            
            if direction == "U":
                current_pos[1] += magnitude
            
            if direction == "D":
                current_pos[1] -= magnitude
            
            if direction == "R":
                current_pos[0] += magnitude
            
            if direction == "L":
                current_pos[0] -= magnitude
    
            for count, pos in enumerate(positions[:len(positions)-1]):
                if check_if_intercept(old_pos, current_pos, [pos, positions[count+1]]):
                    print(f"Distance was {manhattan_distance([0, 0], [])}")
        
