# Process input file into a list
def read_file_input(filename):
    binary_array = []
    with open(filename) as f:
        for line in f:
            binary_array.append(line.strip())
    
    return binary_array

# Part 1: Compute the power consumption of our submarine using gamma and epsilon rates
def compute_power_consumption(data):
    count_summary = [[0] * 2 for i in range(len(data[0]))]
    gamma, epsilon = "", ""
    # Loop through list of binaries and compute gamma and epsilon
    for i in range(len(data)):
        binary = data[i]
        for j in range(len(binary)):
            if binary[j] == '0':
                count_summary[j][0] += 1
            elif binary[j] == '1':
                count_summary[j][1] += 1

    # Compute gamma and epsilon using the max and min indices of the count
    for i in range(len(count_summary)):
        gamma += str(count_summary[i].index(max(count_summary[i]))) 
        epsilon += str(count_summary[i].index(min(count_summary[i])))

    return int(gamma, 2) * int(epsilon, 2)

# Part 2: Compute oxygen generator rating and CO2 scrubber rating

# Create a utility function that returns sublist based on bit frequency
# data -> input list, bit_idx -> bit position, rating_type: 1 for oxygen generator, 0 for CO2 scrubber
def filter_by_bit(data, bit_idx, rating_type):
    count_summary = [0] * 2
    gamma, epsilon = "", ""
    # Loop through list of binaries and compute gamma and epsilon
    for i in range(len(data)):
        binary = data[i]
        if binary[bit_idx] == '0':
            count_summary[0] += 1
        elif binary[bit_idx] == '1':
            count_summary[1] += 1

    # Compute gamma and epsilon using the max and min indices of the count
    temp_data = []
    # For oxygen generator rating
    if rating_type == 1:
        if count_summary[1] >= count_summary[0]:
            for item in data:
                if item[bit_idx] == '1':
                    temp_data.append(item) 
        else:
            for item in data:
                if item[bit_idx] == '0':
                    temp_data.append(item) 
    # For CO2 scrubber rating
    elif rating_type == 0:
        if count_summary[0] <= count_summary[1]:
            for item in data:
                if item[bit_idx] == '0':
                    temp_data.append(item) 
        else:
            for item in data:
                if item[bit_idx] == '1':
                    temp_data.append(item)

    return temp_data


def get_last_number(data, type):
    last_number = ""
    for i in range(len(data)):
        if len(data) == 1:
            last_number += data[0]
            break
        else:
            data = filter_by_bit(data, i, type)

    return last_number

# Major part 2 section that computes life support rating
def compute_life_support_rating(data): 
    oxy_gen = get_last_number(data, 1)
    co2_grab = get_last_number(data, 0)

    return int(oxy_gen,2) * int(co2_grab, 2)

# Main function
def main():
    data = read_file_input('input.txt')
    print('-----Part 1-----')
    print(compute_power_consumption(data))
    print('-----Part 2-----')
    print(compute_life_support_rating(data))


if __name__ == '__main__':
    main()