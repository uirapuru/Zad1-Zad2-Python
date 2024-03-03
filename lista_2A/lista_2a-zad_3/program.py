def sum_numbers_from_file(file_name):
    total_sum = 0
    try:
        with open(file_name, 'r') as file:
            for line in file:
                try:
                    number = float(line)
                    total_sum += number
                except ValueError:
                    print(f"Invalid input: {line.strip()}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        return total_sum

# Usage example:
file_name = "list_of_numbers.txt"
total_sum = sum_numbers_from_file(file_name)
if total_sum is not None:
    print(f"The sum of numbers from file '{file_name}' is: {total_sum}")
