# Process input file into a list of tuples (command, value)
def read_file_input(filename):
    input_tuple_list = []
    with open(filename) as f:
        for line in f:
            try:
                cmnd_val = line.strip().split()
                input_tuple_list.append((cmnd_val[0], int(cmnd_val[1])))
            except:
                print("Invalid line in file")
                pass
    
    return input_tuple_list

# Part 1: Compute submarine depth and horizontal position
def compute_depth_position(data):
    depth = 0
    horizontal_position = 0
    
    for i in range(len(data)):
        if data[i][0] == 'forward':
            horizontal_position += data[i][1]
        elif data[i][0] == 'down':
            depth += data[i][1]
        elif data[i][0] == 'up':
            depth -= data[i][1]

    return depth * horizontal_position

# Part 2: Compute submarine depth and horizontal position with aim
def depth_position_with_aim(data):
    aim = 0 
    depth = 0
    horizontal_position = 0
    for i in range(len(data)):
        if data[i][0] == 'forward':
            horizontal_position += data[i][1]
            depth += data[i][1] * aim
        elif data[i][0] == 'down':
            aim += data[i][1]
        elif data[i][0] == 'up':
            aim -= data[i][1]

    return depth * horizontal_position

# Main function
def main():
    data = read_file_input('input.txt')
    print('-----Part 1-----')
    print(compute_depth_position(data))
    print('-----Part 2-----')
    print(depth_position_with_aim(data))


if __name__ == '__main__':
    main()