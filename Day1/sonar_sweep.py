# Process input file into a list
def get_input(filename):
    input_list = []
    with open(filename) as f:
        for line in f:
            input_list.append(int(line.strip()))
    
    return input_list

# Sona Sweep part 1
def single_depth_increase_count(data):
    depth_count = 0
    for i in range(len(data)):
        if data[i] > (data[i-1] or 0):
            depth_count += 1

    return depth_count

# Sona Sweep part 2 (Windowing)
def window_depth_increase_count(data):
    depth_count = 0
    for i in range(len(data) - 3):
        window1 = [data[i], data[i + 1], data[i + 2]]
        window2 = [data[i + 1], data[i + 2], data[i + 3]]
        if sum(window2) > sum(window1):
            depth_count += 1

    return depth_count

def main():
    data = get_input('input.txt')
    # print(single_depth_increase_count(data))
    print(window_depth_increase_count(data))

if __name__ == '__main__':
    main()