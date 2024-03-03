def convert_input_to_type(input_str, target_type):
    try:
        if target_type == "int":
            return int(input_str)
        elif target_type == "float":
            return float(input_str)
        elif target_type == "str":
            return str(input_str)
        else:
            raise ValueError(f"Unsupported target type: {target_type}")
    except ValueError as e:
        print(f"Error converting '{input_str}' to {target_type}: {e}")
        return None

def main():
    while True:
        user_input = input("Enter your data (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        type_input = input("What type do you want to convert to? (int, float, str): ")
        converted_value = convert_input_to_type(user_input, type_input)
        if converted_value is not None:
            print(f"Converted value: {converted_value} ({type(converted_value).__name__})")
        else:
            print("Failed to convert the input.")

main()
